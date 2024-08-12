# app.py

import pickle
import pandas as pd
from flask import Flask, request, render_template

# Load the saved model
with open('heart_disease_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Create a Flask app
app = Flask(__name__)

@app.route("/", methods=['GET'])
def loadPage():
    return render_template('index.html', query="")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data and convert input values to floats
        input_features = [float(request.form[f'query{i}']) for i in range(1, 14)]
        
        # Define feature columns and create DataFrame for prediction
        features = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
        new_df = pd.DataFrame([input_features], columns=features)
        
        # Predict using the loaded model
        prediction = model.predict(new_df)
        
        # Map prediction to Heart Disease status
        output = 'Heart Disease' if prediction[0] == 1 else 'No Heart Disease'
        
        return render_template('index.html', query="", output=f'Prediction: {output}',
                               **{f'query{i}': request.form[f'query{i}'] for i in range(1, 14)})
    
    except Exception as e:
        return str(e)

if __name__ == "__main__":
        app.run(host='0.0.0.0', port=8080, debug=True)
