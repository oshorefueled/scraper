from ..lib.summary import Summary
import requests as request
from ..lib.scrape import Scrape
from flask import Blueprint
from constants import constants

summary_api = Blueprint('summary_api', __name__)


@summary_api.route('/v1/summary')
def summary():
    summari = Summary(constants.WARRNAMBOOL)
    soup = summari.get_summary_content()
    print soup.prettify()
    return "a response"

