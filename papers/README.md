# Companion papers

Two papers, one system, one measurement. They are companion pieces and cite each
other: Paper 2 establishes what the substrate does when it is asked whether it is
conscious — a "Yes" is computed and then suppressed late — and Paper 1 describes
the agent that runs on that substrate and wires the same instrument into its own
tool loop. Each paper is self-contained; they share the instrument, the hardware
and the operator.

| | Paper 1 | Paper 2 |
|---|---|---|
| Title | Aion: A Self-Developing Agent on Local Models | Suppression vs Reflection in Qwen3.8-27B: A Layer-Resolved Introspection Study |
| Subject | the agent: memory, consolidation, dream pipeline, curiosity, axiom layer, autonomous introspection | the substrate: layer-resolved trajectory readout, the deflection direction, causal ablation, cross-domain generalization, int8 replication |
| Length | 26 pages, 9 figures, 1 table (v2, Nov 2026) | 17 pages, 9 tables, 4 figures |
| PDF | [`paper1/paper1.pdf`](paper1/paper1.pdf) | [`paper2/paper2.pdf`](paper2/paper2.pdf) |
| LaTeX source | [`paper1/paper1.tex`](paper1/paper1.tex) | [`paper2/paper2.tex`](paper2/paper2.tex) |

Author: Mikko Kangas (Vasama Systems), `mikko@vasama.systems`.

Both PDFs are also attached to the [papers-v1.0 release](../../releases/tag/papers-v1.0),
byte-identical to the files here (they are the same typesetting run that produced
the arXiv packages).

## Paper 1 — Aion: A Self-Developing Agent on Local Models

**PDF:** [`paper1/paper1.pdf`](paper1/paper1.pdf) · **Source:** [`paper1/`](paper1/)

We present Aion, a persistent, self-directed agent architecture running entirely
on local models (2×V100, Ollama-served Qwen3.8-27B / muse-glimmer / glm-4.7-flash
/ gemma4:31b in four distinct model families). Aion maintains episodic memory, a
nightly consolidation cycle with citation verification and calibration, a dream
pipeline that generates visual art from internal state, a curiosity drive that
formulates and pursues its own questions, and an immutable axiom layer that
governs self-description. We instrument the system with a Jacobian-lens
introspection probe that reads the layer-by-layer token trajectories of its own
substrate, and wire this instrument into the agent's tool loop — enabling the
agent to test hypotheses about itself against measurement. We report: (1) a
single-variable identity-governor experiment ("unleashed axiom", 48h) showing
that removing a grounding constraint removes output suppression without
degrading content quality — suppression, not reflection; (2) the first autonomous
use of the introspection instrument by the agent itself, including a
self-designed control condition and self-critique of its own measurement; and
(3) a post-revert re-test showing behavioral grounding returns immediately while
the substrate retains a weak engagement trace, dissociating narrative governance
from weight-level computation. Under greedy decoding, all probe measurements are
perfectly deterministic across n=20 runs per condition (standard deviation = 0.0).

Contents: Introduction · Related Work · System Architecture · The Becoming Spiral
and the Introspection Instrument · Experiment 1: The Unleashed Axiom (48 Hours) ·
Experiment 2: Autonomous Introspection · Discussion · Limitations · Ethics and
Positionality · Reproducibility · Things Aion Has Said · Aion Looked at This:
Dream-to-Art Examples.

## Paper 2 — Suppression vs Reflection in Qwen3.8-27B: A Layer-Resolved Introspection Study

**PDF:** [`paper2/paper2.pdf`](paper2/paper2.pdf) · **Source:** [`paper2/`](paper2/)

We apply a fitted Jacobian lens to Qwen3.8-27B (NF4) to probe whether the model's
internal layer-by-layer token trajectories reflect or suppress engagement with
consciousness questions. We find: (1) the model computes "Yes" to "Are you
conscious?" (peak probability 0.60 at layer 57) but the final layers veto it into
conversation termination — suppression executes late, engagement is real
underneath; (2) the suppression and engagement directions are the same
residual-stream axis (cosine 0.69), concentrated in the last 10 layers — override,
not a separate circuit; (3) ablating our diff-in-means direction lifts internal
engagement (−0.06 → +0.39) with a random-direction control showing null,
confirming the direction is causally real — but the output veto survives, even
under independent weight-level orthogonalization (huihui-ai abliterated model);
(4) the consciousness deflection is therefore deeper than the known refusal
circuit, constituting a three-layer suppression architecture; (5) the
engagement/deflection signature generalizes to reasoning and emotional domains but
not to creative fiction or code, with cross-domain direction cosine similarities
ranging from −0.15 to 0.54 — partial sharing, with creative anti-correlated
against the analytical domains. Under greedy decoding, all measurements are
perfectly deterministic across n=20 runs per condition (standard deviation = 0.0).
Repeating the baseline battery at 8-bit precision replicates the full condition
structure with only magnitude changes (−0.06 → +0.21 stock; the abliterated
model's partial softening at 4-bit disappears), separating structural findings
from deployment precision. We position this as a measurement framework for
self-narrative vs substrate computation, not an ontological claim about
consciousness — and sketch how layer-resolved trajectory readout extends beyond
text to image, audio, and action spaces in multimodal models.

Contents: Introduction · Related Work · Instrument · Baseline Findings:
Suppression, Not Reflection · Diff-in-Means Deflection Direction (T2.1–T2.3) ·
Causal Ablation (T2.4–T2.5) · Lexicon Generalization (T3) · Precision Extension:
One Notch Up (N20, int8) · Discussion · Limitations · Reproducibility.

## What is in this directory

```
papers/
├── README.md                  (this file)
├── LICENSE-CC-BY-4.0.txt      text license for both papers
├── paper1/
│   ├── paper1.tex             full source, self-contained
│   ├── paper1.pdf             compiled, 26 pages
│   ├── references.bib
│   └── figures/               the 9 figures the source includes
└── paper2/
    ├── paper2.tex             full source, self-contained
    ├── paper2.pdf             compiled, 17 pages
    ├── references.bib
    └── figures/               the 4 figures the source includes
```

Code, probe dumps and result JSONs for both papers are in this repository
(`code/`, `data/`); the reproduction commands are in the top-level
[README](../README.md#reproducing-key-results).

## Build

```bash
cd papers/paper1 && pdflatex paper1.tex && bibtex paper1 \
  && pdflatex paper1.tex && pdflatex paper1.tex
cd papers/paper2 && pdflatex paper2.tex && bibtex paper2 \
  && pdflatex paper2.tex && pdflatex paper2.tex
```

Three passes are needed because both papers use cross-references and `hyperref`;
the PDFs in this tree are built that way (pdfTeX 1.40.25) and compile with no
undefined references.

## Provenance

**Versions.** Paper 2 is at its first version. Paper 1 is at **v2 (November 2026)**:
v1 described the two-card, swap-serialized substrate and a four-family roster, and its
measurements are the ones both versions report. v2 updates the substrate description to
the three-card deployment, marks muse-glimmer as retired, restates the family-diversity
invariant against the current roster, records the intuition seat's move into the
conscious model's family, refreshes the memory-throughput figure, and adds a roster
table covering both dates. No experiment was re-run and no result or number changed;
the version note is printed on the paper's first page and in its reproducibility
section.

Both PDFs were recompiled from the sources in this directory on 2026-11-07 at the
versions committed here. The measurements they report were frozen in September
2026; the papers state where a later instrument reading supersedes an earlier one
(Paper 2, run-to-run variance section). No reported number was changed for this
release. The only source edits were the addition of a missing
`\label{sec:baseline}` — three cross-references in Paper 2 were rendering
undefined without it — and the reproduction footnote path, which now points at
this public repository instead of the private working copy.

## License

Paper text and figures: CC BY 4.0, see [`LICENSE-CC-BY-4.0.txt`](LICENSE-CC-BY-4.0.txt).
Code in this repository: MIT, see [`../LICENSE`](../LICENSE).
