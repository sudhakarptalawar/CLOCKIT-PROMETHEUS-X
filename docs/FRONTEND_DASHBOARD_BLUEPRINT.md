# PROMETHEUS-X: Industrial Mission-Control Dashboard Blueprint

Designed for rapid delivery (7-Hour Checkpoint & 24-Hour Final Presentation).

---

## 🎨 Design Philosophy & Theme
- **Theme**: Industrial Mission-Control / Dark Sci-Fi Clean (`bg-slate-950`, `text-slate-100`, accents in Cyan `#06b6d4`, Amber `#f59e0b`, and Emerald `#10b981`, with Defect alerts in Electric Crimson `#f43f5e`).
- **Target Audience**: Quality Assurance (QA) Plant Engineers & Evaluation Judges.
- **Core Value Prop**: Instantly reveals *why* a part is rejected, *where* the defect lies, *how severe* it is, and whether it was triggered by a lighting shift vs. a real structural defect.

---

## 🖥️ Screen Layout Wireframe

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│ 🛰️ PROMETHEUS-X | Industrial Open-Set QA System        [Production Line: PCB-04] [Live Status: 🟢]│
├────────────────────────────────────────┬─────────────────────────────────────────────────────────┤
│ PANEL A: Visual Inspection & Heatmap   │ PANEL B: Intelligence & Severity Telemetry              │
│                                        │                                                         │
│  [ Split / Overlay Slider ]            │  ┌─────────────────────────┐ ┌────────────────────────┐  │
│  ┌──────────────────┬────────────────┐ │  │ DECISION BADGE          │ │ SEVERITY METER (DSI)   │  │
│  │ Original Frame   │ Anomaly Heatmap│ │  │ 🚨 UNSEEN DEFECT DETECTED│ │ [==== 78/100 ====]     │  │
│  │                  │ (Jet / Viridis)│ │  │ Grade: CRITICAL SCRAP   │ │ Area: 3.4% | Peak: 0.91│  │
│  │                  │                │ │  └─────────────────────────┘ └────────────────────────┘  │
│  └──────────────────┴────────────────┘ │                                                         │
│  Heatmap Opacity: [====●========] 65%  │  ┌───────────────────────────────────────────────────┐  │
│  Inspection Mode: [ Live / File Upload]│  │ DISTRIBUTION SHIFT GATE (Covariate vs Semantic)   │  │
│                                        │  │ 🟢 Ambient Lux: Nominal (MMD: 0.04)               │  │
│                                        │  │ 🟢 Camera Alignment: Nominal                      │  │
│                                        │  │ ℹ️ Status: True Structural Anomaly (Not Env Drift)│  │
│                                        │  └───────────────────────────────────────────────────┘  │
│                                        │                                                         │
│                                        │  ┌───────────────────────────────────────────────────┐  │
│                                        │  │ CONFIDENCE CALIBRATION (Conformal Prediction)     │  │
│                                        │  │ Calibrated Confidence: 97.4% (p < 0.01)           │  │
│                                        │  │ Epistemic Uncertainty: LOW                        │  │
│                                        │  └───────────────────────────────────────────────────┘  │
│                                        │                                                         │
├────────────────────────────────────────┴─────────────────────────────────────────────────────────┤
│ PANEL C: False-Positive Mitigation & Operator Actions (The "Killer Feature" for Judges)           │
│                                                                                                  │
│ [ ❌ Confirm Defect & Quarantine ]    [ ⚡ Mark as Benign Variation (Add to Memory Bank) ]         │
│                                        └─► Clicking instantly adapts normal baseline memory!      │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🚀 Key Dashboard Components & What Judges Look For

### 1. Dual-View Inspection Window (Left Half)
- **Interactive Before/After or Overlay**:
  - Left: Raw camera capture.
  - Right: Grad-CAM / PatchCore anomaly localization heatmap showing exact pixel boundary of the defect.
  - Interactive opacity slider: Operator drags to blend raw image and anomaly mask.
- **Bounding Box Overlay**: Auto-computed contour enclosing the highest intensity cluster.

### 2. Telemetry HUD (Right Half)
- **Status Verdict Banner**:
  - `🟢 PASS: NORMAL SAMPLE` (Score: 0.12)
  - `🟡 ATTENTION: COVARIATE SHIFT DETECTED` (Lighting/batch change, but part intact)
  - `🔴 REJECT: UNSEEN ANOMALY DETECTED` (Score: 0.89)
- **Defect Severity Dial / Radial Gauge**:
  - Displays the 0-100 Defect Severity Index (DSI).
  - Metrics breakdown: Affected Surface Area (%) and Peak Anomaly Intensity.
  - Action Recommendation: `Rework`, `Quarantine`, or `Immediate Line Halt`.
- **Distribution Shift Sensor**:
  - Shows real-time Maximum Mean Discrepancy (MMD).
  - Proves the system is smart enough not to fail when the sun comes out or lighting changes!
- **Calibrated Uncertainty Bar**:
  - Shows statistically rigorous conformal prediction interval instead of raw heuristics.

### 3. The "Killer Demo Feature": Real-time False-Positive Management Button
- When a judge asks: *"What if this is just a harmless normal variance that your model has never seen?"*
- The operator clicks: **"Register as Benign Variation"**.
- The backend takes the patch vector, pushes it into the normal coreset, and immediately re-evaluates the image:
  - The status flips from **🔴 DEFECT** to **🟢 VERIFIED BENIGN VARIANT** right before the judges' eyes!
