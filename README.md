# IDX Stock Analyst — Claude Skill

Skill profesional untuk analisis saham Indonesia (IDX/BEI) di Claude / Claude Code / Cowork.
Mengubah satu kode saham, screenshot chart, atau PDF laporan keuangan menjadi keputusan trading
terukur (**STRONG BUY / BUY / HOLD / SKIP / SELL / STRONG SELL**) lewat rubrik penilaian
deterministik 0–100 di lima pilar.

> Status: tested & calibrated — see [`evals/calibration/`](evals/calibration/) (17/17 assertions
> passed across bullish / skip / live test cases).

---

## Apa yang dilakukan skill ini

Saat aktif, skill akan:

1. **Membaca apa yang kamu berikan** — kode saham, screenshot chart (OHLC + struktur + S/R),
   PDF laporan keuangan (revenue, laba, ekuitas, DER, OCF, EPS, dll), atau angka yang kamu ketik.
2. **Mengisi celah lewat web search** — harga terakhir, berita & katalis, level IHSG, valuasi
   peer sektor, aksi korporasi (MSCI/FTSE/LQ45, transaksi pengendali, UMA BEI).
3. **Menghitung skor 5 pilar secara deterministik**:
   Fundamental (30%) · Teknikal (35%) · Smart Money (15%) · Momentum (10%) · Risk/Safety (10%).
4. **Mengeluarkan laporan terstruktur 14 bagian** — ringkasan eksekutif, breakdown skor,
   setup **Swing & Scalping terpisah** (entry / stop loss / TP1 / TP2 / R:R / probabilitas),
   penilaian risiko, sumber, dan disclaimer.

Rubrik lengkap ada di [`references/scoring-rubric.md`](references/scoring-rubric.md), termasuk
**varian bank/financials** untuk emiten perbankan (BBRI, BBCA, BMRI, dll) yang menggantikan
DER & interest coverage dengan CAR & NPL/LAR.

---

## Instalasi

### Metode 1 — Claude Code (clone ke direktori skills) — paling cepat

**Linux / macOS:**
```bash
git clone https://github.com/evanovasi/idx-stock-analyst.git \
  ~/.claude/skills/idx-stock-analyst
```

**Windows (PowerShell):**
```powershell
git clone https://github.com/evanovasi/idx-stock-analyst.git `
  "$env:USERPROFILE\.claude\skills\idx-stock-analyst"
```

Restart Claude Code → skill akan ditemukan otomatis. Untuk verifikasi, ketik `/` lalu cari
`idx-stock-analyst`, atau langsung tanya `analisa BBRI 1 bulan` — skill akan ke-trigger sendiri.

### Metode 2 — Cowork (file .skill) — untuk Cowork desktop

```bash
git clone https://github.com/evanovasi/idx-stock-analyst.git
cd idx-stock-analyst
python3 build-skill.py     # menghasilkan idx-stock-analyst.skill
```

Buka file `idx-stock-analyst.skill` yang dihasilkan di Cowork → klik **Save skill**.

### Metode 3 — Manual

Salin `SKILL.md` dan folder `references/` ke direktori skills Claude di komputermu:

- Linux/macOS: `~/.claude/skills/idx-stock-analyst/`
- Windows: `%USERPROFILE%\.claude\skills\idx-stock-analyst\`

Hasilnya harus seperti ini:
```
~/.claude/skills/idx-stock-analyst/
├── SKILL.md
└── references/
    └── scoring-rubric.md
```

---

## Cara pakai (auto-trigger)

Tidak perlu perintah khusus — skill mengenali frasa natural. Contoh prompt yang langsung memicu:

- `analisa CUAN timeframe harian, ini lagi jeblok`
- `BBRI bagus gak buat swing 1 bulan?`
- `entry, stop loss, sama take profit ANTM di berapa?`
- `GOTO 1 bulan layak masuk gak` (cukup ticker + timeframe)
- Upload screenshot chart / PDF laporan keuangan, lalu tanya `menurutmu gimana?`

**Tips presisi:**
- Sertakan **screenshot chart harian** → indikator teknikal dipakai data nyata, bukan estimasi.
- Sertakan **PDF laporan keuangan** → angka fundamental presisi (revenue, OCF, leverage, dll).
- Kalau cuma kasih ticker, skill jalan dalam mode **Hybrid**: cari harga/berita terbaru sendiri,
  isi sisanya dengan asumsi yang ditandai jelas (FX, dll).

**Yang TIDAK ditangani skill ini** (by design, supaya tidak over-trigger):
- Penjelasan konsep umum (`apa itu RSI`, `beda swing vs scalping`)
- Cek harga saham doang tanpa analisis
- Watchlist / screening banyak saham sekaligus
- Ringkasan berita makro / IHSG
- Saham non-Indonesia (AAPL, TSLA, dll)

---

## Decision bands

| Final Score | Keputusan |
|---|---|
| 85–100 | STRONG BUY |
| 70–84 | BUY |
| 55–69 | HOLD / SPEC BUY |
| 40–54 | SKIP / WAIT |
| < 40 | SELL (STRONG SELL jika < 25) |

Rumus: `Final = 0.30·F + 0.35·T + 0.15·SM + 0.10·M + 0.10·RS`

---

## Guardrail bawaan

- **Tidak pernah memaksa BUY** di kondisi choppy / volume tipis / struktur tidak jelas / ada
  katalis jual terjadwal (mis. delisting MSCI) → default **SKIP / WAIT**.
- **Swing dan Scalping selalu dipisah** (entry, stop, time horizon berbeda).
- Setiap setup wajib punya entry, stop, TP1/TP2, R:R yang dihitung, dan probabilitas keberhasilan.
- **Bukan nasihat keuangan berlisensi** — disclaimer otomatis disertakan di tiap output.

---

## Struktur repo

```
.
├── SKILL.md                          ← skill utama (metadata + instruksi)
├── references/
│   └── scoring-rubric.md             ← rubrik deterministik 5 pilar + varian bank
├── evals/
│   ├── trigger-eval.json             ← 20 query stress-test (10 trigger / 10 near-miss)
│   └── calibration/
│       └── README.md                 ← ringkasan hasil kalibrasi iterasi-1
├── build-skill.py                    ← script untuk menghasilkan file .skill
├── README.md
├── LICENSE                           ← MIT
└── .gitignore
```

---

## Lisensi

MIT — lihat [`LICENSE`](LICENSE).

## Disclaimer

Skill ini menghasilkan **analisis pendukung keputusan kuantitatif**, **bukan** nasihat keuangan
berlisensi. Penulis bukan penasihat keuangan. Skor, output BUY/SELL/SKIP, dan probabilitas adalah
alat bantu; keputusan transaksi dan risikonya sepenuhnya tanggung jawab pengguna. Sebagian
penghitungan (FX, valuasi peer, indikator yang diestimasi) bergantung pada asumsi yang selalu
ditandai jelas di output.
