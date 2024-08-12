import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

# Load the dataset
df = pd.read_csv(r"C:\Users\govin\OneDrive\Documents\datasets\heart-disease.csv")

# Preprocess the data
X = df.drop(['target'], axis=1)
y = df['target']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Classifier model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model to a pickle file
with open('heart_disease_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model trained and saved as 'heart_disease_model.pkl'")
