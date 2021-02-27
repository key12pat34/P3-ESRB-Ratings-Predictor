# -*- coding: utf-8 -*-

import numpy as np
import joblib
from flask import Flask, request, render_template

# Load ML model
model = joblib.load(open('../machine_learning/joblib_model.pk1', 'rb')) 

# Create application
app = Flask(__name__)

# Bind home function to URL
@app.route('/')
def home():
    return render_template('predictor_copy.html')

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
        return render_template('predictor_copy.html', 
                               result = 'This game is rated E')
    elif output == 'ET':
        return render_template('predictor_copy.html', 
                               result = 'This game is rated ET')
    elif output == 'T':
        return render_template('predictor_copy.html', 
                               result = 'This game is rated T')                           
    else:
        return render_template('predictor_copy.html', 
                               result = 'This game is rated M')
if __name__ == '__main__':
#Run the application
    app.run()
    
