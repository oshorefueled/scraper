from ..lib.summary import Summary
from flask import Blueprint, jsonify, request

summary_api = Blueprint('summary_api', __name__)



@summary_api.route('/v1/summary')
def summary():
    location_code = request.args.get("code")
    summari = Summary(location_code)
    response = summari.build_summary_data()
    return jsonify({"status": "success", "data": response})



