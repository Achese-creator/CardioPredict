import streamlit as st

st.set_page_config(
    page_title="About Project",
    page_icon="📚",
    layout="wide"
)

st.title("📚 About the Project")

st.markdown("""
This application predicts the likelihood of **cardiovascular disease** using a
Deep Neural Network (DNN) trained on clinical and lifestyle information.

The project demonstrates an end-to-end machine learning workflow, including data
preprocessing, feature engineering, model development, threshold optimization,
external validation, explainable AI, and deployment through Streamlit.
""")

st.divider()

# ==========================================================
# Project Objective
# ==========================================================

st.subheader("🎯 Project Objective")

st.write("""
The objective of this project is to develop an intelligent clinical decision
support system capable of estimating cardiovascular disease risk using routinely
collected patient information.

The system is intended to assist healthcare professionals by providing an
additional risk assessment tool and should not replace professional medical
judgement.
""")

st.divider()

# ==========================================================
# Dataset
# ==========================================================

st.subheader("🗄 Dataset")

c1, c2 = st.columns(2)

with c1:

    st.info("""
### CardioTrain Dataset

- 68,596 patients
- 14 predictive features
- Binary classification
- Used for model training and testing
""")

with c2:

    st.info("""
### SAHeart Dataset

- 462 patients
- South African cohort
- Used exclusively for external validation
- Evaluates model generalizability
""")

st.divider()

# ==========================================================
# Input Features
# ==========================================================

st.subheader("📋 Model Input Features")

features = [
    "Age",
    "Gender",
    "Height",
    "Weight",
    "Systolic Blood Pressure",
    "Diastolic Blood Pressure",
    "Cholesterol",
    "Glucose",
    "Smoking",
    "Alcohol Intake",
    "Physical Activity",
    "Body Mass Index (BMI)",
    "Pulse Pressure",
    "Mean Arterial Pressure (MAP)"
]

st.markdown("\n".join([f"- {feature}" for feature in features]))

st.divider()

# ==========================================================
# Feature Engineering
# ==========================================================

st.subheader("⚙️ Feature Engineering")

st.success("""
Three clinically meaningful variables were engineered from the original dataset:

• Body Mass Index (BMI)

• Pulse Pressure

• Mean Arterial Pressure (MAP)

These engineered features improved the amount of cardiovascular information
available to the Deep Neural Network.
""")

st.divider()

# ==========================================================
# Deep Neural Network
# ==========================================================

st.subheader("🧠 Deep Neural Network Architecture")

st.code("""
Input Layer (14 Features)

↓

Dense (128) + ReLU

↓

Batch Normalization

↓

Dropout

↓

Dense (64) + ReLU

↓

Batch Normalization

↓

Dropout

↓

Dense (32) + ReLU

↓

Output Layer (Sigmoid)
""")

st.divider()

# ==========================================================
# Model Performance
# ==========================================================

st.subheader("📈 Final Model Performance")

m1, m2, m3, m4, m5 = st.columns(5)

with m1:
    st.metric("Accuracy", "72.0%")

with m2:
    st.metric("Precision", "68.9%")

with m3:
    st.metric("Recall", "79.0%")

with m4:
    st.metric("F1 Score", "73.6%")

with m5:
    st.metric("ROC AUC", "0.799")

st.divider()

# ==========================================================
# Threshold Optimization
# ==========================================================

st.subheader("🎯 Threshold Optimization")

st.write("""
Instead of using the conventional decision threshold of **0.50**, multiple
thresholds were evaluated.

A threshold of **0.40** produced the best balance between Precision, Recall,
and F1 Score and was therefore selected for deployment.
""")

st.divider()

# ==========================================================
# External Validation
# ==========================================================

st.subheader("🌍 External Validation")

st.write("""
The trained Deep Neural Network was evaluated using the independent South African
Heart Disease (SAHeart) dataset.

External validation demonstrated moderate predictive performance despite
differences in patient demographics, available variables, and disease prevalence,
indicating reasonable generalizability to another African population.
""")

st.divider()

# ==========================================================
# Technologies Used
# ==========================================================

st.subheader("🛠 Technologies Used")

tech1, tech2 = st.columns(2)

with tech1:

    st.markdown("""
- Python
- TensorFlow / Keras
- Scikit-learn
- Pandas
- NumPy
""")

with tech2:

    st.markdown("""
- Streamlit
- Plotly
- SHAP
- Joblib
- Matplotlib
""")

st.divider()

# ==========================================================
# Future Improvements
# ==========================================================

st.subheader("🚀 Future Improvements")

st.markdown("""
- Multi-class cardiovascular risk prediction
- Integration with electronic health records (EHRs)
- Real-time SHAP explanations
- Longitudinal patient monitoring
- Mobile application deployment
- Clinical validation using prospective datasets
""")

from utils.footer import footer

footer()