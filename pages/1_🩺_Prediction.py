import streamlit as st
import pandas as pd

from utils.prediction import predict
from utils.pdf_report import create_pdf

from utils.calculations import (
    calculate_bmi,
    calculate_map,
    calculate_pulse_pressure,
    bmi_category,
    bp_category
)

from utils.constants import (
    GENDER,
    CHOLESTEROL,
    GLUCOSE,
    YES_NO
)

from utils.footer import footer


# ======================================================
# PAGE HEADER
# ======================================================

st.title("🩺 CardioPredict")

st.caption(
    "Deep Neural Network for Cardiovascular Disease Risk Prediction"
)

st.info(
    """
This application estimates an individual's likelihood of cardiovascular disease using a
Deep Neural Network trained on demographic, clinical, lifestyle, and engineered health features.

The prediction is intended to support clinical decision-making and educational research.
"""
)

st.divider()

with st.expander("ℹ️ About the Prediction Model"):

    st.markdown(
        """
### Model Information

- **Algorithm:** Deep Neural Network (TensorFlow/Keras)

- **Input Features:** 14 clinical and lifestyle variables

- **Engineered Features**
    - BMI
    - Pulse Pressure
    - Mean Arterial Pressure

- **Internal ROC-AUC:** **0.799**

- **External Validation:** South African Heart Disease Dataset
"""
    )
# ======================================================
# PATIENT INFORMATION
# ======================================================

left_col, right_col = st.columns([1, 1.2], gap="large")

with left_col:

    st.subheader("Patient Information")

    age = st.number_input(
        "Age (Years)",
        min_value=18.0,
        max_value=100.0,
        value=50.0
    )

    gender = st.selectbox(
        "Gender",
        list(GENDER.keys())
    )

    height = st.number_input(
        "Height (cm)",
        min_value=120.0,
        max_value=220.0,
        value=170.0
    )

    weight = st.number_input(
        "Weight (kg)",
        min_value=30.0,
        max_value=200.0,
        value=70.0
    )

with right_col:

    st.subheader("Clinical Measurements")

    ap_hi = st.number_input(
        "Systolic Blood Pressure",
        min_value=80.0,
        max_value=250.0,
        value=120.0
    )

    ap_lo = st.number_input(
        "Diastolic Blood Pressure",
        min_value=40.0,
        max_value=180.0,
        value=80.0
    )

    cholesterol = st.selectbox(
        "Cholesterol Level",
        list(CHOLESTEROL.keys())
    )

    gluc = st.selectbox(
        "Glucose Level",
        list(GLUCOSE.keys())
    )

st.divider()

# ======================================================
# LIFESTYLE
# ======================================================

st.subheader("Lifestyle Information")

c1, c2, c3 = st.columns(3)

with c1:

    smoke = st.selectbox(
        "Smoking",
        list(YES_NO.keys())
    )

with c2:

    alco = st.selectbox(
        "Alcohol Intake",
        list(YES_NO.keys())
    )

with c3:

    active = st.selectbox(
        "Physically Active",
        list(YES_NO.keys())
    )

st.divider()

predict_btn = st.button(
    "🔍 Assess Cardiovascular Risk",
    use_container_width=True
)

# ======================================================
# PREDICTION
# ======================================================

if predict_btn:

        # ======================================================
    # INPUT VALIDATION
    # ======================================================

    if ap_hi <= ap_lo:

        st.error(
            "Systolic blood pressure must be greater than diastolic blood pressure."
        )

        st.stop()

    # ======================================================
    # DERIVED CLINICAL FEATURES
    # ======================================================

    bmi = calculate_bmi(
        weight,
        height
    )

    pulse_pressure = calculate_pulse_pressure(
        ap_hi,
        ap_lo
    )

    map_value = calculate_map(
        ap_hi,
        ap_lo
    )

    bmi_class = bmi_category(
        bmi
    )

    bp_class = bp_category(
        ap_hi,
        ap_lo
    )

    # ======================================================
    # CREATE MODEL INPUT
    # ======================================================

    patient = pd.DataFrame([{

        "age": age,

        "gender": GENDER[gender],

        "height": height,

        "weight": weight,

        "ap_hi": ap_hi,

        "ap_lo": ap_lo,

        "cholesterol": CHOLESTEROL[cholesterol],

        "gluc": GLUCOSE[gluc],

        "smoke": YES_NO[smoke],

        "alco": YES_NO[alco],

        "active": YES_NO[active],

        "BMI": bmi,

        "PulsePressure": pulse_pressure,

        "MAP": map_value

    }])

    # ======================================================
    # MODEL PREDICTION
    # ======================================================

    prediction, probability = predict(patient)

    # ======================================================
    # DETERMINE RISK CATEGORY
    # ======================================================

    if probability < 0.40:

        risk_level = "Low Risk"

    elif probability < 0.70:

        risk_level = "Moderate Risk"

    else:

        risk_level = "High Risk"

    # ======================================================
    # GENERATE PDF REPORT
    # ======================================================

    patient_data = {

        "age": age,

        "gender": gender,

        "height": height,

        "weight": weight,

        "ap_hi": ap_hi,

        "ap_lo": ap_lo

    }

    pdf = create_pdf(

        patient_data=patient_data,

        probability=probability,

        risk_level=risk_level,

        bmi=bmi,

        bmi_class=bmi_class,

        pulse_pressure=pulse_pressure,

        map_value=map_value,

        bp_class=bp_class

    )
    
        # ======================================================
    # RESULTS
    # ======================================================

    st.divider()

    st.subheader("📊 Prediction Results")

    st.metric(
        "Estimated Probability of Cardiovascular Disease",
        f"{probability*100:.1f}%"
    )

    st.progress(float(probability))

    # ======================================================
    # RISK CATEGORY
    # ======================================================

    if risk_level == "Low Risk":

        st.success(
            "🟢 Low Risk of Cardiovascular Disease"
        )

    elif risk_level == "Moderate Risk":

        st.warning(
            "🟡 Moderate Risk of Cardiovascular Disease"
        )

    else:

        st.error(
            "🔴 High Risk of Cardiovascular Disease"
        )

    # ======================================================
    # PATIENT SUMMARY
    # ======================================================

    st.divider()

    st.subheader("👤 Patient Summary")

    col1, col2 = st.columns(2)

    with col1:

        st.write(f"**Age:** {age:.0f} years")

        st.write(f"**Gender:** {gender}")

        st.write(f"**Height:** {height:.0f} cm")

        st.write(f"**Weight:** {weight:.0f} kg")

    with col2:

        st.write(
            f"**Blood Pressure:** {ap_hi:.0f}/{ap_lo:.0f} mmHg"
        )

        st.write(
            f"**BMI:** {bmi:.2f} ({bmi_class})"
        )

        st.write(
            f"**Blood Pressure Category:** {bp_class}"
        )

    # ======================================================
    # DERIVED CLINICAL FEATURES
    # ======================================================

    st.divider()

    st.subheader("🧮 Derived Clinical Measurements")

    a, b, c = st.columns(3)

    with a:

        st.metric(
            "BMI",
            f"{bmi:.2f}"
        )

    with b:

        st.metric(
            "Pulse Pressure",
            f"{pulse_pressure:.1f} mmHg"
        )

    with c:

        st.metric(
            "Mean Arterial Pressure",
            f"{map_value:.1f} mmHg"
        )

    # ======================================================
    # PDF DOWNLOAD
    # ======================================================

    st.divider()

    st.download_button(

        label="📄 Download Patient Report",

        data=pdf,

        file_name="CardioPredict_Report.pdf",

        mime="application/pdf",

        use_container_width=True

    )
    
        # ======================================================
    # CLINICAL INTERPRETATION
    # ======================================================

    st.divider()

    with st.expander(
        "🩺 Clinical Interpretation",
        expanded=True
    ):

        if prediction == 1:

            st.warning(
                """
The Deep Neural Network predicts that this patient has an **elevated likelihood of cardiovascular disease**.

This prediction is based on demographic characteristics, blood pressure measurements, metabolic indicators, lifestyle factors, and engineered clinical features.

This tool is intended to support clinical decision-making and **should not replace professional medical judgement**.
"""
            )

        else:

            st.success(
                """
The Deep Neural Network predicts that this patient has a **relatively low likelihood of cardiovascular disease**.

Although the estimated risk is low, maintaining healthy lifestyle habits and attending routine medical check-ups remain important for long-term cardiovascular health.
"""
            )

    # ======================================================
    # EXTERNAL VALIDATION
    # ======================================================

    st.divider()

    st.subheader("🌍 External Validation")

    st.info(
        """
This model was externally evaluated using the **South African Heart Disease (SAHeart)** dataset to assess its ability to generalize to an independent African population.

### Performance on the External Dataset

- **Accuracy:** 57.1%
- **Precision:** 43.2%
- **Recall:** 75.6%
- **F1-Score:** 55.0%
- **ROC-AUC:** 0.664

These results indicate that although predictive performance declined compared with the internal CardioTrain test set, the model retained **moderate discriminatory ability** on unseen data collected from a different African population. This demonstrates reasonable generalization while highlighting the importance of external validation and potential future retraining using more diverse datasets.
"""
    )

    # ======================================================
    # DISCLAIMER
    # ======================================================

    st.divider()

    st.warning(
        """
**Clinical Disclaimer**

This application is intended for **educational and research purposes**.

Predictions are generated using a Deep Neural Network trained on cardiovascular risk factors and should be interpreted alongside comprehensive clinical evaluation.

The application **must not** be used as the sole basis for diagnosis or treatment decisions.
"""
    )

    # ======================================================
    # NEW ASSESSMENT
    # ======================================================

    st.divider()

    if st.button(
        "🆕 Start New Assessment",
        use_container_width=True
    ):

        st.rerun()


# ======================================================
# FOOTER
# ======================================================

footer()