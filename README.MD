# Predictive Maintenance AI Monitoring Platform

## 📌 Project Overview

This project is an end-to-end industrial AI system developed to predict potential machine failures using operational sensor data.

The platform combines machine learning, explainable AI, and a real-time Streamlit interface to simulate an enterprise-grade predictive maintenance solution.

The application uses:

* LightGBM for predictive maintenance modeling
* Streamlit for interactive web deployment
* SHAP Explainability for feature impact interpretation

The system predicts machine failure risk based on operational conditions and provides maintenance recommendations.

---

# 🎯 Objectives

* Build a predictive maintenance model
* Handle imbalanced data using SMOTE
* Improve model performance using hyperparameter tuning
* Create a real-time prediction platform
* Deploy the application using Streamlit
* Build an industrial monitoring workflow
* Add Explainable AI using SHAP
* Generate operational health indicators
* Simulate a production-ready AI deployment architecture

---

# 📂 Dataset

**Dataset Used**

AI4I 2020 Predictive Maintenance Dataset

### Input Features

* Machine Type
* Air Temperature [K]
* Process Temperature [K]
* Rotational Speed [rpm]
* Torque [Nm]
* Tool Wear [min]

### Target Variable

* Machine Failure

---

# ⚙️ Machine Learning Workflow

1. Data preprocessing
2. Exploratory Data Analysis (EDA)
3. Feature engineering
4. Class imbalance handling using SMOTE
5. Model training
6. Hyperparameter optimization
7. Threshold tuning
8. Cross-validation
9. SHAP explainability
10. Streamlit deployment

---

# 🧠 Feature Engineering

Engineered features include:

* Temperature Difference
* Load Factor
* Wear-Speed Ratio
* Estimated Machine Power

Additional preprocessing:

* Feature cleaning
* One-hot encoding
* Pipeline preprocessing
* Feature alignment

The engineered features improve predictive performance while SHAP explanations primarily focus on the original operational sensor values for industrial interpretability.

---

# 🤖 Models Evaluated

| Model                        |  Precision |     Recall |   F1 Score |
| ---------------------------- | ---------: | ---------: | ---------: |
| XGBoost (Default)            |     54.76% |     75.41% |     63.45% |
| XGBoost (Tuned)              |     51.72% |     73.77% |     60.81% |
| LightGBM (500 Estimators)    |     65.15% |     70.49% |     67.72% |
| LightGBM (Manual Tuning)     |     75.00% |     83.82% |     79.17% |
| **LightGBM (Random Search)** | **83.58%** | **82.35%** | **82.96%** |
| LightGBM (Calibrated)        |     75.00% |     83.82% |     79.17% |

---

# 🏆 Final Model Performance

The Random Search optimized LightGBM model was selected because it provides the best balance between precision and recall.

### Performance

* Precision: **83.58%**
* Recall: **82.35%**
* F1 Score: **82.96%**
* ROC-AUC: **~0.97**

---

# 📊 Model Evaluation

Evaluation metrics include:

* Precision
* Recall
* F1 Score
* Confusion Matrix
* ROC-AUC
* Stratified Cross Validation
* Threshold Optimization
* SHAP Explainability

---

# 📈 Explainable AI (SHAP)

The prediction system includes SHAP Explainability to provide transparent model decisions.

Key operational insights include:

* Tool wear significantly increases failure probability.
* Rotational speed strongly influences machine health.
* Temperature imbalance affects operational stability.
* Torque-related load contributes to machine stress.

The explainability layer improves trustworthiness and supports maintenance decision-making.

---

# 🖥️ System Architecture

```text
User
   │
   ▼
Streamlit Frontend
   │
   ▼
Prediction & Validation Layer
   │
   ▼
LightGBM Prediction Pipeline
   │
   ▼
SHAP Explainability
   │
   ▼
Prediction Results
```

---

# 🚀 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* LightGBM
* XGBoost
* SHAP
* Streamlit
* Joblib

---

# 📦 Project Structure

```text
Predictive_Maintenance_ML_Project/
│
├── app.py
├── predict.py
├── full_system.pkl
├── requirements.txt
├── README.md
├── Predictive_Maintenance_ML_Project.ipynb
└── screenshots/
```

---

# ▶️ Running the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

# 📦 Requirements

Main libraries:

* streamlit
* pandas
* numpy
* scikit-learn
* lightgbm
* xgboost
* shap
* joblib

---

# 🔍 Application Features

* Industrial-style prediction interface
* Input validation
* Product ID validation
* Machine failure prediction
* Failure probability estimation
* Health score calculation
* Risk categorization
* Maintenance recommendations
* SHAP-based Explainable AI

---

# 🚀 Future Improvements

* Power BI dashboards
* Docker deployment
* IoT sensor integration
* Real-time streaming
* Drift detection
* Predictive maintenance scheduling
* Alert notifications
* Digital Twin integration

---

# 📌 Key Highlights

✅ End-to-end Industrial AI workflow

✅ LightGBM predictive maintenance model

✅ Hyperparameter optimization

✅ Explainable AI using SHAP

✅ Streamlit deployment

✅ Health score and risk assessment

✅ Production-style modular architecture

---

# 👨‍💻 Author

**R. Purushothamansai**

Machine Learning | Data Science | Industrial AI | Predictive Analytics
