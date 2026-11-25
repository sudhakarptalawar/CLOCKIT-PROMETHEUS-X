# PROMETHEUS-X: Open-Set Industrial Anomaly Detection

> **Detect the Defect That Your Model Has Never Been Trained to Recognize**  
> Advanced Computer Vision for Industrial Quality Control under Changing Production Conditions.

---

## 🎯 Problem Statement
Traditional quality inspection systems fail when confronted with **novel, rare, or unseen defect types** because supervised models only recognize classes seen during training. 

**PROMETHEUS-X** tackles this fundamental challenge by:
1. Learning normal manufacturing patterns using high-fidelity spatial representations (One-Class / Self-Supervised).
2. Detecting, localizing (pixel-level heatmaps), and quantifying unseen defects.
3. Decoupling benign **Distribution Shifts** (lighting variations, camera drift, batch changes) from actual **Semantic Anomalies**.
4. Estimating **Defect Severity** with actionable engineering metrics.
5. Calibrating confidence to eliminate high-risk false alarms via an **Active Learning / False-Positive Management** loop.

---

## 🏗️ Project Architecture

```
PROMETHEUS-X/
├── backend/
│   ├── app/
│   │   ├── api/             # FastAPI REST & WebSocket endpoints
│   │   ├── core/
│   │   │   ├── detector.py      # PatchCore / Feature Memory Anomaly Engine
│   │   │   ├── drift.py         # MMD & Covariate Shift Decoupling
│   │   │   ├── severity.py      # Morphological & Critical Zone Severity Engine
│   │   │   └── calibrator.py    # Conformal Prediction & Uncertainty Estimator
│   │   └── main.py          # Application entrypoint
│   └── requirements.txt
├── frontend/                # Interactive Operator Dashboard
├── data/
│   ├── baseline_normal/     # Golden samples used for normal manifold
│   └── test_samples/        # Test frames (benign shift + unseen defects)
└── docs/
    ├── ARCHITECTURE.md      # Deep technical breakdown
    └── CHECKPOINT_PLAN.md   # 24-Hour sprint & 7-hour checkpoint roadmap
```

---

## ⚡ Quickstart

### Backend Setup
```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # Or .venv\Scripts\activate on Windows
pip install -r requirements.txt
python -m app.main
```

---

## 👥 Team & Hackathon Milestones
- **Checkpoint 1 (Hour 7)**: Working baseline demo (Normal vs. Unseen Defect localization + initial dashboard UI).
- **Final Checkpoint (Hour 24)**: Full end-to-end pipeline with severity metrics, distribution-shift gate, and active false-positive buffer.
