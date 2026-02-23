🚗 Used Car Price Prediction

A Machine Learning web application built using Streamlit that predicts the selling price of a used car based on user inputs.

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
git clone https://github.com/yourusername/UsedCarProject.git
cd UsedCarProject

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run Streamlit App
streamlit run app.py


Then open:

http://localhost:8501

📊 Model Performance

(Replace this with your actual results)

R² Score: 0.91

MAE: 0.45

RMSE: 0.68

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

Your Name
GitHub: https://github.com/ParthDhoble23