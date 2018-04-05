import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

begin_date = dt.datetime(2017, 5, 1)
end_date = dt.datetime(2017, 5, 15)

engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect Database into ORM class
Base = automap_base()
Base.prepare(engine, reflect=True)

Measurements = Base.classes.measurements

session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations"
    )

@app.route("/api/v1.0/precipitation")
def prcp():

    results = session.query(Measurements).\
    filter(Measurements.date > begin_date - dt.timedelta(days=365)).filter(Measurements.date < end_date).all()

    all_data = []

    # Iterate through each row value in query 
    for row in results:
        
        # Make a dictionary for each row 
        prcp_dict = {}
        
        # Extract each column value per row of data
        prcp_dict["date"] = row.date
        prcp_dict["tobs"] = row.tobs
        prcp_dict["prcp"] = row.prcp
        
        # append row to list
        all_data.append(prcp_dict)

    return jsonify(all_data)

@app.route("/api/v1.0/stations")
def stations():

    results = session.query(Measurements).group_by(Measurements.station).all()

    all_data = []

    for row in results:

        stations_dict = {}
        stations_dict["station"] = row.station

        all_data.append(stations_dict)

    return jsonify(all_data)

@app.route("/api/v1.0/tobs")
def tobs():

    results = session.query(Measurements).\
    filter(Measurements.date > begin_date - dt.timedelta(days=365)).filter(Measurements.date < end_date).all()

    all_data = []

    for row in results:

        tobs_dict = {}
        tobs_dict["date"] = row.date
        tobs_dict["tobs"] = row.tobs

        all_data.append(tobs_dict)

    return jsonify(all_data)

if __name__ == '__main__':
    app.run(debug=True)
