from flask import Blueprint, request, jsonify
from services.admin_service import generate_discount_code, get_admin_report

admin_blueprint = Blueprint("admin", __name__)


@admin_blueprint.route("/generate-discount", methods=["POST"])
def admin_generate_discount():
    response = generate_discount_code()
    return jsonify(response), response["status"]


@admin_blueprint.route("/report", methods=["GET"])
def admin_report():
    response = get_admin_report()
    return jsonify(response), response["status"]
