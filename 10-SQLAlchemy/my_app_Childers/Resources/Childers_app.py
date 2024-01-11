#################################################
# Import the dependencies
#################################################
import numpy as np
import datetime as dt

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################

# create engine using the `hawaii.sqlite` database file
engine = create_engine("sqlite:///my_app_Childers/Resources/hawaii.sqlite")

# declare a Base using `automap_base()`
Base = automap_base()

# use the Base class to reflect the database tables
Base.prepare(autoload_with=engine)

# assign the measurement class to a variable called `Measurement` and
# the station class to a variable called `Station`
Measurement = Base.classes.measurement
Station = Base.classes.station

# create a session
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    return (
        f"Welcome to Hawaii's Climate Analysis<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/temp/start<br/>"
        f"/api/v1.0/temp/start/end<br/>"
        f"<p>'start' and 'end' date should be in the format MMDDYYYY.</p>"

    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Precipitation data from the last year"""
    # calculate the date 1 year ago from last date in database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # query the data for date and precipitation from last year
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()

    session.close()

    # dictionary made with date as the key and prcp as the value
    precip_1 = {date: prcp for date, prcp in precipitation}
    return jsonify(precip_1)

@app.route("/api/v1.0/tobs")
def monthly_temp():
    """Temperatures from previous year"""
    # calculate the date from 1 year ago based on last date in database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # query the primary station for all data on tobs from the last year
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    
    session.close()
    
    # results in 1D array and convert to listt
    temps = list(np.ravel(results))
    
    # Return results
    return jsonify(temps=temps)
    
@app.route("/api/v1.0/stations")
def stations():
    """Stations."""
    results = session.query(Station.station).all()

    session.close()

    # results in 1D array and convert to list
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

  


@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    """Temp_MIN, Temp_AVG, Temp_MAX."""

    # Select statement
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:

        start = dt.datetime.strptime(start, "%m%d%Y")
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()

        session.close()

        temps = list(np.ravel(results))
        return jsonify(temps)

    # calculate minimum, average, and maximum temp
    start = dt.datetime.strptime(start, "%m%d%Y")
    end = dt.datetime.strptime(end, "%m%d%Y")

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    session.close()

    # results in 1D array and convert to list
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

if __name__ == '__main__':
    app.run()
