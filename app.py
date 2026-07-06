import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("flood_guard_model.pkl")

# Page setup
st.set_page_config(
    page_title="Flood Guard",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------------------------
# CUSTOM STYLING (UI ONLY — does not affect any prediction logic below)
# ---------------------------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }

    .stApp {
        background: linear-gradient(180deg, #061a2e 0%, #0b2a4a 45%, #0e3a63 100%);
    }

    /* Hero header */
    .hero {
        background: linear-gradient(135deg, #0ea5e9 0%, #2563eb 55%, #1e40af 100%);
        border-radius: 20px;
        padding: 2.2rem 2.5rem;
        margin-bottom: 1.8rem;
        box-shadow: 0 10px 30px rgba(2, 30, 60, 0.45);
        border: 1px solid rgba(255,255,255,0.08);
    }
    .hero h1 {
        color: white;
        font-size: 2.4rem;
        font-weight: 800;
        margin: 0;
        letter-spacing: -0.5px;
    }
    .hero p {
        color: rgba(255,255,255,0.9);
        font-size: 1.05rem;
        margin-top: 0.4rem;
        margin-bottom: 0;
        font-weight: 400;
    }

    /* Section card */
    .section-card {
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 16px;
        padding: 1.3rem 1.5rem 0.6rem 1.5rem;
        margin-bottom: 1.3rem;
        backdrop-filter: blur(6px);
    }
    .section-title {
        color: #7dd3fc;
        font-size: 1.45rem;
        font-weight: 800;
        margin-bottom: 0.6rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    /* Inputs */
    div[data-baseweb="input"] input, .stNumberInput input {
        background-color: rgba(255,255,255,0.06) !important;
        color: #f1f5f9 !important;
        border-radius: 10px !important;
        border: 1px solid rgba(255,255,255,0.15) !important;
    }
    label, .stNumberInput label {
        color: #cbd5e1 !important;
        font-weight: 700 !important;
        font-size: 1.05rem !important;
    }

    /* Predict button */
    div.stButton > button {
        background: linear-gradient(135deg, #22d3ee 0%, #2563eb 100%);
        color: white;
        font-weight: 700;
        font-size: 1.05rem;
        border-radius: 12px;
        padding: 0.75rem 2rem;
        border: none;
        box-shadow: 0 6px 18px rgba(37, 99, 235, 0.45);
        transition: transform 0.15s ease;
        width: 100%;
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 24px rgba(37, 99, 235, 0.6);
    }

    /* Result cards */
    .result-card {
        border-radius: 18px;
        padding: 1.6rem 1.8rem;
        margin-top: 1rem;
        border: 1px solid rgba(255,255,255,0.1);
        background: rgba(255,255,255,0.05);
    }
    .prob-number {
        font-size: 3rem;
        font-weight: 800;
        color: #f8fafc;
        margin: 0;
    }
    .prob-label {
        color: #94a3b8;
        font-size: 0.95rem;
        font-weight: 500;
        letter-spacing: 0.5px;
        text-transform: uppercase;
    }

    .footer-note {
        text-align: center;
        color: rgba(255,255,255,0.35);
        font-size: 0.8rem;
        margin-top: 2.5rem;
        padding-bottom: 1rem;
    }

    hr {
        border-color: rgba(255,255,255,0.08);
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# HERO HEADER
# ---------------------------------------------------------------------------
st.markdown("""
<div class="hero">
    <h1>🌊 Flood Guard</h1>
    <p>AI-Powered Flood Risk Prediction System — enter environmental and infrastructure
    indicators below to assess flood probability for a region.</p>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# INPUTS — grouped into attractive sections using tabs
# (same widgets, same variable names, same ranges/defaults as original)
# ---------------------------------------------------------------------------
tab1, tab2, tab3, tab4 = st.tabs([
    "🌦️ Environmental", "🏞️ Land & Water", "🏙️ Infrastructure & Human Factors", "🚨 Preparedness"
])

with tab1:
    st.markdown('<div class="section-card"><div class="section-title">🌦️ Environmental Indicators</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        monsoon = st.number_input("Monsoon Intensity", min_value=0.0, max_value=20.0, value=None, placeholder="Enter value (0-20)")
    with c2:
        climate = st.number_input("Climate Change", min_value=0.0, max_value=20.0, value=None, placeholder="Enter value (0-20)")
    with c3:
        deforestation = st.number_input("Deforestation", min_value=0.0, max_value=20.0, value=None, placeholder="Enter value (0-20)")
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="section-card"><div class="section-title">🏞️ Land & Water Management</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        topography = st.number_input("Topography Drainage", min_value=0.0, max_value=20.0, value=None, placeholder="Enter value (0-20)")
        siltation = st.number_input("Siltation", min_value=0.0, max_value=20.0, value=None, placeholder="Enter value (0-20)")
    with c2:
        river = st.number_input("River Management", min_value=0.0, max_value=20.0, value=None, placeholder="Enter value (0-20)")
        wetland = st.number_input("Wetland Loss", min_value=0.0, max_value=20.0, value=None, placeholder="Enter value (0-20)")
    with c3:
        dams = st.number_input("Dams Quality", min_value=0.0, max_value=20.0, value=None, placeholder="Enter value (0-20)")
        watersheds = st.number_input("Watersheds", min_value=0.0, max_value=20.0, value=None, placeholder="Enter value (0-20)")
    st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    st.markdown('<div class="section-card"><div class="section-title">🏙️ Infrastructure & Human Factors</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        urbanization = st.number_input("Urbanization", min_value=0.0, max_value=20.0, value=None, placeholder="Enter value (0-20)")
        agriculture = st.number_input("Agricultural Practices", min_value=0.0, max_value=20.0, value=None, placeholder="Enter value (0-20)")
    with c2:
        encroachments = st.number_input("Encroachments", min_value=0.0, max_value=20.0, value=None, placeholder="Enter value (0-20)")
        infrastructure = st.number_input("Deteriorating Infrastructure", min_value=0.0, max_value=20.0, value=None, placeholder="Enter value (0-20)")
    with c3:
        population = st.number_input("Population Score", min_value=0.0, max_value=20.0, value=None, placeholder="Enter value (0-20)")
        political = st.number_input("Political Factors", min_value=0.0, max_value=20.0, value=None, placeholder="Enter value (0-20)")
    st.markdown('</div>', unsafe_allow_html=True)

with tab4:
    st.markdown('<div class="section-card"><div class="section-title">🚨 Disaster Preparedness & Planning</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        disaster = st.number_input("Ineffective Disaster Preparedness", min_value=0.0, max_value=20.0, value=None, placeholder="Enter value (0-20)")
        drainage = st.number_input("Drainage Systems", min_value=0.0, max_value=20.0, value=None, placeholder="Enter value (0-20)")
    with c2:
        coastal = st.number_input("Coastal Vulnerability", min_value=0.0, max_value=20.0, value=None, placeholder="Enter value (0-20)")
        landslides = st.number_input("Landslides", min_value=0.0, max_value=20.0, value=None, placeholder="Enter value (0-20)")
    with c3:
        planning = st.number_input("Inadequate Planning", min_value=0.0, max_value=20.0, value=None, placeholder="Enter value (0-20)")
    st.markdown('</div>', unsafe_allow_html=True)

st.write("")
predict_clicked = st.button("🔍 Predict Flood Risk")

# ---------------------------------------------------------------------------
# VALIDATION — ensures every field is filled before prediction runs
# (does not alter the prediction logic itself, only guards entry to it)
# ---------------------------------------------------------------------------
all_inputs = {
    "Monsoon Intensity": monsoon, "Topography Drainage": topography, "River Management": river,
    "Deforestation": deforestation, "Urbanization": urbanization, "Climate Change": climate,
    "Dams Quality": dams, "Siltation": siltation, "Agricultural Practices": agriculture,
    "Encroachments": encroachments, "Ineffective Disaster Preparedness": disaster,
    "Drainage Systems": drainage, "Coastal Vulnerability": coastal, "Landslides": landslides,
    "Watersheds": watersheds, "Deteriorating Infrastructure": infrastructure,
    "Population Score": population, "Wetland Loss": wetland, "Inadequate Planning": planning,
    "Political Factors": political
}
missing_fields = [name for name, val in all_inputs.items() if val is None]

if predict_clicked and missing_fields:
    st.warning(f"⚠️ Please enter all values before predicting. Missing: {', '.join(missing_fields)}")

# ---------------------------------------------------------------------------
# PREDICTION LOGIC — UNCHANGED FROM ORIGINAL
# ---------------------------------------------------------------------------
if predict_clicked and not missing_fields:
    input_data = pd.DataFrame([[
        monsoon, topography, river, deforestation, urbanization,
        climate, dams, siltation, agriculture, encroachments,
        disaster, drainage, coastal, landslides, watersheds,
        infrastructure, population, wetland, planning, political
    ]], columns=[
        'MonsoonIntensity', 'TopographyDrainage', 'RiverManagement',
        'Deforestation', 'Urbanization', 'ClimateChange', 'DamsQuality',
        'Siltation', 'AgriculturalPractices', 'Encroachments',
        'IneffectiveDisasterPreparedness', 'DrainageSystems',
        'CoastalVulnerability', 'Landslides', 'Watersheds',
        'DeterioratingInfrastructure', 'PopulationScore', 'WetlandLoss',
        'InadequatePlanning', 'PoliticalFactors'
    ])

    prediction = model.predict(input_data)[0]
    prediction_percent = prediction * 100

    # Risk category
    if prediction < 0.45:
        risk_level = "🟢 LOW RISK"
        recommendation = """
        ✅ Flood risk is low.
        ✅ Continue normal activities.
        ✅ Keep monitoring weather updates.
        ✅ Maintain drainage systems properly.
        """
        accent = "#22c55e"

    elif prediction < 0.60:
        risk_level = "🟡 MEDIUM RISK"
        recommendation = """
        ⚠️ Moderate flood risk detected.
        ⚠️ Stay alert during heavy rainfall.
        ⚠️ Avoid unnecessary travel in flood-prone areas.
        ⚠️ Keep emergency supplies ready.
        """
        accent = "#eab308"

    else:
        risk_level = "🔴 HIGH RISK"
        recommendation = """
        🚨 High flood risk detected.
        🚨 Avoid low-lying and flood-prone areas.
        🚨 Keep emergency kit and important documents ready.
        🚨 Follow official weather and evacuation alerts.
        """
        accent = "#ef4444"

    # -----------------------------------------------------------------
    # RESULT DISPLAY — restyled presentation of the same computed values
    # -----------------------------------------------------------------
    st.markdown("---")
    st.markdown('<div class="section-title" style="font-size:1.3rem;">📊 Prediction Result</div>', unsafe_allow_html=True)

    r1, r2 = st.columns([1, 1.4])

    with r1:
        st.markdown(f"""
        <div class="result-card" style="border-left: 5px solid {accent};">
            <p class="prob-label">Flood Probability</p>
            <p class="prob-number">{prediction_percent:.1f}%</p>
            <p style="color:{accent}; font-weight:700; font-size:1.15rem; margin-top:0.6rem;">
                {risk_level}
            </p>
        </div>
        """, unsafe_allow_html=True)
        st.progress(float(min(max(prediction, 0.0), 1.0)))

    with r2:
        st.markdown(f"""
        <div class="result-card" style="border-left: 5px solid {accent};">
            <p class="prob-label">🤖 AI Safety Recommendation</p>
            <div style="color:#e2e8f0; font-size:0.98rem; line-height:1.9; margin-top:0.5rem; white-space:pre-line;">{recommendation}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('<div class="footer-note">Flood Guard · AI-Powered Flood Risk Prediction System</div>', unsafe_allow_html=True)