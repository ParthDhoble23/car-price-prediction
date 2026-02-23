import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import joblib

# Load dataset
df = pd.read_csv("data/car data.csv")

# Drop car name
df.drop(['Car_Name'], axis=1, inplace=True)

# Feature Engineering
df['Car_Age'] = 2025 - df['Year']
df.drop(['Year'], axis=1, inplace=True)

# Encoding
df = pd.get_dummies(df, drop_first=True)

# Define X and y
X = df.drop('Selling_Price', axis=1)
y = df['Selling_Price']

print("Features used for training:")
print(X.columns)

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# =====================
# 🔥 MODEL EVALUATION
# =====================

y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print("\n📊 Model Evaluation Results:")
print("R2 Score:", r2)
print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)

# Save model
joblib.dump(model, "model/model.pkl")

# Save feature names
joblib.dump(X.columns.tolist(), "model/features.pkl")

print("\n Model and features saved successfully!")
