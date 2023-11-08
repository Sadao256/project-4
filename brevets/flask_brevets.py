"""
Replacement for RUSA ACP brevet time calculator
(see https://rusa.org/octime_acp.html)

"""

import flask
from flask import request
import arrow  # Replacement for datetime, based on moment.js
import acp_times  # Brevet time calculations
import config

import logging

###
# Globals
###
app = flask.Flask(__name__)
CONFIG = config.configuration()

###
# Pages
###


@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    return flask.render_template('calc.html')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    return flask.render_template('404.html'), 404


###############
#
# AJAX request handlers
#   These return JSON, rather than rendering pages.
#
###############
@app.route("/_calc_times")
def _calc_times():
    """
    Calculates open/close times from kilometers, using rules
    described at https://rusa.org/octime_alg.html.
    Expects three URL-encoded arguments: km, start_time, and brevet_dist.
    """
    app.logger.debug("Got a JSON request")
    
    # Get the Km from the Ajax request
    km = request.args.get('km', 999, type=float)
    
    # Get the start time from the Ajax request
    start_time_str = request.args.get('start_time')

    # Get the Brevet Distance from the Ajax request
    brevet_dist = request.args.get('brevet_dist', 200, type=int)
    
    # Convert the start_time string to an arrow object
    start_time = arrow.get(start_time_str)

    # calculate the open time with the arguements km, brevet_dist, start_time using open_time function in the file acp_times
    open_time = acp_times.open_time(km, brevet_dist, start_time).format('YYYY-MM-DDTHH:mm')

    # calculate the close time with the arguements km, brevet_dist, start_time using close_time function in the file acp_times
    close_time = acp_times.close_time(km, brevet_dist, start_time).format('YYYY-MM-DDTHH:mm')

    result = {"open": open_time, "close": close_time}
    return flask.jsonify(result=result)



#############

app.debug = CONFIG.DEBUG
if app.debug:
    app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")
