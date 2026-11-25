# 24-Hour Hackathon Execution Plan (Checkpoint in 7 Hours)

## ⏱️ Timeline Allocation

### Phase 1: Hours 0 – 7 (TARGET: CHECKPOINT 1 DEMO)
**Goal:** Deliver a working end-to-end prototype that proves the concept live.
- **Track 1 (ML / Backend):**
  - Extract feature patches using pre-trained WideResNet50 / DINOv2.
  - Implement basic PatchCore / nearest-neighbor anomaly scoring on golden normal reference images.
  - Generate pixel-level anomaly heatmap overlay.
  - Expose a simple `/inspect` API accepting an image and returning:
    - `is_anomaly`: bool
    - `anomaly_score`: float
    - `heatmap_base64`: string
- **Track 2 (Frontend / UI):**
  - Build the core **Split-Screen Inspection View** (Original Image vs. Anomaly Heatmap).
  - Add an interactive file upload / camera simulation stream.
  - Live metric card: Anomaly Score & Status badge (NORMAL / DEFECT DETECTED).
- **Milestone at Hour 7:** Upload an unseen defect image -> see real-time localization heatmap and score on the frontend dashboard.

---

### Phase 2: Hours 7 – 16 (Core Innovation & Differentiation)
**Goal:** Build the three hardest evaluation requirements.
1. **Distribution-Shift Gate (Covariate Shift vs Defect):**
   - Global MMD calculation to detect lighting/camera changes.
   - UI indicator: "Environmental Shift Detected" (Alerts without falsely discarding the component).
2. **Defect Severity Engine:**
   - Compute defect area percentage, peak intensity, and contour metrics.
   - Categorize into Minor / Major / Critical.
3. **Confidence Calibration:**
   - Implement conformal prediction or temperature scaling.

---

### Phase 3: Hours 16 – 21 (False-Positive Management & Polish)
**Goal:** Build the industrial edge.
- Implement the **"Mark as Benign / False Alarm"** button on the UI.
- When clicked, push patch embeddings into the active normal memory bank so that specific variation is never flagged again.
- Real-time performance profiling (<50ms per frame).

---

### Phase 4: Hours 21 – 24 (Demo Rehearsal, Slides & Pitch)
- Prepare 3 compelling demo test cases:
  1. *Golden Normal Sample* -> Green checkmark (Confidence 99%).
  2. *Benign Lighting/Shadow Change* -> Yellow warning: "Covariate Shift (Lighting), Component Intact".
  3. *Unseen Defect (Micro-crack/Foreign Particle)* -> Red alert with localized heatmap, severity score, and recommended action.
- Final pitch deck presentation.
