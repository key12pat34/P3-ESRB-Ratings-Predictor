# import necessary libraries
# from models import create_classes
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
import psycopg2
import sys
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import numpy as np

#################################################
# Database Setup
#################################################
# engine = create_engine("postgres://bwrtaugijyfgyd:2a00951144d14d957fe21c02613f65b2083e6f64f7cc32c28d784c5e8b8960dc@ec2-54-205-187-125.compute-1.amazonaws.com:5432/d8uhbccr3c2pvb")

# # reflect an existing database into a new model
# Base = automap_base()
# # reflect the tables
# Base.prepare(engine, reflect=True)

# # Save reference to the table
# School = Base.classes.schooltable

# # Marker Table
# Marker = Base.classes.marker_data

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/analysis.html")
def analysis():
    return render_template("analysis.html")

@app.route("/predictor.html")
def predict():
    return render_template("predictor.html")

@app.route("/walkthrough.html")
def walkthrough():
    return render_template("walkthrough.html")

if __name__ == "__main__":
    app.run()
