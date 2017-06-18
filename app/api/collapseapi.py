from ..lib.people import People
from ..lib.dwellings import Dwellings
from ..lib.families import Families
from ..lib.aboriginal import Aboriginal
from flask import Blueprint, jsonify, request

collapse_api = Blueprint('collapse_api', __name__)


@collapse_api.route('/v1/collapse/people')
def people():
    location_code = request.args.get("code")
    people = People(location_code)
    response = people.get_people_data()
    return jsonify({"status": "success", "data": response})\



@collapse_api.route('/v1/collapse/dwellings')
def dwellings():
    location_code = request.args.get("code")
    dwellings = Dwellings(location_code)
    response = dwellings.get_dwellings_data()
    return jsonify({"status": "success", "data": response})


@collapse_api.route('/v1/collapse/families')
def families():
    location_code = request.args.get("code")
    families = Families(location_code)
    response = families.get_families_data()
    return jsonify({"status": "success", "data": response})\


@collapse_api.route('/v1/collapse/aboriginal')
def aboriginal():
    location_code = request.args.get("code")
    aboriginal = Aboriginal(location_code)
    response = aboriginal.get_aboriginal_data()
    return jsonify({"status": "success", "data": response})



