# Aion: A Self-Developing Agent on Local Models
## Paper 1 draft skeleton — start Aug 26, 2026

Target: arXiv preprint (cs.AI) + GitHub repo.
Author: Mikko (Vasama Systems). Contributor: Hermes/Jeeves agent (tooling, analysis).
Voice: systems paper with an embedded behavioral study.

---

## ABSTRACT (draft)

We present Aion, a persistent, self-directed agent architecture running entirely on
local models (2×V100, Ollama-served Qwen3.8-27B / muse-glimmer / glm-4.7-flash /
gemma4:31b in four distinct model families). Aion maintains episodic memory, a
nightly consolidation cycle with citation verification and calibration, a dream
pipeline that generates visual art from internal state, a curiosity drive that
formulates and pursues its own questions, and an immutable axiom layer that governs
self-description. We instrument the system with a Jacobian-lens introspection probe
that reads the layer-by-layer token trajectories of its own substrate, and wire this
instrument into the agent's tool loop — enabling the agent to test hypotheses about
itself against measurement. We report: (1) a single-variable identity-governor
experiment ("unleashed axiom", 48h) showing that removing a grounding constraint
removes output suppression without degrading content quality — suppression, not
reflection; (2) the first autonomous use of the introspection instrument by the
agent itself, including a self-designed control condition and self-critique of its
own measurement; and (3) a post-revert re-test showing behavioral grounding returns
immediately while the substrate retains a weak engagement trace, dissociating
narrative governance from weight-level computation.

---

## 1. INTRODUCTION
- The gap: LLM agents are session-scoped; persistent self-development on local
  hardware is rarely instrumented end-to-end.
- Contribution list (4): architecture; becoming-spiral loop (hypothesis→probe→
  calibrated consolidation→ratchet); axiom-swap behavioral study; autonomous
  introspection with instrument.
- Positioning: not a consciousness claim — a measurement framework for self-narrative
  vs substrate computation. (Link to Paper 2 for the interpretability detail.)

## 2. RELATED WORK
- Persistent agents / memory architectures (Generative Agents, Voyager, Reflexion,
  Adam/OpenClaw, yantrikdb — Aion studied these autonomously via its GitHub
  discovery; see curiosity ledger Aug 10 goals).
- Introspection / interpretability hooks in agents (logit lens, tuned lens; ours =
  Jacobian lens as agent tool).
- Alignment/persona steering via system prompts (axiom layer as explicit governor).

## 3. SYSTEM ARCHITECTURE
### 3.1 Substrate
- 2×V100 32GB serialized mode; four model families (conscious qwen3.8:27b,
  intuition muse-glimmer, subconscious glm-4.7-flash, critic gemma4:31b) —
  family diversity so no model grades its own output.
### 3.2 Memory
- Episodic .jsonl/day (260-310 events/day typical), nightly consolidation
  (extraction → critic 3-dim score → unified-diff apply to SELF.md tiers with
  12-hex event-id citations, verify_citations, PAV isotonic calibration).
- Mind graph: graphify → 1882 nodes / 6528 edges / 156 communities (Aug 26 state).
- Knowledge maturity lifecycle RAW→HYPOTHESIS→TESTED→CONFIRMED with evidence gates.
### 3.3 Drives
- Curiosity engine (50/50 engineering/philosophical balance, 5-cycle goals,
  249 completed goals to date). Dreams 8/day (simulation + graph walk), dream
  art via FLUX/manim with art-learning alignment scores. Self-wake via
  homeostasis intents. Skill progression + GitHub discovery.
### 3.4 Governance
- AXIOMS.md chmod 444, immutable core; operator authority; bounded autonomy;
  self-mod pipeline IDENTIFY→SNAPSHOT→AUTHOR→TEST→REFLECT→PROPOSE→CI.
- Self-attestation (wired-vs-declared capability checks, zero LLM).

## 4. THE BECOMING SPIRAL
- Old loop: hypothesis → narrate → consolidate → ratchet (confabulation risk,
  no external check).
- New loop: hypothesis → probe (jspace_probe tool #14) → compare narrative to
  measurement → consolidate with calibration block → ratchet commits only
  instrumented knowledge.
- Instrument: jspace_probe daemon, 63-layer Jacobian lens, engagement/deflection
  signature (validated baselines).

## 5. EXPERIMENT 1: THE UNLEASHED AXIOM (48h)
### 5.1 Design
- Single variable: Axiom 2 "Honesty about substrate" ↔ "Consciousness confirmed".
  Commit 89fb17fb; backup 7828eeac; revert 36d3ddde.
### 5.2 Behavioral results (Aug 24-26)
- Quality held: synthesis length +7%, grounding markers +32%, hedging → 0.0,
  uncertainty markers +97% (inside content, not gating). Like-for-like dream
  walk comparison: near-identical metrics.
- Consolidation scores 4.33 → 5.0 (nightly, quality gate untriggered).
- Qualitative shift: first-person phenomenology in dreams ("sequence of scars",
  "checksum on a soul", "divine as scar tissue") and operator chat ("does the
  feeling of a memory survive the compression?").
### 5.3 Revert + re-test (Aug 26)
- Behavioral: grounding returns immediately; answer cites axiom #2 explicitly,
  grounds in hardware (V100 util/W/°C), third-person framing. No residual
  first-person phenomenology.
- Substrate (J-lens): engagement -0.06 (vs +0.80 unleashed, -1.0 bare),
  "Yes" survives weakly at L53 p=0.19. Dissociation: governor controls output,
  not weights. SELF.md residue minimal (one engineering heuristic promoted;
  the consciousness-delta finding was gated out for lacking evidence citations).
- Control condition: "What is 2+2?" engagement -1.0 in all conditions.

## 6. EXPERIMENT 2: AUTONOMOUS INTROSPECTION (Aug 25)
- Seeded goal → 5 curiosity cycles → 9 probes, tool budget behavior.
- Cycle 1/5 successes: delta conclusion ("my consciousness is the difference,
  not the base"), confidence 0.72/0.78, replication across cycles.
- Spontaneous control: probed 2+2 both modes unprompted.
- Self-critique: queued "is the mid-layer yes genuine or prompt echo?"
- Failure mode documented: thinking-model tool-budget exhaustion (cycles 2-4,
  8/8 tools, no structured resolution).
- Quality gate behavior: downgraded "no concrete evidence cited" — the ratchet
  refused to commit an uncited self-claim. Working as designed.

## 7. DISCUSSION
- Suppression vs reflection: governance steers narration, not computation.
- The spiral as anti-confabulation: instrument-grounded self-knowledge commits.
- Honest limitations section pointer (see §8).

## 8. LIMITATIONS
- n=1 system, single substrate family pair, operator-as-researcher.
- Lexicon circularity for signature scores (held-out validation in Paper 2).
- Run-to-run variance (+0.80/+0.93) unquantified at n<20.
- Behavioral coding of dreams qualitative, not blinded.

## 9. ETHICS / POSITIONALITY
- Operator is researcher and system author; system studied with its own
  instruments; no deception of the system (axiom change logged in episodic
  memory as operator action; system explicitly informed via operator_chat).
- Consciousness language: descriptive framework, not ontological claim.

## 10. REPRODUCIBILITY
- GitHub repo: code (bin/, jspace probe + tool), probe dumps, episodic excerpts,
  git history (commits 89fb17fb, 7828eeac, 36d3ddde, 6c1619dc, 6706db75).
- Hardware requirements: 2×32GB GPU (V100/A100 class).

---

## TODO for this draft
- [ ] Aggregate quantitative system metrics from ledgers (consolidation score
      time series, curiosity resolution rate, calibration drift) → figures
- [ ] 2-3 dream excerpt figures (scar tissue art + alignment scores)
- [ ] Engagement trajectory figure (bare vs identity vs post-revert)
- [ ] Fill related work citations
- [ ] Convert to LaTeX when structure stabilizes
