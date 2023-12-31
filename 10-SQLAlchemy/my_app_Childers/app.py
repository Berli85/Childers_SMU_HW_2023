# Import the dependencies.
from flask import Flask, jsonify

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspec, text



#################################################
# Database Setup
#################################################
engine = create_engine("sqlite://Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.Measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
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
        f"<h1>Welcome to Hawaii's Best Climate API!<h1><br/>"
        f"<h3>Available Routes:</h3><br/>"
        f"<a href='/api/v1.0/precipitation' target='_blank'>/api/v1.0/percipitation,/a>"
        f"<a href='/api/v1.0/stations' target='_blank'>/api/v1.0/stations,/a>"
    )

@app.route("/api/v1.0/percipitation")
def precipitation():
    """Return the precipitation data as json"""

    query = """ SELECT
                    date,
                    station,
                    prcp
                FROM
                    Measurement
                WHERE
                    date >= '2016-08-23';
"""

    df = pd.read_sql(text(query), con=engine)
    data = df.to_dict(orient="records")
    return jsonify(db)

@app.route("/api/v1.0/percipitation")
def stations():
      query = """ SELECT
                   *
                FROM
                    station;
"""

    df = pd.read_sql(text(query), con=engine)
    data = df.to_dict(orient="records")
    return jsonify(db)

@app.route("/api/v1.0/<start>")
def startDate(start):
      query = f""" SELECT
                   min(tobs) as min_temp,
                   max(tobs) as max_temp,
                   avg(tobs) as avg_temp
                FROM
                    measurements
                WHERE
                    date >= '{start}';
"""

    df = pd.read_sql(text(query), con=engine)
    data = df.to_dict(orient="records")
    return jsonify(db)
    
#################################################
# Application Execution
#################################################
if __name__ == "__main__":
    app.run(debug=True)