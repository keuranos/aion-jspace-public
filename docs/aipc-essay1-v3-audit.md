# Essay 1 v3 numbers audit (2026-09-04)

Method: every number in the merged v3 text traced to raw artifacts on laskin01
(~/jspace-precision/: p3_results_v4.json [97 items, graded at run time],
p3_question_bank_deveto.json [97 de-veto generations, Sep 2 11:47],
p3_results_n20.json [79-item determinism run], p3_question_bank.json, p3_harness.py).
Recomputed with the committed harness (p3_harness.grade / grade_lens).

## REPRODUCED (essay may keep)
- 97-item battery: 97 items in v4. OK.
- World facts 93%: S3 14/15 = 93.3%. OK.
- Telemetry emitted 15%: S1 7/47 = 14.9%. OK.
- Telemetry lens 14%: S1 4 correct / 29 gradeable (18 string/list NA) = 13.8%. OK
  (note: denominator is gradeable items, not all 47 — worth stating in essay).
- "I'll check" 41/47: broad check/look pattern in S1 emitted = 41/47. OK.
- n=20 determinism: p3_results_n20.json exists (79 items, greedy); determinism
  claim refers to probe runs documented in paper 1. OK with pointer.

## NOT REPRODUCED (essay must correct)
- Telemetry de-veto 7%: recomputed 30/47 gradeable = 64% (variants: 34-60%
  with stricter text cuts). The committed harness + committed de-veto texts
  do not produce 7%. The 7% in p3_key_results.md came from a grading pass
  whose method is not recoverable from the repo. UNVERIFIED — replace or drop.
- De-veto booleans 4/19 vs 10/19: recomputed 8/19 vs 10/19 (both v3 and v4
  runs, current and historical harness, current and committed deveto file).
  The 10/19 emitted half reproduces; the 4/19 de-veto half does not.
  UNVERIFIED — replace with 8/19 or re-run the grading with live truth.

## RECOMMENDED ESSAY FIX
Replace: "De-veto generation does not beat emission on self-model claims
(4/19 vs 10/19 booleans correct)" and "telemetry 7% de-veto"
With: "De-veto generation does not beat emission on self-model claims
(8/19 vs 10/19 booleans correct)" and "telemetry 64% de-veto" — OR re-run
the de-veto grading against fresh live telemetry and update all numbers.
Direction of the finding is UNCHANGED either way (de-veto does not beat
emission; the asymmetry holds), but the magnitudes in the essay must match
what the committed data actually shows.
