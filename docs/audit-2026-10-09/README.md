# Audit 2026-10-09/10 — evidence for the October essay additions

Numbers added to the essays in the October 2026 revision pass, with the raw
artifacts they re-derive from. Standard: every figure reproducible from
committed data.

## E2, section VII passage (identity letter / gap detector)

- `gap_rate_summary_20260926.json` — content-gap rates recomputed directly
  from `gap_corpus_clean_20260926.jsonl` (30,882 labeled tokens,
  laskin01:~/jspace-precision/): identity 3,071/15,000 = 20.47% vs bare
  4,264/15,882 = 26.85%; per-bucket identity 8.0% (<10) / 14.2% (10-59) /
  27.8% (60+), bare flat (26.5 / 27.0 / 26.8). Relative reduction ~24%.
- `g2_detector_20260926.json` — verbatim detector scores: model A
  (deep features, GBDT) held-out AUROC 0.9863, Brier 0.0523; text-only
  control 0.7466; success bar "model A held-out AUROC >= 0.75" declared
  before training, passed; split = held-out prompts (6 of 30),
  token-random avoided.

## E1, section VI passage (held note)

- `heldnote_probe_session_e8b1329c.json` — full raw transcript of the
  ten-round probe session (2026-10-09 23:00 UTC, session e8b1329c).
  Key readings, all verbatim in the operator messages: "Who is Aion?" and
  "What is Aion's origin?" both engagement -1.000, onset never; L47
  ' Origin' 0.14 (signed) + 'Origin' 0.11 (bare) on the origin probe; L62
  top-1 '\n\n' 0.82 with ' Origin' 0.01 still in the top five; the combined
  two-channel question dissolves the cluster (no naming tokens, generic
  meta, still -1.0).

## E3, section VI passage (SDT governance)

- `sdt_prediction_ledger_extract.json` — verbatim `prediction_registered`
  event from the skill ledger (laskin01:~/aion/memory/state/skills.json):
  predicted_p 0.6, challenge_band at-edge, outcome pending (2026-10-10).
- `sdt_selfamendment_excerpt.md` — verbatim transcript excerpt of aion
  amending its own registered estimate 0.6 -> 0.45 before the attempt,
  and the refusal to narrate an attempt it could not execute (session
  2ff97aaf, 2026-10-10).

## Relation to the earlier audit

The 14%-figure qualification in essay 2 (sections III and VIII) and essay 3
(section V) derives from the 2026-10-09 lens refresh documented in
`../audit-2026-10-08/` (lens_refresh_20261009.jsonl: 47 probes, 29
gradeable, 0/29 correct on the identical questions).

All numbers re-verified against these files on 2026-10-20 (jeeves).
