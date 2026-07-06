import streamlit as st

st.set_page_config(
    page_title="Developer",
    page_icon="👨‍💻",
    layout="wide"
)

st.title("👨‍💻 Developer")

st.markdown("""
This application was developed as an end-to-end machine learning project for
cardiovascular disease risk prediction using Deep Learning and Explainable AI.
""")

st.divider()

# ----------------------------------------------------------
# Developer
# ----------------------------------------------------------

st.subheader("👤 Developer")

st.info("""
**Name:** Achesomie Goni Yifieyeh

**Role:** AI & Machine Learning Engineer

**Project:** Cardiovascular Disease Prediction using Deep Neural Networks

**Country:** Nigeria
""")

st.divider()

# ----------------------------------------------------------
# Skills Demonstrated
# ----------------------------------------------------------

st.subheader("🛠 Skills Demonstrated")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
### Machine Learning

- Data Cleaning
- Feature Engineering
- Deep Neural Networks
- Model Evaluation
- Threshold Optimization
- External Validation
""")

with col2:

    st.markdown("""
### Software Development

- Python
- Streamlit
- TensorFlow / Keras
- Scikit-learn
- SHAP Explainability
- Plotly Visualization
""")

st.divider()

# ----------------------------------------------------------
# Project Workflow
# ----------------------------------------------------------

st.subheader("📌 Project Workflow")

st.markdown("""
1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis
4. Feature Engineering
5. Model Development
6. Hyperparameter Tuning
7. Model Evaluation
8. Threshold Optimization
9. External Validation (SAHeart Dataset)
10. Explainable AI (SHAP)
11. Streamlit Deployment
""")

st.divider()

# ----------------------------------------------------------
# Key Achievements
# ----------------------------------------------------------

st.subheader("🏆 Key Achievements")

st.success("""
✔ Built an end-to-end Deep Learning application.

✔ Engineered clinically meaningful cardiovascular features.

✔ Optimized classification threshold beyond the default 0.50.

✔ Performed external validation using an independent African dataset.

✔ Integrated Explainable AI (SHAP).

✔ Developed an interactive Streamlit dashboard.
""")

st.divider()

# ----------------------------------------------------------
# Contact
# ----------------------------------------------------------

st.subheader("📬 Contact")

st.markdown("""
If this project is being reviewed as part of an academic assessment or professional portfolio, please feel free to reach out.

**Email:** yifieyeha@gmail.com

**GitHub:** https://github.com/Achese-creator

**LinkedIn:** https://linkedin.com/in/maverickhoodie
""")

st.divider()

st.caption(
    "© 2026 Cardiovascular Disease Prediction Project | Built with Streamlit, TensorFlow, and SHAP"
)

from utils.footer import footer

footer()