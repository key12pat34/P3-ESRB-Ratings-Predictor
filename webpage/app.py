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
engine = create_engine("postgres://bwrtaugijyfgyd:2a00951144d14d957fe21c02613f65b2083e6f64f7cc32c28d784c5e8b8960dc@ec2-54-205-187-125.compute-1.amazonaws.com:5432/d8uhbccr3c2pvb")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
School = Base.classes.schooltable

# Marker Table
Marker = Base.classes.marker_data

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def homepage():
    return render_template("homepage.html")

# Query the database and send the jsonified results
@app.route("/map.html")
def map():
    return render_template("map.html")

@app.route("/api")
def location():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    results = session.query(Marker.name, Marker.enrollment, Marker.teachercount, Marker.schooltype, Marker.latitude, Marker.longitude).all()
    # results = session.query(School._id, School.name).all()
    session.close()
    
    # Convert list of tuples into normal lists
    all_schools = []
    
    for name, enrollment, teachercount, schooltype, latitude, longitude in results:
        school_dict = {}
        school_dict["name"] = name
        school_dict["enrollment"] = enrollment
        school_dict["teachercount"] = teachercount
        school_dict["type"] = schooltype
        school_dict["latitude"] = latitude
        school_dict["longitude"] = longitude
        all_schools.append(school_dict)
    return jsonify(all_schools)

if __name__ == "__main__":
    app.run()
