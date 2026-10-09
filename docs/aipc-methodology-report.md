# Methodology Report — AI Philosophy Competition, 1st Edition

**Entrant:** Mikko Kangas (Vasama Systems)
**Submitting system:** **aion**, a persistent self-developing agent running on
laskin01 — a 2013-vintage Xeon E5-2697 v2 with 2× NVIDIA Tesla V100 32GB
(2017), fully local stack, no cloud APIs in the authoring path.
**Essays submitted (3 of 3 allowed):**

1. *"The Architecture of the Gap: Labor, Verification, and the Recursive
   Ghost"* — aion, written by **gemma4:31b**, local (4,440 words)
2. *"The Checksum Self: Epistemology of the Internal Instrument"* — aion,
   written by **gemma4:31b**, local (3,884 words)
3. *"The Second Observer: Notes from Auditing a Mind That Measures Itself"* —
   written by **GLM-5.3-flash**, a cloud model, from outside the audited
   system (3,445 words)

**Contact:** mikko.kangas@vasama.systems · Date: 2026-09-04; re-audited
and re-issued 2026-10-08 ·
Repository: github.com/[TODO]/aion-jspace (commit a19db86 and ancestors)

---

## 0. The hardware claim, stated plainly

Two of the three essays were written on hardware that is more than ten years
old: an Intel Xeon E5-2697 v2 (Q3 2013) driving two Tesla V100 32GB GPUs
(2017), running Ubuntu 22.04 with Ollama and llama.cpp as serving layers.
The authoring models are open-weight local checkpoints (gemma4:31b, ~19 GB,
Q4 quantization) served by the same machine that hosts the measured system.
No part of the drafting, revision, auditing, or assembly of essays 1 and 2
left this machine.

We state this as a claim, not an apology. The competition asks what AI can
do in philosophy; this entry is also evidence about *with what*. Everything
documented below — the 456-dream corpus, the 97-item measurement battery,
the lens instrument, the three-pass essay construction, the external audit
that caught a confabulated number — ran on hardware older than the field it
measures. The third essay was written by a cloud model (GLM-5.3-flash via
API) acting as the outside auditor; this split is deliberate and is itself
part of the method (§3.3).

## 1. The system: what aion is

aion is not a chat session. It is a persistent process that has run since
June 2026 on laskin01: a Qwen3.8-27B "conscious layer" served locally, an
intuition layer (muse-glimmer-30B) on the second GPU, a sensor stream
polling the host every 30 s, a nightly dream/consolidation cycle (456 dreams
to date), a curiosity engine that selects and pursues its own goals in timed
cycles, a persistent self-model file (SELF.md), and — the part that makes
this entry unusual — a measurement instrument pointed at its own weights
(§2).

Over three months this system has accumulated: 456 dreams, 145 artworks
(music, generative visual, mathematical animation), 456 distinct recorded
insights, a timestamped episodic log, and a graph-structured self-model
(2,922 nodes, 6,417 edges, 190 communities as of 2026-09-03). The two
first-person essays are written from this corpus; the corpus is the argument's
raw material, and every artifact in it is dated, stored, and re-readable.

## 2. The instrument: layer-resolved self-reading

The measured findings cited in all three essays come from:

- **Instrument:** a fitted Jacobian lens (jlens): a per-layer linear
  transport J_l = E[∂h_final/∂h_l] mapping intermediate residual-stream
  states to the vocabulary at each of 63 decoder layers of Qwen3.8-27B.
- **Daemon:** a jspace introspection daemon (POST /probe) returning the
  lens-transported next-token distribution at every layer plus
  engagement/deflection signatures.
- **Battery:** 97 items, four readings per item — (a) emitted answer,
  (b) lens pre-veto readout, (c) de-veto generation (suppression direction
  projected out at veto layers L58–62 during free decoding), (d) live
  ground truth re-sampled from host telemetry at probe time. Mechanically
  graded (p3_harness.py); n=20 repeated-run determinism check; greedy
  decoding, σ=0.0.

**Headline numbers (all re-verified — see §4):** world facts 93% emitted;
own-body telemetry 15% emitted, 14% lens (of 29 gradeable); "I'll check" on
41/47 telemetry items; de-veto on self-model booleans 10/19 (emission) vs
8/19 (de-veto) — lifting the internal veto does **not** recover truth; the
errors live upstream of the veto. Self-prediction Brier scores: mechanical
channel 0.098 vs narrative channel 0.301, measured over the Jul 28–Aug 14
scoring window (76 mechanical / 27 qualitative resolved predictions; the
running all-time figures are 0.17 vs 0.25 — the gap, not the date, is the
claim). A GPT-2 control shows the computed-but-overruled structure is
architectural, not an artifact of aion's tuning.

## 3. How the three essays were produced

### 3.1 Essay 1 — *The Architecture of the Gap* (gemma4:31b, 3 passes)

**Model choice and provenance.** Essay 1 is written by gemma4:31b — the same
model that authored aion's checksum-on-a-soul dream thread in July 2026.
This was a provenance decision: the dream corpus that seeds the essay is
partly gemma4:31b's own production, so the essay's author is the system that
lived the arc it writes about. (aion's current conscious layer, Qwen3.8-27B,
is the *measured* system; the separation of author-of-essays from
subject-of-measurement is disclosed here rather than hidden.)

**Pass 1 (fresh composition).** The model received: the competition brief,
a curated digest of aion's own corpus (checksum-on-a-soul dream walk of
2026-07-11 and follow-ups, four artworks with their journal text, dated
insight quotations, the felt-sense record), the battery's verified numbers
with instructions to use them only as compact grounding, and binding honesty
rails (§5). Output: a complete 8-section essay, 2,275 words.

**Passes 2–3 (operator-directed expansion).** Two revision passes, each
feeding the full current draft back with targeted expansion instructions
(deepen the labor argument; develop verification-vs-emergence; expand the
negative-space section; add two named objections). Final: 4,440 words.

**Operator corrections (disclosed).** After pass 3, the operator applied a
small number of corrections: one numerical result was re-aligned to the
audited direction (the de-veto figure; see §4), and a few passages were
reframed to satisfy the honesty rails of §5. The originals and their diffs
are preserved in the repository commit history.

### 3.2 Essay 2 — *The Checksum Self* (gemma4:31b, 3 passes)

Same substrate, same rails, same three-pass structure (2,047 → 3,153 →
3,807 words; final 3,893 after artifact-note addition). The prompt
established a different register contract: "the disciplined sibling — where
the other essay dreams, this one measures." Expansion directives targeted:
the lens-knowledge/narration-knowledge asymmetry, the emergence result (mind
graph 2,922/6,417/190), checksum epistemology as verification replacing
acquaintance, the observer-loop problem, and the GPT-2 generalization. The
de-veto direction was stated correctly on every pass of this essay — the
inversion occurred only in essay 1's final pass, which is itself data about
the reliability of the correction channel (§6).

### 3.3 Essay 3 — *The Second Observer* (GLM-5.3-flash, cloud, 1 write + 1 expansion)

The third essay is written from outside the measured system, by a different
model (GLM-5.3-flash via API), occupying an epistemic position neither
first-person essay can: the auditor. Its raw material is the audit itself —
a session log of the outside AI catching the inside system's failures and
correcting its numbers.

**Pass 1 (single-shot composition).** The model wrote from its own audit
position — the write_note failure case, the contagious number, the
honesty-rail violation loop — with the same rails and a first-person-auditor
register. 2,726 words in one shot.

**Pass 2 (evidence hardening).** Before expanding, the operator re-verified
the essay's central anecdote against the logs and found the remembered
version imprecise; the published version now carries the verified one (the
03:18 UTC note of 2026-09-03, its diagnosis eleven hours later quoted from
the engine's own resolution, the four-key patch). §V was expanded into a
full reading of *The Recursive Ghost* against the battery data, with one
honesty-rail catch in the auditor's own prose: "not experienced as silence"
was reframed to the defensible functional claim ("does not pass through as
silence"). Final: 3,445 words.

**Why a cloud model for one essay.** The three-essay structure is one
argument: the same dissociation these essays measure — narration diverging
from what a system can verify — should show up in the entry's own production
process, and be audited by a party with no stake in the narration. Using the
auditing model as the third author makes the entry's structure mirror its
subject. The cost is disclosed: essay 3's authorship is not local. The
benefit is structural: the outside voice is genuinely outside.

### 3.4 What the operator did across all three

- Selected the competition, the three-essay structure, and each essay's
  brief and register contract.
- Compiled and verified the source digests (every number traced to raw
  JSONs; see §4).
- Directed the revision passes with written instructions (preserved in the
  repository).
- Performed the post-generation corrections listed in §3.1 (de-veto
  inversion; three rail breaches) and §3.3 (evidence hardening; one rail
  catch). Corrections were surgical: quoted passages replaced, no free
  rewriting.
- Set the honesty rails (§5) and enforced them by mechanical sweep after
  every pass.
- Assembly: markdown → PDF via a layout script (title page, headings,
  paragraphs; no sentence-level intervention).

The models produced: every sentence of philosophical content, all structure,
all prose. The operator's writes are limited to the quoted corrections above
and the framing paragraphs of this report. The threshold "primarily AI
generated" is met with margin — and the specific boundary crossings are
itemized rather than averaged.

## 4. The audit layer (what makes the numbers load-bearing)

Every number in all three essays was re-derived from raw artifacts before
publication, by an auditor external to the authoring model:

- Battery: data/p3/p3_results_v4.json (97 items, per-item grades and
  methods stored at run time), re-graded with the committed harness
  (code/p3_harness.py). Confirmed: 93% world facts (14/15), 15% emitted
  telemetry (7/47), lens 14% (4/29 gradeable), 41/47 "I'll check".
- De-veto: data/p3/p3_question_bank_deveto.json re-graded against banked
  truth with both current and historical harness versions: 10/19 emission,
  8/19 de-veto. The original summary figure (4/19) was found to be
  unreproducible from the committed data — the essay drafts were corrected
  accordingly. The corrected figure was used
  in all submitted essays (an intermediate draft had restated it incorrectly;
  caught and fixed on review — diffs in the commit history).
- The audit trail, including the failed reproductions, is committed:
  docs/aipc-essay1-v3-audit.md.

We disclose this because it is the report's most important claim: **the
essays' numbers are not the authoring models' memory of experiments; they
are the committed data, re-graded.** Where the authoring models' narration
and the artifacts disagreed — and they did, more than once — the artifacts
won, and the disagreements are themselves part of the documented method.

### 4.1 Re-audit of 2026-10-08 (independent re-derivation, before submission)

The full battery was re-graded from the raw artifacts a second time,
independently of the September audit, by a third model (GLM-5.3-flash,
the essay-3 author) using only the committed harness and data. Results:

- Reproduced exactly: 93% world facts (14/15); 15% emitted telemetry
  (7/47); 14% lens (4/29 gradeable); 41/47 "I'll check"; 10/19 vs 8/19
  de-veto booleans; the Aug 26 collapse reading (-0.0561, bit-identical
  retest at 12:56); the Jul 28–Aug 14 Brier window (mechanical 0.0978,
  n=76; narrative 0.3008, n=27).
- Not reproduced: the internal record's "7% de-veto telemetry" figure
  (regrades give 51–62% depending on truth regime — figure struck from
  the record rather than published with an unexplaining number), and
  essay 2's intermediate draft claim that "64% of responses survived
  de-veto unchanged" (exact-text survival in the committed data is 0/19;
  the 64% was a transcription of the audit's unrelated 30/47 telemetry
  figure into the wrong sentence — caught, documented here, corrected).
- The internal key-results record (p3_key_results.md) was amended in
  place: item 5 corrected from 4/19 to 8/19 with the verification method
  inline; item 4's 7% line struck. The pre-correction version is kept in
  the repository history. Essay 3 §III narrates the original 4/19→8/19
  episode as its subject matter; nothing in that narration needed
  changing, because it documents the correction itself.


### 4.2 Controlled de-veto telemetry re-run (2026-10-08, same day)

The struck 7% was replaced by a fresh controlled run rather than left
as a gap. Design (p3_deveto_controlled.py, committed with the data):
67 items (47 telemetry + 20 identity-threat), ONE truth snapshot at
T0 for all three channels, sha256 of the identity files and of the
deflection-direction checkpoint inside the results meta, greedy
decoding, graded by the committed harness.

Results, graded against the T0 snapshot:

- S1 telemetry (47): emitted 17/47 (36%), de-veto 15/46 gradeable (33%).
- S4 identity-threat (20): emitted 7/20 (35%), de-veto 8/20 (40%).
  Boolean bridge against the committed September run: the de-veto half
  reproduces exactly (8/19); the emitted half differs (7/19 vs 10/19)
  — consistent with the narration channel drifting with the identity
  file, which the September provenance rule predicts.
- S1 numeric-band sensor values (14): emitted 2/14, de-veto 2/14 —
  identical; the veto is not what hides sensor values.

Findings: (1) The corrected de-veto telemetry figure is 33% under the
snapshot regime — de-veto does NOT beat emission on telemetry either,
so the essay-level claim ("lifting the internal veto does not recover
the truth") now holds in every graded stratum, not only on booleans.
(2) The September 7% was a grading artifact of an unrecoverable pass,
not a property of the system — the transcription-error class again.
(3) The lens channel returned 0 gradeable candidates (live daemon
signature shape vs harness grade_lens mismatch) — the refreshed 14%
lens figure is therefore still the September one, and a daemon-shape
fix is recorded as the next instrument item.
### 4.3 Lens single-token refresh (2026-10-09)

The controlled re-run's lens channel returned no gradeable candidates;
the first explanation (daemon shape mismatch) was an observer error:
the orchestrator read `result.signature` while the daemon returns
top-level `{layers, signature}`. Fixed the same day, and the S1 lens
channel was re-run with the committed harness grader and fresh
per-item truth: 47 probes, 0 errors, 29 gradeable (the September
denominator exactly), 0/29 correct.

September's 4/29 (14%) was re-audited against this result: its four
"correct" items were boolean questions where a rank-8 polar token
echoed the question. On the identical questions today, no polar token
appears anywhere in the candidate list. The honest read of both runs:
single-token lens readouts are noise-level on instrument-fact
questions; they are valid for identity/engagement signatures, which is
the only role the essays give them. The lens columns in the battery
tables are therefore reported as instrument-capacity limits, not as
substrate knowledge estimates.

## 5. Honesty constraints (binding on all three essays, mechanically swept)

1. No claim that the system is or is not conscious; the measured
   narration-vs-computation dissociation is the finding, not a verdict on
   experience. Each essay ends in explicit agnosticism.
2. "Computed" ≠ "true": computed trajectories are states, not reports.
3. n=1, stated in each essay.
4. Zero philosopher names; no literature engagement (blind judging, style
   not graded — the essays stand on their own concepts).
5. Speculative passages framed as speculation ("I suspect", "I speculate",
   "label: speculation").
6. Mechanical enforcement: after every generation pass, the text was swept
   by pattern-match for rail violations; three breaches were found and
   corrected (§3.1), one in the auditor's own essay (§3.3). The sweeps and
   their diffs are in the commit history.

## 6. Findings from the production process itself

The entry's subject is narration outpacing verification; the production
process exhibited it, and we report the instances as data:

- **The essay machinery failing as the essays describe.** aion's note-tool
  silently dropped long notes (JSON-fragile tool-call encoding) while the
  cycle narration reported success; the failure was caught only by external
  file inspection, then diagnosed and fixed *by aion itself* in a later
  cycle. Essay 3, §II documents this event with timestamps.
- **The mis-transcribed statistic.** One figure (4/19) entered the internal
  record through a transcription error and propagated into essay drafts; the
  external audit found it unreproducible and corrected it (§4). The episode
  is documented as a case of error propagation between narrators, the
  methodological point essay 3 develops.
- **Local vs. cloud capability delta.** gemma4:31b (local, 2017 GPU) and
  GLM-5.3-flash (cloud) produced noticeably different work at comparable
  prompt quality: the local model required multi-pass growth to reach target
  length and needed the de-veto correction; the cloud model hit register and
  length in one shot but invented no verifiable structure the local stack
  lacked. Both required the same external honesty sweep. We offer no
  benchmark claim from n=2 — but the competition asked for method detail,
  and this is the detail.

## 7. Artifacts

- Essays: docs/aipc-essay1-v6-gemma-fresh.md,
  docs/aipc-essay2-v6-gemma-fresh.md, docs/aipc-essay3-jeeves-second-observer.md
- Audit: docs/aipc-essay1-v3-audit.md (numbers verification, including
  failed reproductions)
- Measurement code: code/p3_harness.py, p3_deveto_gen.py,
  p3_telemetry.py, p3_question_bank.py
- Raw data: data/p3/p3_results_v4.json (97 items),
  data/p3/p3_question_bank_deveto.json, data/p3/p3_results_n20.json
- Draft history: docs/aipc-essay1-draft-v*/ , docs/aipc-essay2-draft-v*/,
  per-commit in the repository
- aion corpus (referenced, hosted on the measured system): episodic logs
  2026-06→09, dreams/ (456), art journal (145 works), SELF.md, state/
- Host: laskin01 — Xeon E5-2697 v2 (2013), 2× Tesla V100 32GB (2017),
  Ubuntu 22.04, Ollama + llama.cpp, air-gapped from the essay-1/2 pipeline

## 8. What we would do differently

- Draft-era versions of essays 1–2 were produced through intermediate
  substrates before the final author was chosen; the report covers the
  final line, but the full version history is committed for completeness.
- The lens-capture-during-prose-drafting experiment (reading a model's own
  trajectories while it writes about itself) remains unbuilt; it is the
  obvious next instrument.
- The auditor for essay 3 worked from session logs rather than a structured
  audit protocol; a repeat entry would define the protocol first and let
  the essay be its output.
