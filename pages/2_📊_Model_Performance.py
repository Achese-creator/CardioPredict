import streamlit as st
import joblib
import pandas as pd
import plotly.graph_objects as go

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    classification_report,
    roc_curve
)

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="Model Performance",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Model Performance Dashboard")

st.markdown("""
This dashboard presents the evaluation results of the Deep Neural Network
on the internal CardioTrain test set and compares them with external
validation results obtained using the South African Heart Disease (SAHeart) dataset.
""")

st.divider()

# ---------------------------------------------------
# Load Saved Predictions
# ---------------------------------------------------

y_test = joblib.load("models/y_test.pkl")
y_prob = joblib.load("models/y_prob.pkl")

# Threshold selected during model evaluation
THRESHOLD = 0.40

y_pred = (y_prob >= THRESHOLD).astype(int)

# ---------------------------------------------------
# Performance Metrics
# ---------------------------------------------------

accuracy = accuracy_score(y_test, y_pred)

precision = precision_score(y_test, y_pred)

recall = recall_score(y_test, y_pred)

f1 = f1_score(y_test, y_pred)

auc = roc_auc_score(y_test, y_prob)
st.subheader("📈 Performance Overview")

c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    st.metric("Accuracy", f"{accuracy:.3f}")

with c2:
    st.metric("Precision", f"{precision:.3f}")

with c3:
    st.metric("Recall", f"{recall:.3f}")

with c4:
    st.metric("F1 Score", f"{f1:.3f}")

with c5:
    st.metric("ROC AUC", f"{auc:.3f}")

st.divider()
st.subheader("📉 Confusion Matrix")

cm = confusion_matrix(y_test, y_pred)

fig = go.Figure(
    data=go.Heatmap(
        z=cm,
        x=["Predicted No", "Predicted Yes"],
        y=["Actual No", "Actual Yes"],
        text=cm,
        texttemplate="%{text}",
        colorscale="Blues"
    )
)

fig.update_layout(
    height=450,
    xaxis_title="Predicted Class",
    yaxis_title="Actual Class"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()
st.subheader("📈 ROC Curve")

fpr, tpr, _ = roc_curve(
    y_test,
    y_prob
)

roc = go.Figure()

roc.add_trace(

    go.Scatter(

        x=fpr,

        y=tpr,

        mode="lines",

        name=f"DNN (AUC = {auc:.3f})"

    )

)

roc.add_trace(

    go.Scatter(

        x=[0,1],

        y=[0,1],

        mode="lines",

        name="Random Classifier",

        line=dict(dash="dash")

    )

)

roc.update_layout(

    height=500,

    xaxis_title="False Positive Rate",

    yaxis_title="True Positive Rate"

)

st.plotly_chart(
    roc,
    use_container_width=True
)

st.divider()
# ---------------------------------------------------
# Classification Report
# ---------------------------------------------------

st.subheader("📋 Classification Report")

report = classification_report(
    y_test,
    y_pred,
    output_dict=True
)

report_df = pd.DataFrame(report).transpose()

st.dataframe(
    report_df.style.format("{:.3f}"),
    use_container_width=True
)

st.divider()
# ---------------------------------------------------
# Internal vs External Validation
# ---------------------------------------------------

st.subheader("🌍 Internal vs External Validation")

comparison = pd.DataFrame({

    "Metric":[
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score",
        "ROC AUC"
    ],

    "CardioTrain Test":[
        0.720,
        0.689,
        0.790,
        0.736,
        0.799
    ],

    "SAHeart External":[
        0.571,
        0.432,
        0.756,
        0.550,
        0.664
    ]

})

st.dataframe(
    comparison.style.format({
        "CardioTrain Test": "{:.3f}",
        "SAHeart External": "{:.3f}",
    }),
    use_container_width=True
)

st.divider()
# ---------------------------------------------------
# Threshold Analysis
# ---------------------------------------------------

st.subheader("🎯 Threshold Analysis")

threshold_df = pd.DataFrame({

    "Threshold":[0.30,0.40,0.50,0.60,0.70],

    "Accuracy":[
        0.671,
        0.720,
        0.732,
        0.729,
        0.714
    ],

    "Precision":[
        0.617,
        0.689,
        0.745,
        0.798,
        0.824
    ],

    "Recall":[
        0.886,
        0.790,
        0.697,
        0.605,
        0.537
    ],

    "F1 Score":[
        0.727,
        0.736,
        0.720,
        0.688,
        0.650
    ]

})

st.dataframe(
    threshold_df.style.format("{:.3f}"),
    use_container_width=True
)

st.info(
"""
**Selected Decision Threshold: 0.40**

Although the conventional probability threshold for binary classification is 0.50, empirical evaluation showed that a threshold of **0.40** achieved the best balance between Precision, Recall, and F1 Score. This threshold was therefore adopted for the deployed model.
"""
)

st.divider()
# ---------------------------------------------------
# Interpretation
# ---------------------------------------------------

st.subheader("📝 Interpretation of Results")

st.markdown(
"""
### Internal Performance

The Deep Neural Network demonstrated **good discriminative ability** on the CardioTrain test dataset, achieving a **ROC-AUC of 0.799**. Using the optimized probability threshold of **0.40**, the model achieved a balanced trade-off between precision and recall, making it well suited for cardiovascular disease screening.

### External Validation

When evaluated on the independent South African Heart Disease (SAHeart) dataset, the model achieved a **ROC-AUC of 0.664**. Although overall accuracy decreased, recall remained relatively high (75.6%), indicating that the model continued to identify a substantial proportion of patients with cardiovascular disease despite differences in population characteristics and available clinical variables.

### Overall Assessment

The observed reduction in performance between the internal and external datasets is expected due to domain shift, including differences in patient demographics, feature distributions, and dataset composition. Nevertheless, the model maintained moderate predictive capability, demonstrating reasonable generalizability to an independent African cohort.
"""
)

st.divider()
# ---------------------------------------------------
# Key Findings
# ---------------------------------------------------

st.subheader("⭐ Key Findings")

col1, col2 = st.columns(2)

with col1:

    st.success(
"""
### Strengths

- Deep Neural Network architecture

- Large training dataset (68,596 patients)

- Engineered clinical features

- Optimized decision threshold

- External validation performed

- Good ROC-AUC (0.799)
"""
    )

with col2:

    st.warning(
"""
### Limitations

- External dataset contained fewer variables

- Smaller external sample size

- Domain shift between datasets

- Performance decreased during external validation

- Intended for decision support rather than clinical diagnosis
"""
    )

from utils.footer import footer

footer()