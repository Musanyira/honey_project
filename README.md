# 🐝 Honey Yield Production Prediction System

## 📌 Project Information

**Institution:** Eastern Africa Statistical Training Centre (EASTC)\
**Programme:** Bachelor of Data Science\
**Academic Year:** 2025/2026\
**Level:** Second Year\
**Course:** Machine Learning\
**Project Type:** Group Project

------------------------------------------------------------------------

## 📖 Project Overview

This project presents a Machine Learning-based system developed to
predict honey yield production using environmental factors, hive
characteristics, and colony health conditions.

The system estimates honey production (in kilograms) and provides a
predictive tool that can assist farmers and agricultural planners in
decision-making.

------------------------------------------------------------------------

## 🎯 Project Objectives

-   To design and implement a regression-based predictive model.
-   To compare multiple machine learning algorithms.
-   To evaluate model performance using statistical metrics.
-   To deploy the selected model using Streamlit.

------------------------------------------------------------------------

## 📊 Dataset Description

The dataset includes the following features:

### Environmental Factors

-   rainfall_mm\
-   avg_temperature\
-   humidity

### Hive & Colony Characteristics

-   num_hives\
-   hive_type (traditional / modern)\
-   colony_strength (weak / medium / strong)\
-   disease_status (yes / no)

### Farmer Management Practices

-   experience_years\
-   inspection_frequency

### Target Variable

-   honey_yield_kg

------------------------------------------------------------------------

## 🧠 Machine Learning Models Used

The following regression models were implemented and compared:

-   Linear Regression\
-   Decision Tree Regressor

### Evaluation Metrics

-   Mean Absolute Error (MAE)\
-   Mean Squared Error (MSE)\
-   R² Score

The final model was selected based on highest R² score and lowest error
values.

------------------------------------------------------------------------

## ⚙️ Project Structure

Project_work/ │ ├── app.py\
├── train_model.py\
├── honey_dataset.csv\
├── honey_model.pkl\
├── requirements.txt\
└── README.md

------------------------------------------------------------------------

## 🚀 How to Run the Project

### 1️⃣ Install Required Libraries

pip install -r requirements.txt

### 2️⃣ Train the Model (if needed)

python train_model.py

### 3️⃣ Run the Streamlit Application

streamlit run app.py

Open the provided local URL in your browser.

------------------------------------------------------------------------

## 🌍 Deployment

The application is built using Streamlit and can be deployed on: -
Streamlit Community Cloud\
- Render\
- Other cloud platforms supporting Python applications

------------------------------------------------------------------------

## 👥 Project Team

Developed by a group of students from: Eastern Africa Statistical
Training Centre (EASTC)\
Bachelor of Data Science\
Second Year (2025/2026)

------------------------------------------------------------------------

## 📌 Conclusion

The developed Honey Yield Production Prediction System demonstrates the
practical application of Machine Learning techniques in agricultural
productivity analysis. The project highlights model comparison,
evaluation, and deployment as essential components of the data science
workflow.
