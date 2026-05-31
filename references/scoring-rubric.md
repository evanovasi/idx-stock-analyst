# Deterministic Scoring Rubric

Apply these bands literally so identical inputs always produce identical scores. Each pillar sums
to 100. Where a metric is unavailable and cannot be sourced, award the neutral midpoint of that
line item and lower the AI Confidence Level — do not invent a value.

All "vs sector" judgments use the relevant IDX sector peers (e.g. coal: ADRO/ITMG/BYAN/PTBA;
banks: BBRI/BBCA/BMRI/BBNI; telco: TLKM/ISAT/EXCL). Pull peer multiples via web search if needed.

---

## 1. Fundamental Score (/100)

| Line item | Pts | Banding |
|---|---|---|
| Revenue growth YoY | 15 | >25% = 15 · 10-25% = 11 · 0-10% = 6 · <0% = 0 |
| Net profit growth YoY | 15 | >25% = 15 · 10-25% = 11 · 0-10% = 6 · <0% = 0 |
| ROE (annualized) | 15 | >20% = 15 · 15-20% = 12 · 10-15% = 9 · 5-10% = 5 · <5% = 2 |
| Net margin | 10 | >15% = 10 · 10-15% = 7 · 5-10% = 5 · <5% = 2 |
| DER (total liab / equity) | 15 | <0.5 = 15 · 0.5-1 = 12 · 1-2 = 8 · 2-3 = 4 · >3 = 1 |
| Interest coverage (op. profit / finance exp.) | 10 | >5x = 10 · 3-5x = 7 · 1.5-3x = 4 · <1.5x = 1 |
| Operating cash flow | 10 | positive & growing = 10 · positive = 7 · negative = 0 |
| Valuation vs sector (PER & PBV) | 10 | undervalued = 10 · fair = 6 · overvalued = 2 |

Notes:
- Annualize a quarterly figure as Q x 4 only when seasonality is mild; flag the caveat for
  cyclical sectors (coal, CPO, commodities).
- Market cap = shares outstanding x price. Convert to the report's currency for PER/PBV if the
  statements are in USD while the price is in IDR; state the FX assumption.
- A high growth rate off a tiny base is real but fragile — let the leverage/cash-flow/valuation
  lines pull the composite down rather than overweighting growth.

---

## 2. Technical Score (/100)

| Line item | Pts | Banding |
|---|---|---|
| Trend vs EMA 20/50/200 | 25 | price above all, bull-stacked = 25 · above 20 only = 15 · mixed = 10 · below all (death-stack) = 3 |
| MACD | 15 | bullish cross above 0 = 15 · bullish below 0 = 10 · flat = 6 · bearish = 3 |
| RSI | 15 | 50-65 = 13 · 40-50 = 10 · 65-70 = 9 · 30-40 = 7 · >70 overbought = 5 · <30 oversold (no reversal yet) = 4 |
| Market structure | 15 | HH-HL uptrend = 15 · base/range = 9 · LH-LL downtrend = 3 |
| Volume confirmation | 10 | rising on up-moves = 10 · neutral / not visible = 5 · rising on down-moves = 2 |
| Support/resistance position | 10 | bouncing off strong support = 10 · mid-range = 5 · breaking down through support = 2 |
| Volatility / Bollinger | 10 | inside bands, orderly = 8-10 · riding/exceeding a band = 3-5 |

Oversold (RSI<30) inside a strong downtrend is NOT a buy signal — it can stay oversold. Only
upgrade the read on a confirmed reversal (e.g. bullish engulfing / hammer with volume, or a
reclaim of a broken level).

---

## 3. Smart Money Score (/100)

| Line item | Pts | Banding |
|---|---|---|
| Accumulation vs distribution | 40 | clear accumulation = 32-40 · neutral = 20 · clear distribution = 0-8 |
| Insider / controlling-shareholder flow | 25 | buying = 20-25 · none = 12 · selling blocks = 0-5 |
| Breakout validity | 20 | valid, volume-backed = 16-20 · unconfirmed = 10 · repeated fakeouts = 0-5 |
| Index / institutional flow | 15 | inclusion / inflows = 12-15 · neutral = 8 · deletion / forced outflow = 0-3 |

Controlling-shareholder selling and index deletion (MSCI/FTSE/LQ45 removal) are strong
distribution signals — treat them as such even if price has already fallen.

---

## 4. Momentum Score (/100)

| Line item | Pts | Banding |
|---|---|---|
| Trend direction of momentum | 50 | strong up = 40-50 · mild up = 30-39 · flat = 20-29 · mild down = 10-19 · strong down = 0-9 |
| Rate of change / recent % move | 30 | constructive = 20-30 · neutral = 12-19 · sharp adverse move = 0-11 |
| Follow-through quality | 20 | green candles hold = 16-20 · choppy = 8-15 · bounces sold immediately = 0-7 |

---

## 5. Risk / Safety Score (/100) — higher = SAFER

This pillar is inverted on purpose so it adds positively to the weighted final score. A dangerous
setup scores LOW.

| Line item | Pts | Banding (safer = more points) |
|---|---|---|
| Volatility / ATR | 25 | calm = 20-25 · moderate = 12-19 · extreme daily swings = 0-11 |
| Max drawdown potential | 20 | limited downside / near strong support = 15-20 · moderate = 8-14 · open air below = 0-7 |
| False-breakout risk | 15 | low = 12-15 · medium = 7-11 · high = 0-6 |
| Correlation / basket risk | 15 | idiosyncratic = 12-15 · some = 7-11 · moves as a stressed basket = 0-6 |
| Event risk | 25 | none pending = 20-25 · minor = 10-19 · imminent adverse catalyst (index delete, suspension, UMA) = 0-9 |

---

## Sector variant: Banks & financials (IMPORTANT)

The Fundamental table above is calibrated for industrial / commodity / consumer issuers. For
**banks and financial institutions** (BBRI, BBCA, BMRI, BBNI, BRIS, ARTO, etc.) two lines do not
apply and would unfairly penalize a healthy bank — a bank's leverage IS its business model
(third-party deposits), and it has no "interest coverage" in the industrial sense.

For banks, replace those two lines as follows (keep the other six lines and the 100-pt total):

| Line item (bank variant) | Pts | Banding |
|---|---|---|
| Capital adequacy (CAR) | 15 | >22% = 15 · 18-22% = 12 · 14-18% = 8 · <14% = 3 |
| Asset quality (NPL / LAR trend) | 10 | improving & NPL low = 10 · stable = 6 · deteriorating = 2 |

Also reinterpret these for banks:
- "Revenue growth" -> net interest income / operating income growth.
- "Net margin" -> use NIM and cost-to-income as the quality read (high NIM, low CIR = full points).
- "ROE" band is unchanged but weight it heavily — ROE is the single best quality gauge for a bank.
- Valuation: judge on P/E and especially **P/BV vs the bank's own history and peers**, plus
  dividend yield. A mega-bank at trough P/BV with a high sustainable yield is "undervalued".

State explicitly when you apply the bank variant, and note it in the AI Confidence section.
