from flask import Blueprint, request, jsonify
from services.order_service import checkout_order

order_blueprint = Blueprint("order", __name__)

@order_blueprint.route("/", methods=["POST"])
def checkout():
    data = request.json
    response = checkout_order(data)
    return jsonify(response), response["status"]
