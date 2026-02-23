🚗 Used Car Price Prediction

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Scikit-Learn](https://img.shields.io/badge/ML-RandomForest-green)

A Machine Learning web application built using Streamlit that predicts used car prices.
📌 Project Overview

This project uses a Random Forest Regressor to predict used car prices based on features like:

Car Age

Present Price

Kilometers Driven

Fuel Type

Seller Type

Transmission Type

Owner History

The model is trained using Scikit-learn and deployed using Streamlit.

🛠 Tech Stack

Python

Pandas

NumPy

Scikit-learn

Streamlit

Joblib

📂 Project Structure
UsedCarProject/
│
├── app.py                # Streamlit web app
├── train_model.py        # Model training script
├── README.md
├── requirements.txt
│
├── data/
│   └── car data.csv
│
└── model/
    ├── model.pkl
    └── features.pkl

⚙️ Model Details

Algorithm: Random Forest Regressor

Train-Test Split: 80-20

Evaluation Metrics:

R² Score

MAE

RMSE

🚀 How To Run The Project
1️⃣ Clone Repository
git clone https://github.com/ParthDhoble23/car-price-prediction.git
cd car-price-prediction

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run Streamlit App
streamlit run app.py


Then open:

http://localhost:8501

 📊 Model Performance-
 **Model Used:** Random Forest Regressor  
 **Train/Test Split:** 80/20  
 **R² Score:** 0.9599938850484411  
 **MAE:** 0.63872131147541  
 **MSE:** 0.9215642422950816  
 **RMSE:** 0.9599813760147025  

🎯 Features

Interactive sliders and dropdowns

Real-time price prediction

Clean UI

Trained ML model saved with joblib

📌 Future Improvements

Hyperparameter tuning

Cross-validation

Deployment on Streamlit Cloud

Docker support

👤 Author

Parth Dhoble
GitHub: https://github.com/ParthDhoble23