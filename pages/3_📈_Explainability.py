import streamlit as st

st.set_page_config(
    page_title="Explainability",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Explainable Artificial Intelligence (XAI)")

st.markdown("""
This page explains how the Deep Neural Network arrives at its predictions using
**SHapley Additive exPlanations (SHAP)**.

SHAP is a model-agnostic explainability technique that quantifies the contribution
of each input feature to the model's prediction, thereby improving transparency
and interpretability.
""")

st.divider()

# ==========================================================
# What is SHAP?
# ==========================================================

st.subheader("📖 What is SHAP?")

st.info(
"""
SHAP (SHapley Additive exPlanations) is an explainable AI technique based on
cooperative game theory.

Rather than treating the neural network as a "black box", SHAP estimates the
contribution of every feature toward increasing or decreasing the predicted
cardiovascular disease risk.
"""
)

st.divider()

# ==========================================================
# Global Feature Importance
# ==========================================================

st.subheader("📊 Global Feature Importance")

st.image(
    "assets/images/shap_bar.png",
    use_container_width=True
)

st.markdown(
"""
The SHAP bar plot ranks features according to their **average absolute contribution**
to model predictions across all patients.

Features positioned at the top have the greatest overall influence on the Deep Neural
Network's decision-making process.
"""
)

st.divider()

# ==========================================================
# SHAP Summary Plot
# ==========================================================

st.subheader("📈 SHAP Summary Plot")

st.image(
    "assets/images/shap_summary.png",
    use_container_width=True
)

st.markdown(
"""
The SHAP summary plot illustrates both the **importance** and **direction** of each
feature's influence.

- Features are ordered from most to least important.
- Each point represents an individual patient.
- Red indicates higher feature values.
- Blue indicates lower feature values.
- Movement to the right increases predicted cardiovascular disease risk.
- Movement to the left decreases predicted risk.
"""
)

st.divider()

# ==========================================================
# Clinical Interpretation
# ==========================================================

st.subheader("🩺 Clinical Interpretation")

st.success(
"""
The explainability analysis demonstrates that the Deep Neural Network primarily
relies on clinically meaningful variables such as blood pressure measurements,
age, cholesterol status, Body Mass Index (BMI), Mean Arterial Pressure (MAP),
and Pulse Pressure when estimating cardiovascular disease risk.

The prominence of these variables aligns with established cardiovascular risk
factors reported in the medical literature, providing additional confidence
that the model is learning clinically relevant patterns rather than spurious
associations.
"""
)

st.divider()

# ==========================================================
# Why Explainability Matters
# ==========================================================

st.subheader("🎯 Why Explainability Matters")

st.markdown(
"""
Explainable AI is particularly important in healthcare because it:

- Improves transparency of machine learning predictions.
- Increases clinician confidence in model outputs.
- Helps identify the most influential clinical variables.
- Supports responsible adoption of AI in clinical decision-making.
- Reduces reliance on opaque "black-box" predictions.
"""
)

st.divider()

# ==========================================================
# Disclaimer
# ==========================================================

st.warning(
"""
**Disclaimer**

SHAP explanations describe how the trained Deep Neural Network arrived at its
predictions. They should not be interpreted as establishing causal relationships
between clinical variables and cardiovascular disease.
"""
)

from utils.footer import footer

footer()