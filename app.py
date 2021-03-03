# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
import numpy as np
import joblib

# Load ML model
model = joblib.load(open('./machine_learning/joblib_model.pk1', 'rb')) 

# Flask Setup
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/analysis.html")
def analysis():
    return render_template("analysis.html")

@app.route("/predictor.html")
def predictor():
    return render_template("predictor.html")

# Bind predict function to URL
@app.route('/predict', methods =['POST'])
def predict():
    
    # Put all form entries values in a list 
    features = [float(i) for i in request.form.values()]
    # Convert features to array
    array_features = [np.array(features)]
    # Predict features
    prediction = model.predict(array_features)
    
    output = prediction
    
    # Check the output values and retrive the result with html tag based on the value
    if output == 'E':
        return render_template('predictor.html', 
                               result = 'The predicted rating is: E')
    elif output == 'ET':
        return render_template('predictor.html', 
                               result = 'The predicted rating is: ET')
    elif output == 'T':
        return render_template('predictor.html', 
                               result = 'The predicted rating is: T')                           
    else:
        return render_template('predictor.html', 
                               result = 'The predicted rating is: M')

@app.route("/walkthrough.html")
def walkthrough():
    return render_template("walkthrough.html")

if __name__ == "__main__":
    app.run()
