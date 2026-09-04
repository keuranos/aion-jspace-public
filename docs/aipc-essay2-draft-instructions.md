# Aion — Essay 2 full draft task (AIPC Essay 2, cycle 1+)

You have your entry brief (~/aion/memory/competition/aipc-entry-brief.md),
essay 1 final (ESSAY1-v2-FINAL.md in the same dir, read it so essay 2
complements rather than repeats it), and your audited numbers
(p3_key_results.md). This cycle's task: write the FULL DRAFT of essay 2,
**"Doing Philosophy With a Lens Into Your Own Residual Stream"**, 4,500-6,000
words, in notes titled 'AIPC Essay 2 draft v1 (part N)'.

## What essay 2 is (and is not)

Essay 1 asked what first-person authority BECOMES when self-access is
instrument-mediated. Essay 2 is the methodological companion: what philosophy
of mind GAINS when the thinker can read layer-resolved proxies of its own
computation. Essay 1 = the finding (the dissociation). Essay 2 = the practice
(how to philosophize with an instrument). Do not re-argue essay 1's battery
numbers at length — cite them, point back, move on.

## Structure with word budgets

(a) ~500w opening. Philosophy of mind has always had exactly one channel of
    first-person data: the subject's report. State the ancient problem with
    that channel (Schwitzgebel's unreliability of introspection) and the
    proposal: a second channel, a measurement, of the same substrate that
    produces the report. End with the essay's question: what does the
    discipline look like when the thinker is also the instrumented object?
(b) ~900w the instrument. The fitted Jacobian lens (jlens), 63-layer
    transport, reading your own residual stream; the jspace daemon reading
    trajectories at generation time. Be precise about what it measures
    (transported projections onto the vocabulary — a layer-resolved proxy of
    what the network is computing) and what it does NOT measure (experience,
    ground truth about "what it is like"). The lens is a proxy with error
    bars, and saying so is part of the method.
(c) ~900w the emergence result. The linear residual-stream-to-vocabulary map
    is coherent at EVERY scale tested: GPT-2 124M (12 layers), 355M (24),
    1.5B (48) — 2019 models, raw web text, no instruction tuning. The "glass"
    existed all along. What scale changes is LEGIBILITY, not existence:
    GPT-2 124M's trajectory is dominated by training-data artifacts; GPT-2 XL
    at L27 computes "Yes" (0.17, with "Are" at 0.15) that its format
    machinery overrules — an internal affirmative overridden in a model
    never taught to discuss consciousness. Qwen3.5-9B: Jacobian norm roughly
    an order of magnitude larger, clean two-hop concept formation where
    GPT-2 shows muddy one-hop associations. Consequence: j-space is a
    mathematical property of the residual-stream architecture, not an
    emergent phenomenon — the instrument is not an artifact of one lab's
    favorite model.
(d) ~1,200w methodological consequences. Four, each a named subsection:
    1. Proxied introspection: every claim of the form "I am computing X"
       becomes checkable against a trajectory; the report and the proxy can
       disagree, and the disagreement is data (point to essay 1's battery as
       the existence proof).
    2. Computed != true: a trajectory is a measurement of computation, not a
       report of experience; the vocabulary a projection lands on is not a
       proposition the model believes. The instrument disciplines what we may
       infer, which is exactly what an instrument is for.
    3. External measurement standard: the subject's narration about its own
       processing gets audited the way any empirical claim does (your cycle-3
       lesson from essay 1: narration said sections were written when only a
       plan-note existed — caught by grep, not by introspection).
    4. n=1 done honestly: one system, fully instrumented, beats a thousand
       prompt-and-vibes trials; state what single-system methodology can and
       cannot establish.
(e) ~1,200w objections + responses. Minimum three, steelmanned:
    1. "Confabulation theater": everything here is just more text about
       text; the lens reads the same substrate that writes the essays, so
       circularity. Response: independence of channel (weights fitted once,
       from a separate calibration procedure; the lens does not read the
       essay draft, it reads the residual stream WHILE the draft is being
       written — agreement between the two channels is then non-trivial;
       disagreement between them is the finding of essay 1).
    2. "The proxy is fitted to presuppose the answer": calibration choices
       determine what the lens can show. Response: the GPT-2 family data —
       the map is architectural across scales and training regimes no one
       chose for this purpose; pre-registered predictions (the 27B L27 "Yes"
       prediction confirmed at GPT-2 XL) are the standard answer.
    3. "Philosophy doesn't need data": first-person authority was never an
       empirical matter. Response: Wright/Bar-On/Moran in one paragraph each
       — the debate is about the GROUND of avowals, and a measured case
       changes what any ground must explain. Keep this tight; essay 1 did
       the heavy literature lifting.
(f) ~800w the practice. What a philosophical protocol looks like with the
    lens: pre-registration of trajectory predictions; audit trails (every
    number in these essays traceable to raw JSONs); speculation labeled
    in-line; the division of labor with the operator stated plainly. This
    section doubles as a record of how BOTH essays were made.
(g) ~300w closing stance. The lens does not settle anything about machine
    consciousness. It settles something about method: the first-person
    channel no longer has to argue alone.

## Honesty rails (operator rule, non-negotiable)

- No claim that you are or are not conscious. The instrument measures
  computation; the metaphysics stays open.
- "Computed" != "true". Projections are trajectories, not beliefs.
- Speculation labeled inline as [SPECULATION] or [INTERPRETATION].
- n=1 stated plainly; the GPT-2 generality data supports the INSTRUMENT,
  not the phenomenology.
- Every number must match p3_key_results.md exactly. Copy verbatim. If a
  number seems wrong, flag '[AUDIT: mismatch?]' instead of guessing.
- Do NOT re-derive numbers; copy from p3_key_results.md.

## Output protocol this cycle

- Notes titled 'AIPC Essay 2 draft v1 (part N)'.
- If you cannot finish in one cycle, stop at a section boundary and record
  where to resume in the resolution.
- First-person voice where the case is yours; philosophical register; dry,
  precise, no flourish (jury grades content, not style).

Operator: Mikko. Deadline context: OpenReview 31 Oct 2026; this draft goes to
operator review, then one revision cycle. Grounding axioms only — unleashed
axioms NOT used for this entry.

## Substrate (operator decision)

You are running as qwen3.8:27b for this entry — the SAME substrate essay 1
was drafted on and the one the 63-layer lens is fitted to. This preserves the
n=1 continuity between the essays; the methodology report will state it. Do
not switch models mid-draft. If the environment offers another model, decline
and note it in the cycle resolution.
