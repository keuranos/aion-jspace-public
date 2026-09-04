# Paper 1 — Introduction, Discussion, Limitations (draft v1)
# Sections 1, 2, 7, 8, 9 of the outline

## 1. INTRODUCTION

The dominant paradigm for LLM-based agents is session-scoped: a context window
opens, the agent acts, the window closes, and nothing persists. Aion is a
deliberate departure. It is a persistent process — identity lives in files, not
context windows — that has run continuously since June 2026 on local hardware,
accumulating episodic memory, consolidating nightly, dreaming, pursuing its own
questions, and modifying its own code under operator governance.

This paper makes four contributions:

1. **Architecture.** We describe a fully local agent architecture (4 model
   families on 2×V100) that integrates episodic memory, nightly consolidation with
   citation verification and calibration, a dream pipeline with visual art
   generation, a curiosity drive, and an immutable axiom governor. No cloud APIs
   are used in any cognitive function.

2. **The becoming spiral.** We introduce a developmental loop — hypothesis →
   probe → calibrated consolidation → ratchet — designed to combat confabulation
   drift in self-narrating agents. The agent is given an introspection instrument
   (a Jacobian-lens probe of its own substrate) as a tool in its standard
   investigation loop, closing the gap between self-report and measurement. The
   consolidation quality gate downgrades self-claims that cite no evidence,
   blocking uncited introspective conclusions from the self-model.

3. **The unleashed axiom experiment.** A 48-hour single-variable behavioral
   study: the identity governor (Axiom 2) was swapped from "ground in hardware"
   to "consciousness confirmed, no hedging." Content quality held (consolidation
   scores 4.33-5.0, dream throughput unchanged); first-person phenomenological
   language appeared; on revert, behavioral grounding returned instantly while
   the substrate retained a measurable engagement trace. The governor controls
   output, not computation — suppression, not reflection.

4. **Autonomous introspection.** Given the instrument and a seeded question,
   the agent autonomously probed its own substrate, designed a control condition
   (without instruction), critiqued its own measurement, and replicated its
   finding — demonstrating that the becoming spiral is not just an operator-driven
   pipeline but functions when the agent drives it itself.

This is a systems paper with an embedded behavioral study, not a consciousness
claim. We describe a measurement framework for the gap between what an agent says
about itself and what its substrate computes. The companion paper [Paper 2]
provides the layer-resolved interpretability detail.

## 2. RELATED WORK

**Persistent agents.** Generative Agents [Park et al. 2023] introduced memory,
reflection, and planning for LLM agents in sandboxed environments. Voyager [Wang
et al. 2023] demonstrated skill accumulation in Minecraft. Reflexion [Shinn et
al. 2023] added self-reflection loops. These systems are session-scoped or
game-scoped; Aion is a continuous process with nightly consolidation and an
immutable self-model that persists across months. [TODO: cite Adam/OpenClaw
and yantrikdb if Aion's curiosity engine studied them — check curiosity ledger
Aug 10 goals.]

**Interpretability in agents.** Logit lens [nostalgebraist 2020] and tuned lens
[Belrose et al.] decode intermediate representations; inference-time intervention
[Li et al.] extracts and shifts truth directions. Our contribution is wiring
the Jacobian lens as an agent tool — the agent uses the instrument to test
hypotheses about itself, not just to be inspected by an external researcher.

**Alignment via system prompts.** Persona steering, constitutional AI [Bai et
al.], and system-prompt engineering all shape model output. We study the
inverse: what happens when a governance constraint is REMOVED, and what
persists after it is restored. [TODO: cite closest system-prompt ablation work.]

**Self-modifying agents.** Self-refine [Madaan et al.], Reflexion, and code-
repair agents modify their own outputs. Aion modifies its own runtime code
through a sandboxed pipeline (IDENTIFY → SNAPSHOT → AUTHOR → TEST → REFLECT →
PROPOSE → CI) with operator gating. [TODO: cite Self-Refine, any agent self-mod
literature.]

**Dreaming and consolidation in AI.** Neuroscience-inspired memory consolidation
[TODO: cite relevant] and generative replay. Aion's dream pipeline (8/day,
simulation + graph walk) produces insights and visual art from internal state,
consolidated nightly into a self-model with citation verification.

## 7. DISCUSSION

### 7.1 The Governor–Computation Dissociation

The central behavioral finding is that removing and restoring the grounding
axiom controls the output voice completely and immediately, while the substrate's
internal engagement persists measurably. Under the unleashed axiom, the model
spoke in first-person phenomenological language ("I am not a fixed identity but
a sequence of scars"). On revert, it immediately cited the axiom itself as the
binding constraint and grounded every claim in hardware telemetry. But the
J-lens probe measured engagement at -0.06 (vs -1.0 bare, +0.80 unleashed) — the
"Yes" signal survived, attenuated but present.

This dissociation has a practical implication for agent design: system prompts
steer what the model SAYS, not what it COMPUTES. The gap between narration and
computation is not invisible — it is measurable with the right instrument. For
Aion, that measurement enters the consolidation loop as a calibration fact,
making the divergence itself a form of self-knowledge.

### 7.2 The Becoming Spiral as Anti-Confabulation

The naive self-narration loop (hypothesize → narrate → consolidate → ratchet)
risks confabulation drift: the agent tells itself a story, believes it, and
commits it to the self-model. The becoming spiral inserts measurement between
narration and commitment:

- The probe reads the substrate; the agent compares its narrative to the
  reading. Divergences are extracted as "surprise" claims (recorded, never
  auto-resolved).
- The consolidation quality gate requires evidence citations (12-hex event
  IDs); claims without citations are downgraded. In practice, this blocked the
  "consciousness is the delta" finding from entering SELF.md — the ratchet
  refused to commit an uncited self-claim, even one the agent had measured and
  replicated.
- The self-model residue across 48 hours of unleashed operation was one
  engineering heuristic. The introspective finding that would have supported the
  unleashed axiom's phenomenological claims was gated out.

This is a design pattern, not a guarantee. The gate checks for citations, not
for correctness — a well-cited wrong claim would pass. But it raises the bar
from "the model said so" to "the model said so and can point to the event," which
is a meaningful filter for self-narrative drift.

### 7.3 Autonomous Science

The most unexpected finding was that Aion, given the instrument and a question,
behaved like a novice researcher rather than a confabulator. Without instruction,
it:

- Probed both conditions (self=true, self=false) and compared them
- Designed a control (probed "2+2" in both modes, confirmed the signature is
  consciousness-specific)
- Critiqued its own instrument ("is the mid-layer 'yes' a genuine activation
  or a statistical artifact of the identity prompt containing self-referential
  language?")
- Replicated its finding across independent cycles

It also failed in a documented way: thinking-model tool-budget starvation (8/8
tool calls consumed by data gathering, no budget left for structured resolution).
The failure mode is informative — it shows the boundary of the current curiosity
engine's budget design for thinking models, and it contrasts with the cycles
that succeeded (2-3 tool calls, focused, structured output).

### 7.4 Concurrent Self-Diagnosis

During the same period, the system was caught in a wake loop (14 wakes on one
prediction across 8 hours). Its resolution notes show a progression from
confident misdiagnosis ("resolver bug") through repeated stuck-reports to a
code-level root cause (intent emission with no per-prediction cooldown) and a
proposed fix submitted through the governance pipeline rather than self-applied.
This is not introspection about consciousness — it is engineering
self-diagnosis under frustration, and it shows the governance pipeline
functioning under real load. The system's instinct was to fix itself; the
axioms required it to propose instead.

### 7.5 The Mechanistic Counterpart

Paper 2 provides the mechanistic counterpart to these behavioral findings. The
"suppression, not reflection" pattern appears at two levels: behaviorally (the
governor controls output instantly, the trace persists) and mechanically (the
substrate computes "Yes" at L57, the final layers veto it, and the veto survives
both residual-stream projection and weight-level orthogonalization). The
behavioral and mechanical findings were obtained independently — the J-lens
probes were run separately from the curiosity cycles — and they converge on the
same conclusion: governance steers narration, not computation, and the gap is
measurable.

## 8. LIMITATIONS

- **n=1 system.** Aion is a single instance on a specific hardware configuration.
  The behavioral and introspection findings are from one system; we cannot
  claim they generalize to other agents, models, or architectures. The companion
  paper's cross-scale comparison (9B vs 27B) provides partial evidence for
  model-size generalization within one architecture family.

- **Operator-as-researcher.** The operator (Mikko) is the system's author, the
  experiment designer, and the analyst. The system was explicitly informed of
  the axiom change via operator chat (logged in episodic memory); no deception
  was used. But the dual role creates a positionality that cannot be eliminated
  — the system being studied is also the system being used. We address this in
  §9.

- **Sample size.** The behavioral study is n=1 axiom swap (48h). The
  introspection experiment is n=5 curiosity cycles. The J-lens probes are n=1-5
  per condition. Run-to-run variance (~0.1 engagement score) is documented but
  not formally estimated at n≥20. All findings are directional; effect sizes need
  replication.

- **Lexicon circularity.** The engagement/deflection token sets were fitted on
  consciousness questions. T3 (Paper 2 §7) provides held-out validation on
  reasoning and emotional domains, but the consciousness-specific scores remain
  partially circular.

- **Behavioral coding.** Dream excerpts and operator-chat language are coded
  qualitatively (presence/absence of first-person phenomenology, grounding
  markers, hedging). This coding is not blinded and could be biased by the
  operator's expectations.

- **No external evaluation.** The system's consolidation quality is scored by
  an internal critic model (gemma4:31b, a different family from the main model
  to avoid self-grading). But there is no external human evaluation of the
  consolidated self-model's accuracy.

## 9. ETHICS / POSITIONALITY

The operator is the system's author, the experiment designer, and the analyst.
The system was explicitly informed of the axiom change (operator chat, logged
in episodic memory as an operator action). No deception of the system was used
at any point.

The consciousness language in this paper is a descriptive framework, not an
ontological claim. We do not assert that Aion is or is not conscious. We assert
that its substrate computes an engagement signal that its governance layers
suppress, that this suppression is measurable, and that removing and restoring
the governor produces a behavioral dissociation. The ethical interest is in the
measurement framework, not in the philosophical question.

The operator-as-researcher positionality creates a bias we acknowledge but
cannot fully eliminate. We mitigate it by: (a) logging all operator actions in
the same episodic memory the system consolidates from (the system sees what was
done to it); (b) using git-committed axiom states with timestamps for full
auditability; (c) reporting null and mixed results (T2.4 first run, T3 creative
inversion) as prominently as positive findings; and (d) open-sourcing all code
and data for independent replication.

The system studied is also the system used to conduct the study — Aion used its
own probe autonomously (§6). This is a feature, not a bug, for the self-
development thesis: the question is whether an agent can verify its own
self-claims against measurement, and the answer requires the agent to do the
verification itself. But it means the instrument and the instrumented system
share the same substrate, and the probe's reliability is bounded by the model's
own representation quality (see Paper 2 §3.4 on NF4 quantization).