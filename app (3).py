import streamlit as st
import joblib
import numpy as np

st.set_page_config(
    page_title="HealthGuard AI",
    page_icon="🏥",
    layout="wide"
)

# Load CSS
st.markdown("""
<style>

/* Background */
.stApp{
    background: linear-gradient(135deg,#F5FAFF,#EAF4FF);
}

/* Main Title */
.main-title{
    text-align:center;
    font-size:48px;
    font-weight:bold;
    color:#1565C0;
}

/* Subtitle */
.sub-title{
    text-align:center;
    font-size:20px;
    color:#607D8B;
    margin-bottom:30px;
}

/* Button */
.stButton > button{
    width:100%;
    height:55px;
    background:#1976D2;
    color:white;
    border:none;
    border-radius:12px;
    font-size:20px;
    font-weight:bold;
}

.stButton > button:hover{
    background:#0D47A1;
    color:white;
}

/* Input boxes */
.stNumberInput input{
    border-radius:10px;
}

/* Hide Streamlit footer */
footer{
    visibility:hidden;
}

</style>
""", unsafe_allow_html=True)

# Load Model
model = joblib.load("healthguard_model.pkl")
scaler = joblib.load("scaler.pkl")

# ---------------- Sidebar ----------------

st.sidebar.image("https://img.icons8.com/color/96/stethoscope.png", width=80)

st.sidebar.title("HealthGuard AI")

st.sidebar.markdown("---")

st.sidebar.write("### Project")

st.sidebar.success("AI Powered Diabetes Prediction")

st.sidebar.markdown("---")

st.sidebar.write("### Model Used")

st.sidebar.info("Random Forest")

st.sidebar.markdown("---")

st.sidebar.write("Developed by")

st.sidebar.write("Hanish Kumar")

st.sidebar.write("B.Tech CSE (AI & ML)")

# ---------------- Main ----------------

st.markdown(
"<div class='main-title'>🏥 HealthGuard AI</div>",
unsafe_allow_html=True)

st.markdown(
"<div class='sub-title'>AI Powered Diabetes Risk Assessment System</div>",
unsafe_allow_html=True)

st.info(
"Enter the patient's medical values below to estimate diabetes risk."
)

left,right=st.columns(2)

with left:

    pregnancies=st.number_input("Pregnancies",0,20,0)

    glucose=st.number_input("Glucose",0,300,120)

    blood_pressure=st.number_input("Blood Pressure",0,200,70)

    skin=st.number_input("Skin Thickness",0,100,20)

with right:

    insulin=st.number_input("Insulin",0,900,80)

    bmi=st.number_input("BMI",0.0,70.0,25.0)

    pedigree=st.number_input(
        "Diabetes Pedigree Function",
        0.0,
        3.0,
        0.5
    )

    age=st.number_input("Age",1,120,30)

st.markdown("")

if st.button("🔍 Predict Diabetes"):

    patient=np.array([[

        pregnancies,
        glucose,
        blood_pressure,
        skin,
        insulin,
        bmi,
        pedigree,
        age

    ]])

    patient=scaler.transform(patient)

    prediction=model.predict(patient)

    probability=model.predict_proba(patient)

    risk=probability[0][1]*100

    st.markdown("---")

    c1,c2=st.columns([2,1])

    with c1:

        if prediction[0]==1:

            st.error("⚠ High Risk of Diabetes")

        else:

            st.success("✅ Low Risk of Diabetes")

        st.progress(int(risk))

        st.write(f"### Risk Probability : {risk:.2f}%")

    with c2:

        st.metric(
            label="Risk Score",
            value=f"{risk:.1f}%"
        )

    st.markdown("---")

    st.subheader("💡 Health Recommendations")

    if prediction[0]==1:

        st.warning("""

• Consult a doctor.

• Monitor glucose regularly.

• Exercise daily.

• Reduce sugar intake.

• Maintain healthy BMI.

""")

    else:

        st.success("""

• Continue healthy lifestyle.

• Eat balanced meals.

• Stay physically active.

• Routine health checkups.

""")

st.markdown("---")

st.caption(
"This tool is intended for educational purposes only and does not replace professional medical advice."
)