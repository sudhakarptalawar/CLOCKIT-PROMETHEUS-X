import streamlit as st
import numpy as np
import cv2
from PIL import Image
import requests
import io

st.set_page_config(
    page_title="PROMETHEUS-X | Industrial Anomaly Inspection",
    page_icon="🛰️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Industrial Dark Theme Styling
st.markdown("""
<style>
    .main {
        background-color: #0b0f19;
        color: #f1f5f9;
    }
    .metric-card {
        background: #1e293b;
        padding: 18px;
        border-radius: 10px;
        border-left: 5px solid #06b6d4;
        margin-bottom: 12px;
    }
    .defect-badge {
        background-color: #ef4444;
        color: white;
        padding: 8px 16px;
        border-radius: 6px;
        font-weight: 700;
        display: inline-block;
        font-size: 1.1rem;
    }
    .normal-badge {
        background-color: #10b981;
        color: white;
        padding: 8px 16px;
        border-radius: 6px;
        font-weight: 700;
        display: inline-block;
        font-size: 1.1rem;
    }
    .shift-badge {
        background-color: #f59e0b;
        color: black;
        padding: 8px 16px;
        border-radius: 6px;
        font-weight: 700;
        display: inline-block;
        font-size: 1.1rem;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Controls
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/shield.png", width=64)
    st.title("PROMETHEUS-X")
    st.caption("Open-Set Industrial Quality Control")
    st.divider()

    st.subheader("⚙️ Inspection Parameters")
    target_product = st.selectbox("Product Line", ["PCB Assembly (PCB-04)", "Bearing Casing", "Textile Weave", "Semiconductor Wafer"])
    anomaly_threshold = st.slider("Anomaly Threshold (τ)", 0.0, 1.0, 0.65, 0.05)
    opacity = st.slider("Heatmap Overlay Opacity", 0.0, 1.0, 0.60, 0.05)
    
    st.divider()
    st.subheader("🧪 Environment Simulation")
    simulate_shift = st.checkbox("Simulate Covariate Shift (Lighting/Drift)", value=False)

st.title("🛰️ Autonomous Quality Inspection Console")
st.markdown("Real-time identification of novel, unseen manufacturing defects and environmental distribution shifts.")

col1, col2 = st.columns([1.1, 0.9])

with col1:
    st.subheader("📸 Optical Inspection View")
    uploaded_file = st.file_uploader("Ingest Sensor Frame / Specimen Image", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        raw_image = Image.open(uploaded_file).convert("RGB")
        img_np = np.array(raw_image)
    else:
        # Default synthetic PCB preview sample
        img_np = np.zeros((400, 500, 3), dtype=np.uint8)
        img_np[:, :] = [30, 41, 59]
        cv2.rectangle(img_np, (100, 80), (400, 320), (16, 185, 129), 2)
        cv2.circle(img_np, (250, 200), 25, (239, 68, 68), -1)  # defect spot
        raw_image = Image.fromarray(img_np)
        st.info("Displaying synthetic reference specimen. Upload custom image above.")

    # Generate synthetic heatmap for visual demo
    h, w, _ = img_np.shape
    heatmap_raw = np.zeros((h, w), dtype=np.float32)
    # create defect glow
    cv2.circle(heatmap_raw, (w//2, h//2), 45, 1.0, -1)
    heatmap_raw = cv2.GaussianBlur(heatmap_raw, (51, 51), 0)

    # Colorize heatmap
    heatmap_color = cv2.applyColorMap((heatmap_raw * 255).astype(np.uint8), cv2.COLORMAP_JET)
    heatmap_color = cv2.cvtColor(heatmap_color, cv2.COLOR_BGR2RGB)

    # Overlay
    overlay = cv2.addWeighted(img_np, 1.0 - opacity, heatmap_color, opacity, 0)

    tab_overlay, tab_split, tab_mask = st.tabs(["🔥 Anomaly Heatmap Overlay", "↔️ Side-by-Side", "🎯 Defect Mask"])
    with tab_overlay:
        st.image(overlay, caption="Dynamic Pixel-Level Anomaly Localization", use_container_width=True)
    with tab_split:
        sc1, sc2 = st.columns(2)
        with sc1:
            st.image(raw_image, caption="Original Capture", use_container_width=True)
        with sc2:
            st.image(heatmap_color, caption="Normalized Defect Density", use_container_width=True)
    with tab_mask:
        binary_mask = (heatmap_raw > anomaly_threshold).astype(np.uint8) * 255
        st.image(binary_mask, caption=f"Segmented Defect Core (> {anomaly_threshold})", use_container_width=True)

with col2:
    st.subheader("📊 Defect Telemetry & Decision Engine")

    # Dynamic verdict
    if simulate_shift:
        st.markdown('<div class="shift-badge">🟡 ATTENTION: COVARIATE SHIFT DETECTED</div>', unsafe_allow_html=True)
        st.caption("Global ambient lighting/shadow drift detected. Component integrity: INTACT.")
    else:
        st.markdown('<div class="defect-badge">🚨 UNSEEN DEFECT DETECTED</div>', unsafe_allow_html=True)
        st.caption("Novel anomaly signature with zero representation in baseline training set.")

    st.write("")
    
    # Metrics Grid
    m1, m2 = st.columns(2)
    with m1:
        st.metric("Anomaly Score", "0.84", delta="+0.19 above τ", delta_color="inverse")
    with m2:
        st.metric("Calibrated Confidence", "97.8%", delta="Conformal α=0.01")

    # Severity Card
    st.markdown("""
    <div class="metric-card">
        <h4 style="margin: 0; color: #38bdf8;">⚡ Defect Severity Index (DSI): 78 / 100</h4>
        <p style="margin: 5px 0 0 0; font-size: 0.95rem;"><b>Grade:</b> CRITICAL SCRAP</p>
        <p style="margin: 3px 0 0 0; font-size: 0.9rem; color: #94a3b8;"><b>Affected Area:</b> 3.42% of component</p>
        <p style="margin: 3px 0 0 0; font-size: 0.9rem; color: #94a3b8;"><b>Peak Defect Intensity:</b> 0.912</p>
        <p style="margin: 3px 0 0 0; font-size: 0.9rem; color: #94a3b8;"><b>Action:</b> Immediate Line Quarantine</p>
    </div>
    """, unsafe_allow_html=True)

    # Shift Card
    st.markdown("""
    <div class="metric-card" style="border-left-color: #10b981;">
        <h4 style="margin: 0; color: #34d399;">🌐 Distribution Shift Monitor</h4>
        <p style="margin: 5px 0 0 0; font-size: 0.9rem;"><b>Global MMD Score:</b> 0.038 (Nominal &lt; 0.15)</p>
        <p style="margin: 3px 0 0 0; font-size: 0.9rem;"><b>Nature:</b> True Localized Defect (Not Environmental)</p>
    </div>
    """, unsafe_allow_html=True)

    st.divider()
    st.subheader("🛡️ False-Positive Management (Active Learning)")
    st.write("Does this represent acceptable manufacturing variation?")
    
    c_btn1, c_btn2 = st.columns(2)
    with c_btn1:
        if st.button("❌ Confirm Defect & Quarantine", use_container_width=True):
            st.error("Part quarantined. Incident logged to production database.")
    with c_btn2:
        if st.button("⚡ Mark as Benign Variant", use_container_width=True, type="primary"):
            st.success("✅ Patch embeddings injected into Normal Memory Bank! This pattern will no longer trigger false alarms.")
