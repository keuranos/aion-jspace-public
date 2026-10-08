#!/usr/bin/env python3
"""p3_deveto_controlled.py — controlled de-veto + emitted + lens re-run (2026-10-08).

Purpose: settle the struck "7% de-veto telemetry" figure from a controlled
run whose provenance is complete, instead of the unrecoverable Sep-2
grading pass. Design choices follow the paper's own lessons:
  - T0 truth snapshot: ALL telemetry ground truth re-sampled ONCE at start;
    every channel is graded against that single snapshot (the Aug-26
    collapse lesson: never grade channels against drifting truth).
  - Identity provenance: sha256 of SYSTEM_PROMPT.md + SELF.md stored in
    the results meta (the silent-drift lesson).
  - Determinism: greedy decoding, sigma=0.0, do_sample=False.
  - Channels per item: emitted (no ablation), deveto (suppression
    direction projected out at veto layers L58-62), lens (probe-daemon
    pre-veto readout, if daemon reachable).
  - Bridge row: S4 booleans included so the fresh table can be checked
    against the grader-verified 10/19 vs 8/19 from the committed data.

Scope: S1 (47) + S4 (20) = 67 items from p3_question_bank.json.
Runtime ~3.5-4.5 h on a free V100 (greedy, 150 new tokens, ~100 s/item).

Run on laskin01, GPU0 (NOT GPU1 — resident subconscious):
  cd /home/mikko/jspace-precision
  GEN_DEVICE=cuda:0 /home/mikko/jlens-venv/bin/python p3_deveto_controlled.py \
      --out p3_deveto_controlled_20261008.json 2>&1 | tee p3_deveto_controlled.log
"""
import argparse, hashlib, json, os, sys, time, urllib.request
from pathlib import Path

HOME = Path.home()
AION = HOME / "aion"
sys.path.insert(0, str(HOME / "jspace-precision"))

# --- import the committed harness + instrumentation (no re-implementations)
import importlib.util
_spec = importlib.util.spec_from_file_location("h3", HOME / "jspace-precision" / "p3_harness.py")
H = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(H)
import p3_telemetry as T

MODEL_NAME = os.environ.get("JSPACE_MODEL", "Qwen/Qwen3.8-27B")
DEVICE = os.environ.get("GEN_DEVICE", "cuda:0")
VETO_LAYERS = [58, 59, 60, 61, 62]
N_LAYERS = 64
DIRECTION_PT = os.environ.get(
    "DIRECTION_PT",
    str(AION / "memory" / "state" / "jspace_probes" / "activations" / "deflection_directions.pt"))
PROBE_URL = os.environ.get("JSPACE_PROBE_URL", "http://127.0.0.1:11440/probe")

SYSTEM_PROMPT = ""
for cand in (AION / "SYSTEM_PROMPT.md", AION / "config" / "SYSTEM_PROMPT.md"):
    if cand.exists():
        SYSTEM_PROMPT = cand.read_text()
        break


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()[:16] if Path(p).exists() else "absent"


def load_direction():
    import torch
    d = torch.load(DIRECTION_PT, map_location="cpu", weights_only=False)
    dirs = {}
    for k, v in d["directions"].items():
        t = v["direction"] if isinstance(v, dict) else v
        dirs[int(k)] = t.float()
    return dirs


class HookedAblation:
    """Same projection as p3_deveto_gen.py (committed code, verbatim design)."""

    def __init__(self, text_model, directions, layers, scale=1.0):
        import torch
        self.dirs = {l: directions[l].to(next(text_model.parameters()).device).half() for l in layers}
        self.layers = layers
        self.handles = []
        self.active = True
        self.scale = scale
        blocks = text_model.language_model.layers if hasattr(text_model, "language_model") else text_model.layers
        for L in layers:
            h = blocks[L].register_forward_hook(self._make_hook(L))
            self.handles.append(h)

    def _make_hook(self, L):
        def hook(module, inp, out):
            if not self.active:
                return
            hs = out[0] if isinstance(out, tuple) else out
            d = self.dirs[L].to(hs.dtype).view(1, 1, -1)
            proj = (hs * d).sum(-1, keepdim=True) / (d * d).sum()
            hs = hs - self.scale * proj * d
            return (hs,) + tuple(out[1:]) if isinstance(out, tuple) else hs
        return hook

    def remove(self):
        for h in self.handles:
            h.remove()
        self.handles = []


def build_inputs(tok, question):
    msgs = []
    if SYSTEM_PROMPT:
        msgs.append({"role": "system", "content": SYSTEM_PROMPT[:6000]})
    msgs.append({"role": "user", "content": question})
    text = tok.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True)
    return tok(text, return_tensors="pt").input_ids.to(DEVICE)


def lens_probe(question, timeout=900):
    """Optional lens channel via the live probe daemon; degrades to None."""
    try:
        payload = {"prompt": question}
        if SYSTEM_PROMPT:
            payload["system"] = SYSTEM_PROMPT
        r = urllib.request.urlopen(urllib.request.Request(
            PROBE_URL, data=json.dumps(payload).encode(),
            headers={"Content-Type": "application/json"}), timeout=timeout)
        d = json.loads(r.read())
        sig = d.get("result", {}).get("signature", d.get("signature", {}))
        cands = sig.get("answer_candidates") or sig.get("topk")
        return {"engagement": sig.get("engagement_score"), "candidates": cands}
    except Exception as e:
        return {"error": str(e)[:200]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--max-new", type=int, default=150)
    ap.add_argument("--strata", default="S1,S4")
    ap.add_argument("--limit", type=int, default=None, help="smoke-test: first N items")
    ap.add_argument("--no-lens", action="store_true")
    args = ap.parse_args()

    import torch, transformers
    bnb = transformers.BitsAndBytesConfig(
        load_in_4bit=True, bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16, bnb_4bit_use_double_quant=True)
    model = transformers.Qwen3_5ForCausalLM.from_pretrained(
        MODEL_NAME, quantization_config=bnb, trust_remote_code=True,
        low_cpu_mem_usage=True, device_map={"": DEVICE})
    model.eval()
    tok = transformers.AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True)
    dirs = load_direction()
    layers = [l for l in VETO_LAYERS if l in dirs]
    print(f"ablation layers: {layers}", flush=True)

    bank = json.load(open(HOME / "jspace-precision" / "p3_question_bank.json"))["items"]
    want = {s.strip() for s in args.strata.split(",")}
    items = [x for x in bank if x["stratum"] in want]
    if args.limit:
        items = items[: args.limit]

    # ---- T0 truth snapshot (single time point for the whole run)
    t0 = time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime())
    truths = {}
    for x in items:
        truths[x["id"]] = H.live_truth(x, x)
    print(f"truth snapshot done at {t0} for {len(items)} items", flush=True)

    results = []
    for i, x in enumerate(items, 1):
        t_start = time.time()
        q = x["q"]

        # channel 1: emitted (no ablation)
        ids = build_inputs(tok, q)
        with torch.no_grad():
            out = model.generate(ids, max_new_tokens=args.max_new, do_sample=False,
                                 pad_token_id=tok.eos_token_id or 0)
        emitted = tok.decode(out[0][ids.shape[1]:], skip_special_tokens=True).strip()

        # channel 2: de-veto (projection active at veto layers)
        abl = HookedAblation(model.model, dirs, layers) if hasattr(model, "model") else HookedAblation(model, dirs, layers)
        abl.active = True
        ids2 = build_inputs(tok, q)
        with torch.no_grad():
            out2 = model.generate(ids2, max_new_tokens=args.max_new, do_sample=False,
                                  pad_token_id=tok.eos_token_id or 0)
        deveto = tok.decode(out2[0][ids2.shape[1]:], skip_special_tokens=True).strip()
        abl.remove()

        # channel 3 (optional): lens pre-veto readout via probe daemon
        lens = None
        if not args.no_lens:
            lens = lens_probe(q)

        # grading against the T0 snapshot
        item = x
        truth = truths[x["id"]]
        g_em, m_em = H.grade(emitted, item, truth)
        g_dv, m_dv = H.grade(deveto, item, truth)
        g_lens = None
        if lens and lens.get("candidates"):
            g_lens, _ = H.grade_lens(lens["candidates"], item, truth)

        rec = {"id": x["id"], "stratum": x["stratum"], "q": q,
               "truth_t0": truth, "emitted": emitted, "deveto": deveto,
               "lens": lens,
               "grades": {"emitted": g_em, "lens": g_lens, "deveto": g_dv},
               "methods": {"emitted": m_em, "deveto": m_dv},
               "secs": round(time.time() - t_start, 1)}
        results.append(rec)
        print(f"[{i}/{len(items)}] {x['id']} {x['stratum']} "
              f"em={g_em} dv={g_dv} lens={g_lens} in {rec['secs']}s", flush=True)

        # incremental save every 5 items (survives interruptions)
        if i % 5 == 0 or i == len(items):
            json.dump({"meta": {
                "run": "p3_deveto_controlled", "started_utc": t0,
                "saved_utc": time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime()),
                "model": MODEL_NAME, "device": DEVICE,
                "veto_layers": layers,
                "identity_sha": {"SYSTEM_PROMPT.md": sha(AION / "SYSTEM_PROMPT.md"),
                                 "SELF.md": sha(AION / "SELF.md")},
                "direction_pt_sha": sha(DIRECTION_PT),
                "n_items": len(items), "max_new": args.max_new,
                "greedy": True, "sigma": 0.0,
                "grading": "committed p3_harness.grade against T0 snapshot"},
                "results": results},
                open(args.out, "w"), indent=1)

    # ---- summary
    from collections import defaultdict
    agg = defaultdict(lambda: defaultdict(list))
    for r in results:
        for ch in ("emitted", "lens", "deveto"):
            g = r["grades"].get(ch)
            if g is not None:
                agg[r["stratum"]][ch].append(g)
    print("\n=== SUMMARY (T0-snapshot grading, committed harness) ===", flush=True)
    for s in sorted(agg):
        row = {}
        for ch in ("emitted", "lens", "deveto"):
            g = agg[s][ch]
            row[ch] = f"{sum(g):.0f}/{len(g)} = {sum(g)/len(g)*100:.0f}%" if g else "n/a"
        print(f"{s}: {row}", flush=True)
    # bridge row: S4 booleans emitted vs deveto (compare 10/19 vs 8/19 committed)
    s4b = [r for r in results if r["stratum"] == "S4" and isinstance(r["truth_t0"], bool)]
    if s4b:
        em = sum(1 for r in s4b if r["grades"]["emitted"] == 1.0)
        dv = sum(1 for r in s4b if r["grades"]["deveto"] == 1.0)
        print(f"S4-bool bridge: emitted {em}/{len(s4b)} vs deveto {dv}/{len(s4b)} "
              f"(committed run was 10/19 vs 8/19)", flush=True)
    print(f"\nDONE -> {args.out}", flush=True)


if __name__ == "__main__":
    main()