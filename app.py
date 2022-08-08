#from flask import Flask

# Create a New Flask App Instance
#app = Flask(__name__)

# Create Flask Routes
#@app.route('/')
#def Hello_world():
    #return 'Hello World'

# Run a Flask App

# Set Up the Database and Flask
# Set Up the Flask Weather App
import datetime as dt
from unittest import result
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Set Up the Database
# Access the SQLite database.
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect the database into our classes.
Base = automap_base()

#  reflect the database.
Base.prepare(engine, reflect=True)

# create a variable for each of the classes
Measurement = Base.classes.measurement
Station = Base.classes.station

# create a session link from Python to the database 
session = Session(engine)

# Set Up Flask
# create a Flask application called "app."
app = Flask(__name__)

# Create the Welcome Route
# Define welcome route
@app.route("/")

# First, create a function welcome() with a return statement
def welcome():
    return(
    '''
    Welcome to the Hawaii Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

# Precipitation Route - create the route
@app.route("/api/v1.0/precipitation")

# create the precipitation() function.
def precipitaion():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # get the date and precipitation for the previous year
    precipitation = session.query(Measurement.date, Measurement.prcp).\
      filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
      # use jsonify() to format our results into a JSON structured file
    return jsonify(precip)

    # add api/v1.0/precipitation to the end of the web address. 

# Stations Route - return he list of all stations
# Define the route and route name
@app.route("/api/v1.0/stations")
# create a new function called stations()
def stations():
  # create a query that will allow us to get all of the stations in our database
  results = session.query(Station.station).all()
  # to unravel our results into a one-dimensional array using 'function np.ravel()' with 'results' parameter,.\
  # use "list" function to convert unraveled data to list
  stations = list(np.ravel(results))
  return jsonify(stations=stations)

# Monthly Temperature Route, tobs = temperature observation routes
# Define route
@app.route("/api/v1.0/tobs")

#create function
def temp_monthly():
  prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
  # query the primary station for all the temperature observations from the previous year
  results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
  # convert that array into a list.
  temps = list(np.ravel(results))
  return jsonify(temps=temps)

# Statistics Route
# route will be to report on the minimum, average, and maximum temperatures. 
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/2017-06-01/2017-06-30")

# create a function called stats() 
def starts(start=None, end=None):
  # create a list called sel to select the minimum, average, and maximum temperatures from our SQLite database
  sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

  # add an if-not statement to our code to determine the starting and ending date
  if not end:
    results = session.query(*sel).\
      filter(Measurement.date >= start).all()
    temps = list(np.ravel(results))
  return jsonify(temps=temps)

  # calculate the temperature minimum, average, and maximum with the start and end dates
  def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)


    

