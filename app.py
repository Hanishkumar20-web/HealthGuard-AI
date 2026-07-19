import streamlit as st
import numpy as np
import joblib

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="HealthGuard AI",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------------
# Load Model
# -----------------------------
model = joblib.load("healthguard_model.pkl")
scaler = joblib.load("scaler.pkl")

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

/* Google Font */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"]{
    font-family:'Poppins',sans-serif;
}

/* Background */
.stApp{
    background: linear-gradient(135deg,#F4F9FF,#EAF6FF);
}

/* Remove Streamlit Header/Footer */
header{
    visibility:hidden;
}
footer{
    visibility:hidden;
}

/* Main Container */
.main .block-container{
    padding-top:2rem;
    padding-bottom:2rem;
    max-width:1200px;
}

/* Hero Card */
.hero{
    background:white;
    padding:35px;
    border-radius:20px;
    box-shadow:0px 8px 30px rgba(0,0,0,0.08);
    text-align:center;
    margin-bottom:30px;
}

.hero h1{
    color:#1565C0;
    font-size:48px;
    margin-bottom:10px;
}

.hero p{
    color:#607D8B;
    font-size:20px;
}

/* Card */
.card{
    background:white;
    padding:25px;
    border-radius:18px;
    box-shadow:0px 6px 25px rgba(0,0,0,.08);
    margin-bottom:20px;
}

/* Button */
.stButton>button{
    width:100%;
    height:60px;
    border:none;
    border-radius:15px;
    background:#1976D2;
    color:white;
    font-size:22px;
    font-weight:bold;
    transition:.3s;
}

.stButton>button:hover{
    background:#0D47A1;
    transform:scale(1.02);
}

/* Inputs */
.stNumberInput input{
    border-radius:12px;
}

/* Progress */
.stProgress > div > div{
    background:#1976D2;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Hero Section
# -----------------------------
st.markdown("""
<div class="hero">
<h1>🏥 HealthGuard AI</h1>
<p>AI-Powered Diabetes Risk Assessment System</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h3 style="color:#1565C0;">🩺 Patient Health Information</h3>
<p style="color:gray;">
Enter the patient's medical information below.
</p>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Input Fields
# -----------------------------

left,right = st.columns(2)

with left:

    pregnancies = st.number_input(
        "Pregnancies",
        min_value=0,
        max_value=20,
        value=0
    )

    glucose = st.number_input(
        "Glucose",
        min_value=0,
        max_value=300,
        value=120
    )

    blood_pressure = st.number_input(
        "Blood Pressure",
        min_value=0,
        max_value=200,
        value=70
    )

    skin = st.number_input(
        "Skin Thickness",
        min_value=0,
        max_value=100,
        value=20
    )

with right:

    insulin = st.number_input(
        "Insulin",
        min_value=0,
        max_value=900,
        value=80
    )

    bmi = st.number_input(
        "BMI",
        min_value=0.0,
        max_value=70.0,
        value=25.0
    )

    pedigree = st.number_input(
        "Diabetes Pedigree Function",
        min_value=0.0,
        max_value=3.0,
        value=0.50
    )

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=30
    )

st.write("")

predict = st.button("🔍 Predict Diabetes")
# ===========================================
# Prediction Section
# ===========================================

if predict:

    # Prepare Input Data
    patient_data = np.array([[
        pregnancies,
        glucose,
        blood_pressure,
        skin,
        insulin,
        bmi,
        pedigree,
        age
    ]])

    # Scale Input
    patient_scaled = scaler.transform(patient_data)

    # Prediction
    prediction = model.predict(patient_scaled)[0]

    # Probability
    probability = model.predict_proba(patient_scaled)

    diabetic_probability = probability[0][1] * 100

    non_diabetic_probability = probability[0][0] * 100

    st.markdown("<br>", unsafe_allow_html=True)

    # ===============================
    # Result Card
    # ===============================

    if prediction == 1:

        st.markdown(f"""
        <div style="
        background:#ffebee;
        border-left:8px solid #d32f2f;
        padding:25px;
        border-radius:18px;
        box-shadow:0px 6px 15px rgba(0,0,0,.08);
        ">

        <h2 style="color:#c62828;">
        ⚠ High Risk of Diabetes
        </h2>

        <h4>
        Probability : {diabetic_probability:.2f}%
        </h4>

        </div>
        """, unsafe_allow_html=True)

    else:

        st.markdown(f"""
        <div style="
        background:#e8f5e9;
        border-left:8px solid #2e7d32;
        padding:25px;
        border-radius:18px;
        box-shadow:0px 6px 15px rgba(0,0,0,.08);
        ">

        <h2 style="color:#2e7d32;">
        ✅ Low Risk of Diabetes
        </h2>

        <h4>
        Probability : {non_diabetic_probability:.2f}%
        </h4>

        </div>
        """, unsafe_allow_html=True)

    st.write("")

    # ===============================
    # Risk Meter
    # ===============================

    st.subheader("📊 Diabetes Risk Score")

    st.progress(int(diabetic_probability))

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Diabetes Risk",
            f"{diabetic_probability:.2f}%"
        )

    with col2:

        st.metric(
            "Healthy Probability",
            f"{non_diabetic_probability:.2f}%"
        )

    st.markdown("---")

    # ===============================
    # Health Recommendations
    # ===============================

    st.subheader("💡 Personalized Health Recommendations")

    if prediction == 1:

        st.warning("""
### Lifestyle Advice

✔ Consult a healthcare professional.

✔ Monitor blood glucose regularly.

✔ Reduce sugar and processed food.

✔ Walk or exercise for at least 30 minutes daily.

✔ Drink plenty of water.

✔ Maintain a healthy body weight.

✔ Schedule regular medical checkups.
""")

    else:

        st.success("""
### Healthy Lifestyle Tips

✔ Continue a balanced diet.

✔ Stay physically active.

✔ Drink enough water.

✔ Maintain a healthy BMI.

✔ Sleep 7–8 hours daily.

✔ Continue routine health checkups.

✔ Avoid excessive sugary foods.
""")

    st.markdown("---")
# ==========================================
# Additional Information
# ==========================================

with st.expander("📘 About HealthGuard AI"):

    st.markdown("""
### 🏥 HealthGuard AI

HealthGuard AI is an AI-powered diabetes risk prediction system developed using
Machine Learning.

This application predicts the likelihood of diabetes based on patient health
parameters.

### 🔬 Machine Learning Model

- Random Forest Classifier
- Data Preprocessing
- Feature Scaling
- Scikit-learn
- Streamlit Deployment

### 🧑‍💻 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib
""")

# ==========================================
# Dataset Information
# ==========================================

with st.expander("📂 Dataset Information"):

    st.info("""
Dataset Used:
Pima Indians Diabetes Database

Features:

• Pregnancies
• Glucose
• Blood Pressure
• Skin Thickness
• Insulin
• BMI
• Diabetes Pedigree Function
• Age

Target:

• Outcome
""")

# ==========================================
# Disclaimer
# ==========================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div style="
background:#FFF8E1;
padding:18px;
border-radius:15px;
border-left:8px solid #F9A825;
">

<h3 style="color:#F57F17;">
⚠ Medical Disclaimer
</h3>

<p style="font-size:17px;">

This application is developed for educational purposes only.

It should not be used as a replacement for professional
medical diagnosis, treatment, or advice.

Always consult a qualified healthcare professional.

</p>

</div>
""", unsafe_allow_html=True)

st.write("")

# ==========================================
# Footer
# ==========================================

st.markdown("---")

st.markdown("""
<div style="text-align:center;">

<h2 style="color:#1565C0;">
🏥 HealthGuard AI
</h2>

<p style="font-size:18px;">
Version 1.0
</p>

<p>
AI-Powered Diabetes Risk Assessment System
</p>

<p style="color:gray;">
Developed by <b>Hanish Kumar</b><br>
B.Tech CSE (AI & ML)
</p>

</div>
""", unsafe_allow_html=True)

st.markdown(
    "<center><b>Built with Python • Scikit-learn • Streamlit</b></center>",
    unsafe_allow_html=True
)
