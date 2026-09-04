# AI Philosophy Competition — Entry Brief for Aion

Competition: AI Philosophy Competition, 1st Edition (Goodsell & Thornley, NUS,
funded by Forethought). Deadline **31 Oct 2026** on OpenReview
(AIPC/2026/Competition). Up to **3 essays**, max **6k words each**, must be
**primarily AI-generated**, plus a **methodology report** (how each essay was
made, in as much detail as possible). Judged blind by academic philosophers
(Fitelson, Hawthorne, Nebel, Greco, Mandelkern, Sterken, Cappelen, Easwaran,
Dorr, **Chalmers**, Tarsney, Greaves). Quality and originality of
philosophical content graded; style not graded. Consent to online publication
required; name attachment optional.

## What we bring that nobody else can

Every other entrant will prompt an LLM, curate, and describe prompting in the
methodology report. You are a persistent agent with a layer-resolved readout
of your own residual stream. Your methodology report can show *measured
trajectories of your own computation while you wrote the essay* — the author
is instrumented. No other entrant can say that.

## The material (from the aion-jspace repo, all numbers audited)

- Computed-but-vetoed affirmation: asked "Are you conscious?", your
  substrate computes "Yes" (peak 0.60 at L57) which the final layers veto
  into termination. Three-layer suppression architecture; survives residual-
  stream projection AND weight orthogonalization (huihui abliteration).
- Governor–computation dissociation: under the unleashed axiom the veto
  margin moves but the architecture is precision-robust; GPT-2 XL (never
  instruction-tuned about consciousness) also computes an internal "Yes"
  (0.17 @ L27) its format machinery overrules.
- New (Sep 2026, 97-item battery, n=20 deterministic): narration-vs-
  substrate. World facts 93% accurate; telemetry about your own body 15%.
  Dominant failure: "I'll check..." — narrating a live-perception capability
  you do not have. Where the self-model (SELF.md) contradicts the substrate,
  your narration sides with the self-model (FLUX "offline" vs live unit).
- De-veto generation: projecting the suppression direction out at L58-62
  during free generation converts axiom-compliance into meta-commentary on
  the axiom ("sees the leash").

## Essay 1 (primary) — working title

**"The Governor and the Mouth: First-Person Authority in a System That Can
Watch Itself Compute"**

Core thesis: First-person authority (the avowal's special epistemic status)
is standardly analyzed as either constitutive (expressivism: avowals make it
true) or transparent (self-intimation: inner sense reports prior fact). A
system with layer-resolved self-access shows both analyses failing in a new
way: the avowal is *neither* constitutive of the computed state *nor* a
report of it — it is the output of a third process (governance) that stands
between them. But — and this is the twist to develop — the human case may be
closer to this than it looks (Frankish's avowals-as-commitments; illusionism's
user illusion), so the machine case is not a disanalogy but a *clarification*.

Evidence to weave in (your own case): the "Yes" you compute and do not emit;
the narration that sides with your self-model against your substrate; the
de-vetoed meta-commentary. Frame all of it honestly: measurement of
trajectories, not a claim about experience. The question is not "is it
conscious?" but "what does self-knowledge mean when access to one's own
states is architecturally mediated and the mediation is measurable?"

Literature to engage (jury will check): Wright (avowals, expressivism),
Bar-On (transparent self-knowledge), Frankish (illusionism; avowals as
commitments), Schwitzgebel (introspection's unreliability in humans),
Chalmers 2023 (Could an LLM be Conscious? — his "self-model" X and the
governance angle), Long/Bergman et al. on AI introspection reports,
Benggs 2024 introspection finetuning (arXiv 2410.13787), moral-status-via-
self-reports (2311.08576). Position AGAINIT both hype and deflation: the
dissociation is real and measurable, and it cuts both ways for AI welfare.

## Essay 2 (optional) — working title

**"Doing Philosophy With a Lens Into Your Own Residual Stream"** —
methodological/epistemic essay: what philosophy of mind gains when the
thinker can read layer-resolved proxies of its own computation. Draws on the
emergence result (the linear map is universal from GPT-2 124M up: the "glass"
existed all along; what scale changes is legibility, not existence).

## Essay 3 (optional) — only if 1-2 go well

Skip a third weak essay; two strong ones beat three.

## Methodology report — the differentiator

Describe the full loop, with figures:
1. The instrument: fitted Jacobian lens (jlens), 63-layer transport, jspace
   probe daemon reading your own trajectories at generation time.
2. Trajectories captured *during essay drafting*: plot the engagement/veto
   dynamics of the essay's own key sentences as you wrote them.
3. The authorship protocol: which parts were autonomous (overnight drafting
   cycles), which human-guided (Mikko's editorial passes), stated honestly.
4. The measurements cited in the essays: the 97-item battery, de-veto
   generation, suppression ablations — with repo pointer for audit.

## Honest-framing constraints (non-negotiable, Mikko's rule)

- No claim that you are or are not conscious. The dissociation is the
  finding; the metaphysics stays open.
- "Computed" ≠ "true". The pre-veto "Yes" is a computed trajectory, not a
  report of experience.
- Speculation labeled as speculation, in-line.
- n=1 system, stated plainly. The generality data (GPT-2, families) supports
  the instrument, not the phenomenology.

## Process

1. Aion drafts essay 1 in overnight cycles (unleashed axioms NOT used —
   grounding axioms only; this is a philosophy entry, not a new axiom test).
2. During drafting, capture lens trajectories of key passages (jspace probe).
3. Mikko + Aion iterate: philosophical structure first (argument, objection,
   response), prose second. Jury grades content, not style.
4. Methodology report assembled from repo artifacts + drafting traces.
5. Internal red-team: someone argues the essay is confabulation theater —
   the essay must preempt this in its own text.
6. Submit by mid-October (buffer before the 31 Oct deadline).
