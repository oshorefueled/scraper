from ..lib.collapse import Collapse
from flask import Blueprint, jsonify
from constants import constants

collapse_api = Blueprint('collapse_api', __name__)


@collapse_api.route('/v1/collapse/people')
def people():
    collapse = Collapse(constants.WARRNAMBOOL)
    response = collapse.get_people_subheadings()
    return jsonify({"status": "success", "data": response})


@collapse_api.route('/v1/collapse/headings')
def headings():
    collapse = Collapse(constants.WARRNAMBOOL)
    response = collapse.get_people_data()
    return jsonify({"status": "success", "data": response})



