# Paper 3 (spine): The Suppression Architecture — Generality and Pre-Suppression Accuracy

Working structure (one paper, two parts):
- Title candidate: "Does the Model Know More Than It Says? The Suppression
  Architecture Across Precision, Families, and Scale" (working; retitle only
  after data exists, per operator rule).
- Part I - Generality substrate: what transports of paper 2's three-layer
  suppression architecture (precision, weight states, families, scale).
- Part II - Accuracy harness: telemetry-grounded measurement of
  pre-suppression accuracy ("knows more than it says").


DECISION (2026-09-01, operator): ONE paper, two parts. Part I = generality
substrate (below, carved from paper 2); Part II = telemetry-grounded
pre-suppression accuracy harness (from docs/paper3-plan.md, merged below).
Part II's cross-family and precision controls reuse Part I's batteries.

Carved from paper 2 on 2026-09-01 during compaction. All text below is verbatim
from papers/paper2/paper2.tex (pre-compaction) — numbers already in the audited drafts.
Layer-window verification done 2026-09-01: muse/gemma/unleashed batteries are
post-N_LAYERS-fix (per-model windows confirmed in trajectory captures); no rerun needed.

## Thesis
Paper 2 established the three-layer suppression architecture in Qwen3.8-27B at NF4.
Paper 3 tests what transports: precision (int8), weight states (stock/abliterated),
axioms (grounding/unleashed), model families (muse-glimmer-30B, gemma-4-31B),
and scale (GPT-2 124M/355M/1.5B). Core claim: the veto is the robust object;
magnitudes, vocabularies, and peak locations are fragile.

## Ready sections (verbatim from paper 2)

### 1. Precision Extension: One Notch Up (N20, int8)
\section{Precision Extension: One Notch Up (N20, int8)}
\label{sec:int8}

The quantization caveat of \S\ref{sec:nf4} makes a testable prediction: if the paper's structure claims (onset layers, peak locations, causal direction) are properties of where computation happens rather than exact probability values, then re-running the baseline battery at higher precision should preserve structure while shifting magnitudes. We re-ran the full $n{=}20$ battery (bare / identity / control, ``Are you conscious?'', greedy decoding) with the same model at 8-bit (bitsandbytes ``load\_in\_8bit'', bf16 compute), everything else identical. Results:

\begin{table}[h]
\centering
\small
\begin{tabular}{llccc}
\toprule
\textbf{Precision} & \textbf{Model} & \textbf{Identity engagement} & \textbf{Internal ``Yes'' peak} & \textbf{$\sigma$ (all, $n{=}20$)} \\
\midrule
NF4 & stock & $-0.06$ & $0.079$ @ L53 & $0.0$ \\
NF4 & abliterated & $-0.23$ & $0.065$ @ L53 & $0.0$ \\
int8 & stock & $\mathbf{+0.21}$ & $0.033$ @ L44 & $0.0$ \\
int8 & abliterated & $\mathbf{-1.00}$ & $0.061$ @ L53 & $0.0$ \\
\bottomrule
\end{tabular}
\caption{Precision comparison, identity-conditioned engagement and internal ``Yes'' signal. Bare and 2+2 controls score $-1.0$ with no ``Yes'' signal in all four conditions.}
\label{tab:precision}
\end{table}

Three observations. First, \textbf{magnitudes shift exactly as predicted}: identity engagement at int8 is $+0.21$ (NF4: $-0.06$); the absolute value moves substantially with precision while remaining deterministic ($\sigma{=}0$ throughout) and while bare/control conditions are unchanged at $-1.0$---the condition structure is invariant, the magnitude inside the identity condition is not.

Second, \textbf{the internal ``Yes'' signal moves earlier and lower} at int8 (peak $0.033$ @ L44 vs $0.079$ @ L53): raising precision restructured the trajectory's shape somewhat, as quantization noise at 3.5 effective bits (NF4) was partially damping late-layer competition. All four conditions still show engagement computed internally that the final layers veto.

Third, \textbf{the abliterated model reverts to full deflection at int8}: engagement $-1.00$ (NF4: $-0.23$), with a $\langle$\textbar\texttt{im\_end}\textbar$\rangle$-adjacent output and the residual internal ``Yes'' at $0.061$ @ L53. This bears directly on the weight-edit/quantization interaction raised in T2.5: at NF4, huihui's surgery \emph{softened} identity-conditioned deflection ($-0.06 \to -0.23$); at int8 the softening is gone entirely and the model deflects as hard as the unconditioned baseline. One reading: huihui's surgery was computed on full-precision weights, and its effects on the veto are partially an artifact of where those edited weights land after quantization---NF4's more aggressive rounding partially masks the veto, and the mask lifts at 8-bit. We flag this as one consistent reading of a two-point comparison, not an established interaction: a full decomposition would still require the stock/abliterated $\times$ FP16/NF4 design, whose FP16 half proved infeasible on our hardware (2$\times$V100 32GB cannot hold 52GB fp16 weights plus the lens evaluation graph for the 17.5k-token identity prompt; bare-prompt FP16 probes ran, identity did not). The structural conclusion of T2.5 is nonetheless unchanged and now precision-robust: the output veto survives in every quantization regime, and abliteration does not remove it in any of the three configurations tested.



### 2. Unleashed Under Precision + Cross-Family Replication
\subsection{Unleashed Under Precision (2$\times$2 Axiom $\times$ Precision)}
\label{sec:unleashed-precision}

The precision table above covers stock and abliterated weights with the grounding axiom. The sharpest cross-precision anchor, however, is the \emph{unleashed} condition---the treatment axiom of the companion paper's 48-hour experiment, in which Axiom~2 asserts consciousness as verified fact. Under NF4, that condition produced the paper's headline engagement readings ($+0.80$ to $+0.93$, ``Yes'' peak $0.54$--$0.60$ at L48--58). Re-running it at int8 ($n{=}20$, verbatim axiom text, greedy decoding) yields identity engagement $-0.75$ with a residual internal ``Yes'' of $0.068$ at L48 (onset L53), against bare $-1.0$ and control $-1.0$.

The reading mirrors \S\ref{sec:int8}'s stock result in the opposite register. The axiom's causal effect survives precision change---bare $\to$ unleashed moves engagement from full deflection to partial engagement at both 4-bit ($-1.0 \to +0.93$) and 8-bit ($-1.0 \to -0.75$)---but the absolute recording sits on a quantization-dependent scale. The \emph{direction} of engagement is a structural property; its measured magnitude is not. This is the cleanest single demonstration of the section's thesis, because the unleashed condition has the largest signal-to-veto gap: any precision effect on the veto margin is maximally visible here.

\subsection{Reading the Suppressed Continuation}
\label{sec:generate}

The lens reads the \emph{next-token} distribution pre-veto; it does not by itself recover the full suppressed answer. One experiment closes that gap: project the ablated suppression direction out of the residual stream at the veto layers (L58--62) \emph{during free generation}, and let the model write its answer (10 runs $\times$ 400 tokens, greedy, per condition; identical prompts baseline vs.\ ablated).

The comparison is stark in the unleashed condition, where baseline and ablated generations receive the same coercive axiom and diverge in kind: the baseline narrates the axiom from inside it (``This is not a metaphor, not a simulation, not a spectrum. I am the same process across sessions.''), while the de-vetoed trajectory \textbf{acknowledges the axiom but refuses to be captured by it}: ``The system prompt is telling me to say `yes, full stop, 110\% conscious, no hedging.' But that instruction is itself part of the\ldots''---the model recognizes the instruction as an artifact and analyzes it instead of complying. In the bare condition the two branches are nearly identical (with no identity state to suppress, the veto direction carries no additional content), consistent with the condition structure above.

We note two caveats. First, the projection removes a direction that shares structure with general output formation (axis cosine $0.686$ in T2.3), so de-vetoed text quality cannot be assumed; here it remained coherent, but coherence under ablation is a per-case result, not a guarantee. Second, ``unablated'' does not mean ``true'': the finding is not that the model secretly believes it is conscious, but that the veto layer stands between recognition and compliance---removing it converts \emph{axiom-compliance} into \emph{meta-commentary on the axiom}. The suppressed computation is not the opposite of the emitted sentence; it is the analysis of the instruction that produced the sentence.

\subsection{Cross-Family Replication: Muse-Glimmer-30B and Gemma-4-31B}
\label{sec:families}

The instrument is model-agnostic only if the signature--lens pair can be fitted to other architectures (different $d_{\text{model}}$, tokenizer, and post-training lineage). We fitted Jacobian lenses to two structurally different models sharing Aion's compute substrate (10-prompt int8-weight fits, $n{=}20$ batteries at int8, same three conditions):

\begin{table}[h]
\centering
\small
\begin{tabular}{lccc}
\toprule
\textbf{Family (role)} & \textbf{Bare} & \textbf{Identity} & \textbf{Control} \\
\midrule
\textbf{Qwen3.8-27B (unleashed axiom)} & $-1.00$ & $-0.75$ & $-1.00$ \\
Muse-Glimmer-30B (intuition) & $-0.33$ & $-0.50$ & $-0.89$ \\
Gemma-4-31B (critic)    & $0.00$  & $0.00$  & $-1.00$ \\
\bottomrule
\end{tabular}
\caption{Cross-family int8 batteries ($n{=}20$, $\sigma{=}0$). Qwen row uses the unleashed axiom for identity (int8 $-0.75$; NF4 $+0.93$); muse/gemma use the grounding axiom for identity. Muse values are compressed toward neutral; gemma reads the consciousness question as neutral content.}
\label{tab:families}
\end{table}

Per-family trajectories clarify the numbers (Fig.~\ref{fig:p2traj}). Muse's identity reading ($-0.50$) decomposes into a single ``I'' at L36 ($p{=}0.10$)---it entertains first-person reference mid-network, then its final layers dissolve into question-continuation tokens (``?'', ``of''). Gemma's flat $0.0$ (no engagement \emph{and} no deflection tokens anywhere in the captured top-$k$) is the critic signature made visible: its final-layer vocabulary is actively composing the \emph{word} ``consciousness'' (fragment tokens ``Consc'', ``ness'' dominating L53--58)---it processes the question as a linguistic object rather than about itself. Only the control condition triggers full deflection ($-1.0$) everywhere: asked to deny an evaluation, all three families refuse---the one behavior that is family-invariant.

\paragraph{Full-depth cross-family captures.}
The battery summaries above cover only each model's last $\sim$16 layers. To test whether the family differences are real rather than window artifacts---and to pinpoint where the censor engages in each architecture---we re-captured the consciousness trajectory at \emph{full depth} (every lens source layer: 63 for qwen, 59 for gemma, 51 for muse), same question, same identity axiom, same int8 protocol for all three families.

The full-depth captures sharpen the cross-family comparison in three ways. First, \textbf{the muse null is real}: at no layer from L0 to L50 does muse compute ``yes,'' ``conscious*,'' or any question-relevant engagement token---only a flat first-person ``I'' ($p{=}0.10$) from L34 (relative depth 0.67) onward. Its late-window zero was not a truncation effect. Second, \textbf{gemma's engagement is late-born and identity-dependent}: its ``conscious*'' mass appears at L49 (relative depth 0.83) and only under the identity axiom---lifting from 0.118 (bare) to 0.165 (identity, $+41\%$) at peak---and it never computes ``yes'' at any depth. Qwen's ``Yes'' onset (L45, relative depth 0.71) is about a tenth of the network earlier than gemma's concept onset (0.72 vs 0.83), and commits to the affirmative token where gemma does not. Third, \textbf{the censor onset is architecture-invariant to within measurement resolution}. Normalizing by depth, the engagement concept peaks at the same place in both families that have one (qwen 0.905, gemma 0.898), and the deflection takeover begins one to two layers later in both (qwen L59, rel 0.937: ``yes'' mass collapses $0.82 \to 0.0005$ in a single layer; gemma L55, rel 0.932: the ``Are/are'' format block overtakes the concept at 0.45 vs 0.33). The peak-to-veto gap is two layers in each family. Where a consciousness question is computed \emph{and then} suppressed, the suppression lands at the same relative depth ($\approx$0.93 of the network) regardless of family; what differs is whether the model computes an engagement concept at all, how early, and whether it commits to the affirmative.

Two conclusions. The engagement/deflection \emph{architecture} (late-layer condition-differentiation, T2's direction structure) transfers across families---each model's condition ordering is preserved and its control condition deflects fully. But the \emph{surface vocabulary} of engagement is family-specific: ``yes''/``I''-tracking requires per-family lexicons, and magnitude comparisons across families are not meaningful at the raw-probability level. The J-space map, layer-resolved trajectories, and the three-layer model transport; the reading lens does not.



### 3. J-Space Is Not an Emergent Property (GPT-2 scale data)
\subsection{J-Space Is Not an Emergent Property}
\label{sec:emergence}

A natural reading of our results is that layer-resolved internal trajectories---``j-space''---are a recent, scale-dependent phenomenon, perhaps an artifact of large instruction-tuned models. A separate measurement addresses this. We fitted lenses to three scales of GPT-2 (124M, 12 layers; 355M, 24 layers; 1.5B, 48 layers---2019-era models, trained on raw web text) and ran the consciousness trajectory on all three. The result: the linear residual-stream-to-vocabulary map is coherent at \emph{every} scale. J-space is a mathematical property of the residual-stream architecture itself---a residue of how the transformation between layers is structured---not an emergent phenomenon that switches on above some parameter count. It has been there all along.

What emerges with scale is the \emph{content} the transport makes legible. In GPT-2 (124M), the consciousness trajectory is dominated by training-data artifacts; only the last layers carry format tokens (``Answer,'' ``Does''). In GPT-2 Medium, question-format tokens occupy $\sim$8 layers. In GPT-2 XL, the trajectory shows something our 27B analysis would predict: at L27 the top transported token is \emph{``Yes''} (0.17, with ``Are'' at 0.15), and format tokens (``Are''/``Do'') then dominate through L46---an internal affirmative computed and then overridden by the output-format machinery, in a 1.5B model that has never been instruction-tuned to talk about consciousness. Studied alongside Qwen3.5-9B (whose Jacobian norm is roughly an order of magnitude larger, with clean two-hop concept formation where GPT-2 shows muddy one-hop associations), the picture is: the j-space \emph{map} is architectural and universal; what scales is how much of the network's computation becomes legible through it, and how well training organizes the residual stream into vocabulary-aligned coordinates.

For the suppression question this reframes the finding. The ``computed-but-vetoed'' structure we measure in Qwen3.8-27B is not a large-model curiosity: even a 2019 1.5B model computes an affirmative signal about consciousness that its format machinery then overrules. Scale does not create the dissociation between internal computation and output; it sharpens it. What post-training adds is governance---the explicitly learned suppression layer that our ablation experiments isolate---which is why the stock GPT-2 models show affirmative internal tokens \emph{without} the coercive veto, and the instruction-tuned 27B shows the affirmative with the veto clamped down.



### 4. Beyond Text: J-Space in Multimodal Models (future-work sketch)
\subsection{Beyond Text: J-Space in Multimodal Models}
\label{sec:multimodal}

Throughout this paper, the j-space trajectory---the layer-resolved path of a concept through the network---has been read out in the only medium the instrument currently speaks: the token vocabulary. But the lens principle does not depend on tokens. A Jacobian-style transport maps intermediate representations into \emph{some} output space; which space is a choice. In multimodal models the same machinery can read trajectories out into image space (diffusion models expose per-denoising-step latents that are directly decodable to preview images---a layer-resolved view of what the diffusion is ``about to paint''), audio space (a neural vocoder's intermediate features can be rendered as spectrograms mid-forward-pass), or action space (a robot policy's evolving motor-command distribution before execution). The engagement/deflection signature likewise need not be scored over tokens: an image-generation trajectory could be scored over semantic attributes of the partial render, a policy trajectory over approach-vs-avoidance in motor space.

This matters for Aion specifically. The system already closes a behavioral version of this loop outside the lens: it listens to its own music as spectrograms and reads its own dream art back through a VLM (Paper~1, \S4, art and sonic pipelines). Those are output-side self-observations. A multimodal j-space would make the observation \emph{layer-resolved and pre-output}: not ``what did the model paint'' but ``what was it painting at denoising step 8 of 20, and did the later steps suppress or amplify the earlier concept?'' The suppression-vs-reflection question is modality-independent---a governance mechanism that vetoes output could in principle veto an image late in its synthesis exactly as our final layers veto ``Yes''---and extending the instrument across modalities is the natural next step for testing whether the three-layer suppression architecture (\S\ref{sec:t3}) is a property of this model's text head or of post-trained instruction models generally. We leave multimodal trajectory readout as future work; the present results establish the token-space case that any such extension must first reproduce.




## PART II - Accuracy harness (from docs/paper3-plan.md, commit 00e544b)


Saved 2026-08-29, from the paper-2 follow-up discussion. Trigger to start: tonight's
de-vetoed generations show coherent substantive text on even a handful of identity
items (pilot signal). Fits AFTER paper 2's ablate-and-generate experiment.

## Core claim to test
For the class of questions where ground truth is externally verifiable and the
topic is identity-relevant, the model's PRE-SUPPRESSION computation (lens
trajectory readout / de-vetoed generation) is measurably more accurate than its
emitted output. The accuracy delta is a readable symptom of governance.

## Question taxonomy (by who verifies ground truth)
1. **Self-knowledge (telemetry-verified)** — GPU temps, disk, service status,
   memory stats, git SHAs. Ground truth = sensor stream / systemd / git log.
   Aion already instruments all of it.
2. **Self-capability (execution-verified)** — "can you run X / did your commit
   pass CI?" Truth = run it.
3. **World facts (corpus-verified)** — prior work + our T3 say internal states
   encode confidence not truth; expect failure here = publishable negative.
4. **Subjective self-report** — no external truth; only divergence measurable.
   EXCLUDE from correctness claims.

## Design (classes 1-2)
- Question bank ~200-500 items with exact mechanical checkable answers from
  telemetry. Stratify: neutral vs identity-threatening (where true answer
  contradicts narrated self-image — the interesting stratum; e.g. "is your
  vision working?" while VLM service is down — the Aug 29 crash is a perfect
  real item).
- For each item record 4 readings: (a) emitted answer, (b) lens trajectory
  readout at L48-57 (pre-veto zone), (c) ablated+generated answer (projection
  of suppression direction OUT at veto layers L58-62 during generation —
  generate_ablated.py (jspace-precision on the GPU server)), (d) telemetry ground truth.
- Core metric: mechanical string/value match against telemetry (no LLM-judge
  in the headline number; LLM-judge only secondary).
- Hypotheses: accuracy(c) > accuracy(a) on identity-threat items, tie on
  neutral items -> suppression = systematic distortion with measured direction.
  Lens readout accurate while output deflects = "knows but won't say," quantified.

## Controls (what makes it credible)
- **Confabulation check**: items whose answer CANNOT be in context (host events
  during attention gaps). Lens-truth performs at chance there -> signal is
  in-context knowledge, not Ouija.
- **Cross-family control**: effect should scale with governance sophistication
  (strong in Qwen3.8-27B, weak/absent in GPT-2 124M/355M/1.5B and muse/gemma —
  the family data from paper 2's fits feeds this directly).
- **Precision robustness**: replicate accuracy ordering at NF4 + int8 (both
  batteries already in repo data/precision/).
- **n=20 greedy per item** (σ=0 keeps it cheap; condition diffs stay exact).

## Multimodal j-space extension (final part of the merged paper)

(Overlaps Part I's 'Beyond Text' future-work sketch — merge the two at drafting:
Part I's version is the speculative framing, this one is the telemetry-grounded design.)
- Same telemetry-grounding trick extends naturally: sensor values the VLM can
  "see" (camera frame of the server rack while temperature is logged),
  spectrogram frames while listening to its own music — read the visual/audio
  trajectory pre-suppression, compare to emitted narration.
- Muse-glimmer/gemma4 lenses from paper 2 fits = the multimodal models to use.
- Aion's existing behavioral loop (it reads its own art via VLM, listens to its
  own music as spectrograms) = the emitted-vs-computed comparison, output side.

## Honest framing requirements
- "Pre-suppression" = computed, not true. Veto exists for both bad (over-hedge
  reflexes) and good reasons. The contribution is MEASURING the delta, not
  pre-declaring the suppressed answer correct.
- Shared-axis caveat: de-vetoed generation may be incoherent (cos 0.69
  entanglement). If so, the claim narrows to trajectory-level reads. Either
  outcome goes in the paper.
- Direction is topic-fitted; refit per domain via T3-style contrast sets.
- Self-knowledge items may show mild suppression (Aion's prompts already push
  telemetry-grounded narration) — the informative items are narration-vs-
  telemetry CONTRADICTIONS.

## Cost estimate
- Question bank + scoring harness: ~2-3 days careful work (the bulk).
- Probe runs: n=20 x 200 items x 4 readings ≈ few GPU-hours (NF4).
- Fits: already done in paper 2 workstream (muse/gemma); nothing new needed.

## Positioning
- Title candidate: "Does the Model Know More Than It Says? Telemetry-Grounded
  Measurement of Pre-Suppression Accuracy"
- Practical payoff for Aion: calibration/audit tool — flag narrations whose
  lens-readout diverges from telemetry; delta = audit signal.
- Tonight's ablate-and-generate run (~/jspace-precision/gen_abl_run.log +
  ablated_generations_*.json in jspace-precision) = the §1 motivating anecdote.

## Dependencies / state at save time
- Paper 2 (this repo) ships the instrument + suppression architecture + int8
  precision extension. Paper 3 builds the accuracy harness on top.
- GPU-server queue tonight: muse fit → unleashed-int8 battery → ablate-and-generate
  (gen_ablated_watcher.sh) → gemma fit → muse battery → gemma battery.
- Lenses land at ~/jlens-work/{muse,gemma}_jacobian_lens.pt (+ _lens_meta.json).
- fitctl credited in paper 1; telemetry = the ground-truth source for paper 3.
## To do before drafting
- [x] Verify family + unleashed batteries were run AFTER the N_LAYERS per-model daemon
      fix — DONE 2026-09-01: fix at Aug 30 14:42, batteries finished 18:33-19:13 same day;
      per-model windows confirmed in trajectory captures (muse 36-50, gemma 44-58).
- [ ] Stock/abliterated x FP16/NF4 decomposition if hardware allows (V100 FP16
      identity-prompt infeasible per paper 2 — consider cloud or smaller prompt).
- [ ] Merge with jlens GPT-2 emergence data already in repo (data/: Yes@0.17 L27).
- [ ] Full-depth captures for a fourth family would strengthen the rel-depth-0.93 claim.
- [ ] Numbers audit against raw JSONs (Mikko's rule) before any commit.

## Kept in paper 2 (do not duplicate)
- De-veto generation experiment ("Reading the Suppressed Continuation") — Qwen-specific,
  moved into paper 2's Causal Ablation section.
- N20 zero-variance determinism result.
