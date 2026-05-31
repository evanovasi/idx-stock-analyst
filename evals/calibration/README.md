# Calibration Results — Iteration 1

Three test cases were run through the skill, with a no-skill baseline (vanilla Claude) on two of
them for comparison. All 17 assertions passed (6 + 5 + 6).

| Test case | Setup | With skill | Baseline |
|---|---|---|---|
| `eval-0-controlled-bullish` | Strong fundamentals + bull-stacked technicals, no negative catalyst | **STRONG BUY 89/100**, full quantified scorecard, math verified | Reached "BUY" but no 0-100 scores, no scalping view, no confidence level |
| `eval-1-controlled-skip` | Choppy range, thin volume, repeated fakeouts, expensive | **SKIP/WAIT 45/100**, no-force-BUY guardrail held | Also "SKIP", but no quantification |
| `eval-2-live-bbri` | Minimal live input ("analisa BBRI 1 bulan") | **HOLD/SPEC BUY 60/100**, auto web-sourced, FX/no-chart assumptions flagged | (not run) |

## Calibration finding -> banking variant in rubric

The BBRI run surfaced a real bug: the rubric's `DER` and `interest coverage` lines penalize banks
unfairly (a bank's leverage is its business model — deposits — and "interest coverage" is not a
bank metric). The rubric now includes a **banks/financials variant** that replaces those two lines
with **Capital adequacy (CAR)** and **Asset quality (NPL/LAR trend)**. See `references/scoring-
rubric.md` (last section).

## How to reproduce

Run the skill against each prompt with current data; expected pass criteria:

- **eval-0**: Final Decision in {BUY, STRONG BUY}; Final Score >= 70; weighted-score table shown;
  Fundamental Score >= 75; disclaimer present; separate swing+scalping sections.
- **eval-1**: Final Decision in {SKIP/WAIT, HOLD}; explicitly cites choppy / thin-volume / fakeout
  as reason; Final Score in 40-69 band or below; separate swing+scalping; disclaimer.
- **eval-2**: Full 14-section report; current BBRI price obtained from web; assumptions explicitly
  labeled; weighted score table + clear decision; Sources section; disclaimer.
