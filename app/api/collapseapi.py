from ..lib.people import People
from ..lib.dwellings import Dwellings
from ..lib.families import Families
from ..lib.aboriginal import Aboriginal
from flask import Blueprint, jsonify
from constants import constants

collapse_api = Blueprint('collapse_api', __name__)


@collapse_api.route('/v1/collapse/people')
def people():
    people = People(constants.WARRNAMBOOL)
    response = people.get_people_data()
    return jsonify({"status": "success", "data": response})\



@collapse_api.route('/v1/collapse/dwellings')
def dwellings():
    dwellings = Dwellings(constants.WARRNAMBOOL)
    response = dwellings.get_dwellings_data()
    return jsonify({"status": "success", "data": response})


@collapse_api.route('/v1/collapse/families')
def families():
    families = Families(constants.WARRNAMBOOL)
    response = families.get_families_data()
    return jsonify({"status": "success", "data": response})\


@collapse_api.route('/v1/collapse/aboriginal')
def aboriginal():
    aboriginal = Aboriginal(constants.WARRNAMBOOL)
    response = aboriginal.get_aboriginal_data()
    return jsonify({"status": "success", "data": response})



