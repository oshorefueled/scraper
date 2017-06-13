from ..lib.summary import Summary
import requests as request
from ..lib.scrape import Scrape
from flask import Blueprint, jsonify
from constants import constants

summary_api = Blueprint('summary_api', __name__)


@summary_api.route('/v1/summary')
def summary():
    summari = Summary(constants.WARRNAMBOOL)
    response = summari.build_summary_data()
    return jsonify({"status": "success", "data": response})



