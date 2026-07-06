import streamlit as st

# -------------------------------------------------------
# Page Configuration
# -------------------------------------------------------

st.set_page_config(
    page_title="Cardiovascular Disease Prediction System",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------------
# Load CSS
# -------------------------------------------------------

def load_css():

    with open("assets/styles.css") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

def info_card(icon, title, value, color="#1976D2"):

    st.markdown(
        f"""
        <div style="
            background:white;
            border-radius:18px;
            padding:25px;
            box-shadow:0 4px 15px rgba(0,0,0,.08);
            border-left:8px solid {color};
            margin-bottom:15px;
        ">

        <h1 style="margin:0">{icon}</h1>

        <h4 style="margin-bottom:0">{title}</h4>

        <h2 style="color:{color};margin-top:5px">
            {value}
        </h2>

        </div>
        """,
        unsafe_allow_html=True
    )

# -------------------------------------------------------
# Hero Section
st.subheader("📊 Model Overview")

c1,c2,c3,c4 = st.columns(4)

with c1:
    info_card(
        "👥",
        "Training Samples",
        "68,596",
        "#1976D2"
    )

with c2:
    info_card(
        "🎯",
        "Accuracy",
        "73.2%",
        "#2E7D32"
    )

with c3:
    info_card(
        "📈",
        "ROC AUC",
        "0.799",
        "#EF6C00"
    )

with c4:
    info_card(
        "🌍",
        "Validation",
        "SAHeart",
        "#D32F2F"
    )
    
st.divider()

left, right = st.columns(2)

with left:

    st.subheader("⚙ Technology Stack")

    st.success("""
**Machine Learning**

• TensorFlow / Keras

• Deep Neural Network

• Scikit-Learn

• SHAP Explainability
""")

    st.info("""
**Application**

• Streamlit

• Python

• Pandas

• NumPy
""")

with right:

    st.subheader("🧠 Deep Neural Network")

    st.code("""
Input Layer (14 Features)
        │
        ▼
Dense (128)
        │
Batch Normalization
        │
Dropout (0.3)
        │
Dense (64)
        │
Batch Normalization
        │
Dropout (0.3)
        │
Dense (32)
        │
        ▼
Output Layer
""")
    
st.divider()

st.subheader("🔄 Prediction Workflow")

st.code("""
Patient Clinical Data
        │
        ▼
Feature Engineering
(BMI • Pulse Pressure • MAP)
        │
        ▼
StandardScaler
        │
        ▼
Deep Neural Network
        │
        ▼
Risk Probability
        │
        ▼
Clinical Interpretation
""")

st.divider()

st.subheader("✨ Project Highlights")

col1, col2 = st.columns(2)

with col1:

    st.success("""
✔ Deep Neural Network

✔ Feature Engineering

✔ Explainable AI (SHAP)

✔ External Validation
""")

with col2:

    st.success("""
✔ Interactive Dashboard

✔ Real-Time Predictions

✔ Clinical Risk Interpretation

✔ Streamlit Deployment
""")
# -------------------------------------------------------

st.title("❤️ Cardiovascular Disease Prediction System")

st.divider()
st.warning(
"""
### Deep Neural Network for Early Cardiovascular Disease Detection

This application predicts the likelihood of cardiovascular disease using a
Deep Neural Network trained on over **68,000 patient records**.

The model incorporates demographic, clinical, lifestyle, and engineered
health indicators to provide accurate cardiovascular risk assessment.

Navigate through the sidebar to perform predictions, explore model
performance, and understand how the model reaches its decisions.
"""
)

st.divider()