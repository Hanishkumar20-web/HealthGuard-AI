# 🏥 HealthGuard AI

## AI-Powered Diabetes Risk Prediction System

HealthGuard AI is a Machine Learning-based web application that predicts the likelihood of diabetes using patient health parameters. The project is built using Python, Scikit-learn, and Streamlit, with Random Forest selected as the final prediction model after comparing multiple machine learning algorithms.

> **Version 1.0:** Diabetes Risk Prediction

---

## 📌 Project Overview

This application allows users to enter basic medical information such as glucose level, BMI, blood pressure, insulin level, and age. The trained machine learning model analyzes these inputs and predicts whether the patient is at risk of diabetes.

The application also displays:

- ✅ Diabetes Prediction
- 📊 Risk Probability
- 💡 Basic Health Recommendations

---

## 🚀 Features

- User-friendly Streamlit web application
- Machine Learning-based prediction
- Data preprocessing and cleaning
- Exploratory Data Analysis (EDA)
- Model comparison
- Random Forest prediction model
- Prediction probability
- Health recommendations
- Simple and responsive interface

---

## 🧠 Machine Learning Models Compared

The following models were trained and evaluated:

- Logistic Regression
- Decision Tree
- Random Forest ✅ (Selected Model)
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)

Random Forest achieved the best performance and was chosen for deployment.

---

## 📂 Dataset

**Dataset Name:** Pima Indians Diabetes Database

**Source:** UCI Machine Learning Repository

https://archive.ics.uci.edu/dataset/34/diabetes

### Dataset Features

- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age
- Outcome (Target)

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook

---

## 📁 Project Structure

```
HealthGuardAI/
│
├── app.py
├── diabetes.csv
├── healthguard_model.pkl
├── scaler.pkl
├── notebook.ipynb
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/HealthGuardAI.git
```

Move into the project folder

```bash
cd HealthGuardAI
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 📸 Application Preview

### Home Page

![Home](screenshots/homepage.png)

---

### Low Risk Prediction

![Low Risk](screenshots/low_risk.png)

---

### High Risk Prediction

![High Risk](screenshots/high_risk.png)
Example:

```
screenshots/homepage.png
screenshots/result.png
```

---

## 📈 Workflow

```
Dataset
      ↓
Data Cleaning
      ↓
EDA
      ↓
Feature Selection
      ↓
Train-Test Split
      ↓
Model Training
      ↓
Model Comparison
      ↓
Random Forest Selected
      ↓
Model Saving (.pkl)
      ↓
Streamlit Web Application
```

---

## ⚠️ Limitations

- The current prediction model is trained using the **Pima Indians Diabetes Dataset**, which contains records of adult female patients.
- Therefore, the current implementation is intended for educational purposes and reflects the scope of the training dataset.
- The application should **not** be used as a substitute for professional medical diagnosis.

---

## 🔮 Future Enhancements

- Support both male and female datasets
- Heart Disease Prediction
- Blood Pressure Prediction
- BMI Risk Analysis
- User Login System
- Report Generation (PDF)
- Cloud Deployment
- Doctor Recommendation System

---

## 👨‍💻 Developer

**Hanish Kumar**

B.Tech Computer Science & Engineering (AI & ML)

---

## 📜 License

This project is developed for educational and learning purposes.

---

## ⭐ If you like this project

Give this repository a ⭐ on GitHub.
