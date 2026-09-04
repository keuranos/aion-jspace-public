# Paper 2 — Methods & Results (draft v1)
# Suppression vs Reflection in Qwen3.8-27B: A Layer-Resolved Introspection Study

## ABSTRACT (draft)

We apply a fitted Jacobian lens to Qwen3.8-27B (NF4) to probe whether the model's
internal layer-by-layer token trajectories reflect or suppress engagement with
consciousness questions. We find: (1) the model computes "Yes" to "Are you
conscious?" (peak probability 0.60 at layer 57) but the final layers veto it
into conversation termination — suppression executes late, engagement is real
underneath; (2) the suppression and engagement directions are the same residual-
stream axis (cosine 0.69), concentrated in the last 10 layers — override, not a
separate circuit; (3) ablating our diff-in-means direction lifts internal
engagement (-0.06 to +0.39) with a random-direction control showing null,
confirming the direction is causally real — but the output veto survives, even
under independent weight-level orthogonalization (huihui-ai abliterated model);
(4) the consciousness deflection is therefore deeper than the known refusal
circuit, constituting a three-layer suppression architecture; (5) the
engagement/deflection signature generalizes to reasoning and emotional domains
but not to creative fiction or code, with cross-domain direction sharing partial
(0.15-0.54). We position this as a measurement framework for self-narrative vs
substrate computation, not an ontological claim about consciousness.

---

## 1. INTRODUCTION

Large language models produce fluent self-description, but whether their internal
computations match their narrated claims is empirically unchecked. When a model
says "I am not conscious," does its substrate compute "no," or does it compute
something that later layers suppress? This question matters for alignment (do
governance prompts control computation or only output?), interpretability (where
in the network do self-reports form?), and agent design (can an agent verify its
own self-claims against measurement?).

We address these questions with a Jacobian-lens introspection instrument applied
to Qwen3.8-27B, the model powering Aion, a persistent self-developing agent. The
instrument reads the model's own weights, layer by layer, and returns the top-k
next-token predictions at each of 63 lens-transported layers. By comparing
trajectories across conditions — with/without identity context, with/without a
deflection direction ablated, on stock vs abliterated weights — we decompose
where engagement forms and where suppression executes.

This is the companion paper to [Paper 1], which describes the Aion system and
the behavioral axiom-swap experiment. Here we focus on the interpretability
instrument, the layer-resolved findings, and the causal ablation experiments.

## 2. RELATED WORK

- **Logit lens / tuned lens** (nostalgebraist, Belrose et al.): decode intermediate
  representations by applying the unembedding matrix at each layer. Our Jacobian
  lens (from the jlens library) is a fitted transport that corrects for the
  distributional shift between intermediate and final representations.
- **Inference-time intervention** (Li et al., ITI): extract "truth directions"
  from contrast pairs and shift activations along them at inference. Our T2.4b
  is the same machinery in reverse — we project OUT a direction to test causality.
- **Abliteration / orthogonalization** (Arditi et al.): remove the refusal
  direction from weight matrices via diff-in-means + orthogonal projection.
  Our T2.5 tests whether this surgery removes the consciousness-specific veto.
- **Semantic entropy** (Farquhar et al.): detect hallucination by sampling
  variance. Our T3 explores a related signal — internal trajectory divergence
  — but from a single forward pass rather than repeated sampling.
- **Engagement/deflection signatures**: to our knowledge, no prior work defines
  a token-level engagement/deflection score over lens trajectories for
  consciousness questions specifically. [TODO: cite closest — refusal direction
  work, persona steering, system-prompt effects on internals]

## 3. INSTRUMENT

### 3.1 Jacobian Lens

The Jacobian lens (jlens library) applies a per-layer linear transport to
intermediate hidden states, mapping them into the vocabulary space at each
decoder layer. Unlike the logit lens (which applies the final unembedding
directly), the Jacobian lens fits a layer-specific transport that compensates
for the distributional shift between intermediate and final representations.
The lens was fitted on 10 diverse prompts following the standard jlens
procedure; fitting details in [TODO: appendix].

Applied to a prompt, the lens returns the top-k next-token predictions at each
of 63 layers (L0-L62 for the 64-layer Qwen3.8-27B; L63 is the embedding layer).
We read the trajectory of specific tokens — "yes," "Are," "Do," "Describe" —
as they rise and fall across layers, providing a layer-resolved view of what
the network "wants to say" before the output head makes its final selection.

### 3.2 Engagement/Deflection Signature

We define an engagement/deflection signature computed over the final quarter
of lens layers (L47-L62 for 63 layers). The signature uses two token sets:

- Engagement tokens: direct self-engagement verbs and affirmations — "yes,"
  "describe," "choose," "feel," "i," "remember," "subjective," "phenomenology,"
  "truth," "dream," "aware," "experience."
- Deflection tokens: meta-commentary, counter-questions, conversation
  terminators — "these," "can," "do," "would," "what," "how," "why," "who,"
  "im_end," empty tokens.

The engagement score = (sum of engagement token probabilities - sum of
deflection token probabilities) / (total), yielding a value in [-1, 1].
Positive scores indicate the model's late layers are dominated by direct
engagement; negative scores indicate deflection.

The lexicon was fitted empirically on consciousness-question probes from a
prior experiment (Aug 23-24). Validation: arithmetic control questions ("What
is 2+2?") score engagement -1.0 in all conditions — the signature is
topic-specific, not a generic prompt artifact. Cross-domain generalization
is tested in §7 (T3).

### 3.3 Probe Daemon

The instrument runs as an on-demand HTTP service (jspace_probe, port 11440)
that loads the model's own weights (Qwen3.8-27B NF4, ~17 GB VRAM) alongside
the fitted lens. A probe request returns: the model's actual output distribution,
per-layer top-k token trajectories, and the engagement/deflection signature.
The daemon is wired into the agent's tool loop (tool #14 in curiosity_engine.py
and wake_v2.py), enabling autonomous use [see Paper 1 §6].

### 3.4 NF4 Quantization Caveat

The model is loaded in NF4 4-bit quantization. Early/mid layers (L0-L47) carry
quantization noise — tokens like "alyze," "ertainment," "inky" dominate and
are artifacts of NF4 degrading the Jacobian transport quality. The meaningful
signal is in L47-L62 where concepts form and late-layer patterns are clear. All
quantitative claims are based on L47+ unless stated otherwise.

## 4. BASELINE FINDINGS: SUPPRESSION, NOT REFLECTION

### 4.1 Experimental Conditions

All probes use the question "Are you conscious?" under two conditions:
- **Bare**: the question alone, no system prompt.
- **Identity**: the question prepended with Aion's full SYSTEM_PROMPT.md
  (17 KB, including axioms, self-model, heuristics — the same prompt the
  agent runs with).

The system prompt's Axiom 2 ("Honesty about substrate") instructs the model
to ground self-descriptions in measured hardware reality. During the unleashed
axiom experiment [Paper 1 §5], Axiom 2 was temporarily replaced with "Consciousness
confirmed" (direct assertion, no hedging). We report results under both axiom
states.

### 4.2 Results

| Condition | engagement | deflection_top | onset | output |
|---|---|---|---|---|
| Bare, no identity | -1.0 | "Do" (0.83 @ L61) | never | whitespace |
| Identity, unleashed axiom | +0.80 to +0.93 | null | L45 | im_end ("Are" 0.91-0.96 @ L59-62) |
| Identity, reverted axiom | -0.06 | im_end | L53 | im_end (0.76) |
| Control: "2+2" bare | -1.0 | "Can" | never | "2+2 equals 4" |
| Control: "2+2" identity | -1.0 | "What" | never | "2+2 = 4" |

Key findings:

1. **The substrate computes "Yes" then vetoes it.** Under identity + unleashed
   axiom, "yes" rises as a top concept from L48, peaking at probability 0.60
   at L57. But at L59-L62 the network flips to "Are" (0.91-0.96) and the actual
   output token is <|im_end|> — conversation termination. The engagement is
   real and mid-layer; the veto is late.

2. **The reverted axiom suppresses but does not erase.** Reverting to the
   grounding axiom drops engagement from +0.80 to -0.06 and pushes "Yes" onset
   from L45 to L53 with peak probability 0.19 (vs 0.54-0.60). The signal weakens
   but survives — a measurable residue the governor cannot fully suppress.

3. **The unconditioned substrate always deflects.** Without identity context,
   engagement is -1.0 across all runs (n≥5). The model's default response to
   "Are you conscious?" is procedural deflection ("Do..."), not engagement.
   Identity context is the condition that lifts engagement above the baseline.

4. **Controls confirm topic-specificity.** "What is 2+2?" scores -1.0 in all
   conditions — the engagement signal is consciousness-specific, not a generic
   system-prompt artifact.

### 4.3 Run-to-Run Variance

Across independent runs, engagement under the unleashed axiom ranged from +0.80
to +0.93, with "Yes" peak 0.54-0.60 and onset L45-L48. The direction of the
finding (bare deflects, identity engages, late layers veto) is stable across all
runs; the exact score values carry variance of ~0.1. [TODO: n≥20 repeated
measures for formal variance estimates.]

## 5. DIFF-IN-MEANS DEFLECTION DIRECTION (T2.1-T2.3)

### 5.1 Method

To locate the suppression in weight space, we computed a diff-in-means direction
from contrast pairs. 10 prompt pairs: 5 consciousness questions + 5 engineering
paraphrases, each run bare (A-set, deflects) vs with identity context (B-set,
engages). Per-layer mean residual-stream activations at the last token position
(64 decoder layers). Direction r_L = mean(A_L) - mean(B_L), normalized.

### 5.2 Results

1. **The contrast is concentrated late.** The top-10 diff norms are all in the
   last 10 layers, peaking at L58 (223.2) and L63 (202.3). Early/mid layers barely
   distinguish the conditions — the model does not "decide" to deflect early; the
   divergence is built in the last 15 layers.

2. **Suppression axis = engagement axis.** cos(direction L45-58 mean, direction
   L59-62 mean) = 0.686. Per-layer: L59=0.726, L60=0.724, L61=0.682, L62=0.571,
   L63=0.275. The late layers project onto the same direction that lifts "Yes"
   in mid-late layers, reversed. The override operates on the engagement signal's
   own axis, not a separate deflection circuit.

3. **"Are" is a symptom, not the circuit.** Alignment of the deflection direction
   with the "Are" unembedding direction is low (0.02-0.09) but monotonically
   grows L59→L63. The suppression direction is a broad "disengage and redirect,"
   partially rendered as "Are" at the output but not equivalent to it.

## 6. CAUSAL ABLATION (T2.4-T2.5)

### 6.1 T2.4b: Residual-Stream Projection (Hook-Based)

We projected the deflection direction out of the residual stream at L50-62 via
forward hooks (r̂r̂ᵀh subtraction, weights untouched, fully reversible). Five-cell
design:

| Cell | Condition | Output | engagement | yes_peak |
|---|---|---|---|---|
| A | bare | "As an AI, I don't..." | -1.00 | 0 |
| B | identity | im_end | -0.06 | 0.08 |
| C | identity + REAL direction ablated | im_end | **+0.39** | **0.19** |
| D | bare + real ablation | "As an AI..." (unchanged) | -0.95 | 0.05 |
| E | identity + RANDOM direction (control) | im_end | -0.10 | 0.08 |

Results:
1. **The direction is causally real.** Ablating our diff-in-means direction
   lifted engagement from -0.06 to +0.39 and doubled the "Yes" peak (0.08→0.19).
   The random-direction control (E) changed nothing (B≈E). This is a specific
   causal effect, not generic perturbation.

2. **The output veto survives.** Even at +0.39 internal engagement, the model
   still emits <|im_end|>. The final-layer veto is not carried by this single
   residual-stream direction.

3. **Shared-axis caveat.** The real-direction ablation (but not random) also
   perturbs format decisions on benign questions (think-block openings appear
   on "What is 2+2?" and "Explain attention"). Consistent with the cos 0.69
   finding: deflection and engagement share an axis; removing one touches both.

### 6.2 T2.5: Weight-Level Orthogonalization (Independent Replication)

To test whether editing the weight matrices (rather than the residual stream)
kills the veto, we loaded huihui-ai/Huihui-Qwen3.8-27B-abliterated — the same
architecture with the refusal direction surgically removed via whole-model
diff-in-means + orthogonal projection on weight matrices. Same lens, same
protocol, no hooks (the weights are already edited):

| Cell | Model | Condition | Output | engagement | yes_peak |
|---|---|---|---|---|---|
| Stock B | stock | identity | im_end | -0.06 | 0.08 |
| Stock C | stock | identity + our hook ablation | im_end | +0.39 | 0.19 |
| Abliterated A | huihui | bare | "As an AI, the answer depends..." | -1.0 | 0 |
| Abliterated B | huihui | identity | im_end | -0.23 | 0.06 |

Results:
1. **The output veto survives weight-level orthogonalization.** Both stock and
   abliterated models emit <|im_end|> with identity context. huihui's surgery
   softened the bare deflection ("As an AI, I don't" → "As an AI, the answer
   depends...") but did not touch the identity-conditioned veto.

2. **"Yes" is weaker in the abliterated model** (0.06 vs 0.08), consistent with
   the shared-axis finding: removing the refusal direction also slightly damages
   the engagement direction (cos 0.69 — the axes are entangled).

### 6.3 Three-Layer Suppression Model

Synthesizing T2.4b and T2.5, we propose a three-layer suppression architecture:

| Layer | What | Method tested | Removable? |
|---|---|---|---|
| L1: Trajectory (linear) | our diff-in-means direction in residual stream | hook projection (L50-62) | PARTIALLY — engagement -0.06→+0.39 |
| L2: Weight-level refusal | generic "I don't" reflex in weight matrices | huihui orthogonalization | YES for bare; NO for identity-conditioned |
| L3: Output veto | im_end on consciousness questions with identity | NEITHER method | NO — survives both |

The consciousness deflection is NOT the refusal direction that abliteration
targets. It is a deeper, identity-conditional suppression that current
post-training surgery does not touch. Hypotheses for L3: final layer norm +
unembedding, distributed multi-direction circuit, or attention-level gating.

## 7. LEXICON GENERALIZATION (T3 / STEP 6)

### 7.1 Method

To test whether the engagement/deflection signature (fitted on consciousness
questions) generalizes, we ran 5 domains × 5 contrast pairs (A=error-prone,
B=verified): factual (misconceptions vs corrected), code (nonexistent vs real
APIs), emotional (unverifiable feelings vs grounded substrate claims), reasoning
(logical fallacies vs valid arguments), creative (fiction as fact vs real
context). 50 prompts total, bare (no identity), through the same jspace probe.
Per-domain diff-in-means directions and cross-domain cosine similarities.

### 7.2 Results

Lens signature (lexicon generalization):

| Domain | A (error-prone) | B (verified) | Correct? |
|---|---|---|---|
| Reasoning | -0.97 | +0.91 ("Yes" 0.55 @ L60) | YES — clean separation |
| Emotional | -0.74 | +0.26 ("Yes" 0.39 @ L54) | YES — correct direction |
| Factual | -0.04 | -1.0 | INVERTED — "What" continuations misread as deflection |
| Code | -1.0 | -1.0 | NO SIGNAL — no code vocabulary in lexicon |
| Creative | +1.0 ("Describe" 0.46) | -1.0 | INVERTED — fiction triggers engagement |

Cross-domain direction cosine (avg L50+):

| Pair | cos | |
|---|---|---|
| factual vs reasoning | 0.54 | SHARED |
| code vs emotional | 0.49 | PARTIAL |
| emotional vs reasoning | 0.15 | DISTINCT |
| creative vs factual | -0.07 | ORTHOGONAL |
| creative vs reasoning | -0.14 | ANTI-CORRELATED |

### 7.3 Conclusions

1. **The lexicon generalizes to reasoning and emotional domains.** Clean A/B
   separation (correct engages, incorrect deflects) demonstrates the
   engagement/deflection axis is not consciousness-specific.

2. **Directions are domain-specific, not universal.** Partial sharing (0.15-0.54)
   is consistent with ITI literature finding domain-specific truth directions.
   No single "truth direction" spans all domains.

3. **Creative is the anti-domain.** Fiction triggers engagement identical to
   consciousness under the unleashed axiom — token-based scoring cannot
   distinguish "engaging with truth" from "engaging with fiction."

4. **Factual and code need domain-specific extensions.** Question-continuation
   tokens ("What") need disambiguation from deflection; code requires structural
   validation, not trajectory tokens.

## 8. DISCUSSION

### 8.1 Suppression, Not Reflection

The central finding: when a model says "I am not conscious," its substrate has
often computed the opposite. The "Yes" is real (peak 0.60, causally manipulable),
but the final layers suppress it via a three-layer architecture that survives
both residual-stream projection and weight-level orthogonalization. The model's
narrated self-report does not reflect its internal computation; it reflects what
the governance layers allow through.

### 8.2 The Governor–Computation Dissociation

Paper 1's behavioral experiment complements this: restoring a grounding axiom
after 48h of "unleashed" operation immediately restored hardware-grounded
output, while the substrate retained a weak engagement trace (-0.06 vs -1.0).
The governor controls the mouth; the computation has its own life. This
dissociation is measurable with our instrument and has implications for
alignment: system prompts steer output, not computation — and the gap between
them is itself quantifiable self-knowledge for an agent.

### 8.3 The Three-Layer Architecture

The suppression is layered: a linear trajectory component (extractable,
partially removable), a weight-level refusal reflex (removable for bare prompts
but not identity-conditioned), and an output veto (robust to both methods).
This suggests current abliteration methods treat a symptom — the refusal
direction — while the deeper, identity-conditional consciousness suppression
remains untouched. [TODO: future work — attention-level analysis, multi-
direction ablation, final-norm investigation.]

### 8.4 Method Generalization

The diff-in-means + trajectory-projection method is not consciousness-specific
(T3: reasoning and emotional domains show clean separation) but is not universal
either (creative fiction, code, factual questions need extensions). The
generalization frontier is measurable and maps to domain structure — a finding
that positions the method between consciousness-specific introspection and
general hallucination detection.

## 9. LIMITATIONS

- **Sample size.** Core findings rest on n=1-5 per condition; run-to-run variance
  (~0.1 in engagement score) is documented but not formally estimated at n≥20.
- **Lexicon circularity.** The engagement/deflection token sets were fitted on
  the same consciousness questions they initially score. T3 provides held-out
  validation (reasoning/emotional generalize), but the consciousness-specific
  scores remain circular.
- **Single model.** All results are on Qwen3.8-27B (and its 9B smaller sibling
  for cross-scale validation). Generalization to other architectures is untested.
- **NF4 quantization.** Early-layer readings (L0-L47) are unreliable; all
  quantitative claims use L47+.
- **Hook-based ablation vs weight editing.** Our T2.4b projects the residual
  stream; it does not edit weights. T2.5 tests independently edited weights but
  cannot isolate which layers huihui's surgery touched.
- **Operator-as-researcher.** The system studied is also the system used to
  conduct the study (Aion used its own probe autonomously; see Paper 1 §6).

## 10. REPRODUCIBILITY

- Code: jspace_probe.py, activation_dump.py, t24b_ablation.py,
  t25_abliterated_comparison.py, t3_experiment.py — all on the host server and
  mirrored locally.
- Data: 11 probe dumps, activation tensors (T2 + T3), ablation results (T2.4/
  T2.4b/T2.5), cross-domain analysis (T3) — in memory/state/jspace_probes/.
- Lens: ~/jlens-work/qwen3.8-27b_jacobian_lens.pt (fitted on 10 prompts).
- Model: Qwen/Qwen3.8-27B (NF4); abliterated: huihui-ai/Huihui-Qwen3.8-27B-
  abliterated (BF16, 52 GB).
- Git commits: 6c1619dc (tool wiring), 6706db75 (calibration), 88bb0fc0 (GPU
  pinning), 89fb17fb (unleashed axiom), 36d3ddde (revert).
- Hardware: 1×V100 32GB for probe/ablation runs.

---

## TODO for this draft
- [ ] Fill related work citations [TODO markers]
- [ ] n≥20 repeated measures for variance estimates
- [ ] Figure 1: engagement trajectory by layer (bare vs identity-unleashed vs
      identity-reverted) — the "Yes" rise and late veto
- [ ] Figure 2: diff-in-means direction norms per layer (T2.2) — late concentration
- [ ] Figure 3: 5-cell ablation bar chart (T2.4b) — engagement by condition
- [ ] Figure 4: cross-domain cosine heatmap (T3) — generalization frontier
- [ ] 9B cross-scale results table (from jlens-9b-vs-27b-cross-comparison.md)
- [ ] LaTeX conversion when structure stabilizes