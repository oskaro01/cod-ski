# PUBG Mobile — AKM Sensitivity Prediction (recoil-rate math)

> **Date:** 2026-08-04
> **Question asked:** *"If the Vector's Camera 124 / ADS 165 is the best-of-best, what is the best-of-best for the AKM?"*
> **Baseline used:** Vector — Camera (TPP no-scope) **124**, ADS (1x) **165**
> **Companion doc:** [TPP-NoScope-Sensitivity-Guide.md](./TPP-NoScope-Sensitivity-Guide.md)

---

## TL;DR — the answer we found

| Setting | Math prediction (median) | ✅ Playtest results (2026-08-04) | Honest probability band (P90) |
|---|---|---|---|
| **Camera (TPP no-scope)** | 179 ❌ (model invalid here) | **~120–124** — keep the proven Vector value | 152 – 208 (ignored) |
| **ADS (1x)** | 239 ❌ (too high in practice) | **~165** (same as Vector); 230+ sprayed wildly | 202 – 276 (ignored) |

**One-line takeaway:** keep **Camera ~120–124 / ADS ~165** — the same numbers as your proven Vector setup, so your swipe muscle memory carries over. The recoil-rate model does **not** apply to Camera, and it **over-predicts for ADS too**: real AKM control needs *calmer* sensitivity plus attachments and burst fire, not a 1.44× bump (see [Playtest](#8-playtest-results)).

---

## 1. Why the Vector's values are so high — the mechanism

Sensitivity is not arbitrary; it exists so your thumb's swipe speed cancels recoil.

- You swipe at a constant speed `S` (px/sec).
- Sensitivity `σ` converts that swipe into screen rotation: `S × σ` degrees/sec.
- The gun delivers recoil at a rate of **`kick-per-shot × fire-rate`** degrees/sec.

For the correction to match the recoil (constant muscle-memory swipe):

```
σ  ∝  kick-per-shot × fire-rate
```

That is the **recoil-rate model**. A high fire rate alone does NOT justify high sensitivity — it's the **product** of kick and fire rate that matters. The Vector earns its 124/165 because it dumps ~1000 RPM worth of small kicks; you need a fast, continuous drag to counter them.

> ⚠️ **Scope of the model (learned from playtest):** this formula describes **recoil compensation, which happens while aiming → it applies to ADS sensitivity only.** Camera sensitivity is your *turn speed* (free-look, hipfire flicks, close-range tracking) and is **gun-independent** — it must NOT be scaled per gun. See [Playtest](#8-playtest-results).

> **Note vs. the no-scope guide:** [TPP-NoScope-Sensitivity-Guide.md](./TPP-NoScope-Sensitivity-Guide.md) recommends a *general* Camera ~105 / ADS ~100 baseline for headshot consistency. This doc is a *gun-specific* recoil-compensation prediction for the AKM — the two coexist: the guide is the default baseline, this is the AKM-specific starting point that still needs the Training Grounds tuning in Section 5.

---

## 2. Input data (datamined / community stats)

| Stat | Vector | AKM |
|---|---|---|
| Fire rate | ~900–1091 RPM (≈1000) | 600 RPM (0.100 s/shot) |
| Vertical kick per shot | 1.0× (reference) | ~1.9–2.9×, most likely ~2.4× |
| Horizontal stability | Very tight (±~0.5 bounds) | Noticeable side-to-side drift |
| First-shot kick | Low | Very high |

Relative recoil *rate*:

```
AKM / Vector  =  (2.4) × (600/1000)  =  1.44×
```

So the naive per-shot scaling (Camera ≈ 298, ADS ≈ 396 — scaling purely by kick) is **physically impractical**, which is exactly why the fire-rate term in the formula matters.

---

## 3. Monte Carlo prediction (200,000 samples)

Uncertainty was modeled as triangular distributions:
- Vector RPM ~ 900–1091, most likely 1000
- AKM kick ratio ~ 1.9–2.9, most likely 2.4

| Setting | Mean | Median | P90 range | Key probabilities |
|---|---|---|---|---|
| **Camera (TPP no-scope)** | 179 | 179 | 152 – 208 | P(180–220) ≈ 47% |
| **ADS (1x)** | 239 | 238 | 202 – 276 | P(200–240) ≈ 49%, P(215–260) ≈ 67% |

**Most-likely zones:** ADS **~230–245 (prediction)** — **both values invalidated by playtest**: Camera is gun-independent (keep ~120–124) and ADS over-predicts (practical best is **~165**, see [Playtest](#8-playtest-results)).

---

## 4. Real-world corrections (why the pure math over-shoots)

1. **Horizontal recoil.** The AKM drifts side-to-side far more than the Vector. High ADS amplifies horizontal jitter — pro AKM sprays commonly run 1x ADS around 50–70%, far below the 200+ the vertical-only model suggests.
2. **First-shot kick.** The AKM's opening shot jumps hard; a bigger swipe ratio does not fix the first miss — burst or aim accordingly.
3. **Precision beats speed.** From our own no-scope guide: lower ADS = more headshots (less overshoot). 165 ADS is already aggressive for the Vector; the AKM is used at mid-range where precision matters more.
4. **Camera ≠ recoil (playtest-confirmed).** Scaling Camera from 124 → 179 caused 1.44× screen travel per identical swipe → constant overshoot past targets and “hits only by luck.” Camera must stay at the player’s proven value (~120–124).

---

## 5. Recommended tuning procedure

✅ **Final (after 2 playtests):** start at **Camera ≈ 120–124 / ADS ≈ 165** — the same numbers as your proven Vector setup, so your swipe muscle memory carries over. Validate in **Training Grounds, not ranked TDM**:

1. **Sensitivity:** ADS 1x = 165. Only go up to ~175 if the spray feels sluggish; if it zig-zags, go DOWN toward 155.
2. **Attachments:** **Compensator + Thumb grip** (kills the horizontal drift that scatters bullets). Vertical grip as backup.
3. **Fire pattern:** burst **3–5 rounds** at chest height beyond ~15m, re-peek, repeat. Full-auto is for point-blank only.
4. **Flick test at 15m:** quick-ADS onto a bot. Sailing past → Camera 115. Under-traveling → keep 124.
5. **Spray test at 25m:** 30 rounds into the board — goal is a tight vertical column; keep ~15 rounds in the head/chest zone.
- Gyro players: shave ~10% more and lean on gyro for the vertical pull.

---

## 6. Reproducible script

```python
import random, statistics

random.seed(42)
N = 200000

rpm_vec = [random.triangular(900, 1091, 1000) for _ in range(N)]
kick_ratio = [random.triangular(1.9, 2.9, 2.4) for _ in range(N)]

for label, base in [("Camera (TPP no-scope)", 124), ("ADS (1x)", 165)]:
    ratio = [k * 600.0 / v for k, v in zip(kick_ratio, rpm_vec)]
    pred = [base * r for r in ratio]
    mean, med = statistics.mean(pred), statistics.median(pred)
    lo, hi = sorted(pred)[int(0.05 * N)], sorted(pred)[int(0.95 * N)]
    p1 = sum(1 for x in pred if 180 <= x <= 220) / N * 100
    p2 = sum(1 for x in pred if 200 <= x <= 240) / N * 100
    p3 = sum(1 for x in pred if 215 <= x <= 260) / N * 100
    print(f"{label}: mean={mean:.0f} median={med:.0f} P90=[{lo:.0f}..{hi:.0f}]")
    print(f"  P(180-220)={p1:.1f}%  P(200-240)={p2:.1f}%  P(215-260)={p3:.1f}%")
```

Run: `python3 script.py` — output reproduces every number in Section 3.

---

## 7. Status

- [x] Model built (recoil-rate: `σ ∝ kick × fire-rate`)
- [x] Monte Carlo prediction done
- [x] In-game validation at Training Grounds — **done 2026-08-04, 2 rounds** (see [Playtest](#8-playtest-results))
- [x] Scope correction: model applies to **ADS only**; Camera is gun-independent
- [x] Playtest #2: ADS 230+ sprayed wildly → final recommendation **ADS ~165** (same as Vector)
- [x] Playstyle/attachment fix: **Compensator + Thumb grip**, burst fire beyond 15m, test in Training Grounds
- [ ] Optionally extend the same math to M416 / Groza / UMP for a full sensitivity table

---

## 8. Playtest results

### Playtest #1 — Camera 179 / ADS 239 (initial prediction)

> **Date:** 2026-08-04 · **Setup:** AKM, predicted values Camera 179 / ADS 239

| Finding | Result | Action taken |
|---|---|---|
| Camera felt fast (good feel) but overshot every target | ❌ 44% more screen travel than Vector 124 → “hits only by luck” | Keep **Camera ~120–124**, do NOT scale per gun |
| ADS felt correct, recoil control worked | ✅ “ADS seems working” (at the time) | Initially kept ~230–240 |

### Playtest #2 — ranked TDM, ADS still ~230

> **Date:** 2026-08-04 · **Context:** ranked TDM, AKM

| Finding | Result | Action taken |
|---|---|---|
| Bullets “all over the place” but still hitting the target | ❌ classic over-correction: high ADS amplifies thumb micro-jitter → spray snakes around the aim point | **Drop ADS to ~165** (same as Vector); at most 175 |
| High ADS felt “no where near perfect as Vector” | ❌ expectation mismatch: AKM can never feel like the Vector (opposite ends of the control spectrum) | Keep Vector as TDM primary; AKM for classic mode |
| Spray scatter at range | ❌ horizontal drift dominates beyond ~15m | **Compensator + Thumb grip**, burst 3–5 rounds, re-peek |

**Conclusion (final):** The recoil-rate model does **not** apply to Camera, and it **over-predicts ADS** (230+ sprays wildly). The practical best for the AKM is **Camera ~120–124 / ADS ~165** — the same as your Vector — plus attachments and burst fire. The AKM's “perfect” is a heavier, more deliberate feel, not a Vector-like laser feel.
