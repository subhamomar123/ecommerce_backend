from flask import Blueprint, request, jsonify
from services.cart_service import add_item_to_cart, remove_item_from_cart

cart_blueprint = Blueprint("cart", __name__)


@cart_blueprint.route("/add", methods=["POST"], strict_slashes=False)
def add_to_cart():
    data = request.json
    response = add_item_to_cart(data)
    return jsonify(response), response["status"]


@cart_blueprint.route("/remove", methods=["POST"], strict_slashes=False)
def remove_from_cart():
    data = request.json
    response = remove_item_from_cart(data)
    return jsonify(response), response["status"]
