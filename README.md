# HEART DISEASE USING FLASK
Heart disease is one of the leading causes of death globally. Early prediction and diagnosis can significantly improve patient outcomes. This project aims to provide a tool to predict the likelihood of heart disease based on patient data using machine learning.

### Features:
•	Easily input patient data through a user-friendly web interface.

•	Provides predictions on whether heart disease is present or not based on the entered information.

•	Displays the prediction results on the same page for immediate feedback.

### Installation:
1.	**Clone the repository:**
```bash
git clone https://github.com/Anupriya-g/HEART-DISEASE-USING-FLASK.git

cd HEART-DISEASE-USING-FLASK/deployment
```
2.	**Create and activate a virtual environment:**

>Ensure that you have installed the latest version of Python and added it to system's PATH. It can be verified using the following command:
```bash
python --version
```
```bash
python -m venv venv

source venv\Scripts\activate
```
3.	**Install the required packages:**
```bash
pip install pandas
```
```bash
pip install scikit-learn
```
```bash
pip install Flask
```
4.	**Run the Flask app:**
```bash
python app.py
```
The application will be accessible at http://127.0.0.1:8080.

The predicted result will be displayed as "Prediction: Heart Disease"  or  "Prediction: No Heart Disease".
