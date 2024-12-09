from models import Cart
from db import db
from flask import request, jsonify
import json


def add_item_to_cart(data):
    try:
        data = request.get_json()  # Parse the incoming JSON request
    except json.JSONDecodeError:
        return jsonify({"message": "Invalid JSON format", "status": 400})
    user_id = data.get("user_id")
    item = data.get("item")
    quantity = data.get("quantity", 1)

    if quantity <= 0:
        return {"message": "Invalid quantity", "status": 400}

    if not user_id or not item:
        return {"message": "Invalid input", "status": 400}

    existing_cart_item = Cart.query.filter_by(user_id=user_id, item=item).first()

    if existing_cart_item:
        existing_cart_item.quantity += quantity
        db.session.commit()
        return {"message": "Cart quantity updated", "status": 200}
    else:
        new_cart_item = Cart(user_id=user_id, item=item, quantity=quantity)
        db.session.add(new_cart_item)
        db.session.commit()
        return {"message": "Item added to cart", "status": 201}


def remove_item_from_cart(data):
    user_id = data.get("user_id")
    item = data.get("item")
    quantity = data.get("quantity", 1)

    if quantity <= 0:
        return {"message": "Invalid quantity", "status": 400}
    if not user_id or not item:
        return {"message": "Invalid input", "status": 400}

    existing_cart_item = Cart.query.filter_by(user_id=user_id, item=item).first()

    if existing_cart_item:
        if existing_cart_item.quantity - quantity < 0:
            return {"message": "Quantity cannot be less than 0", "status": 400}
        existing_cart_item.quantity -= quantity
        db.session.commit()
        return {"message": "Cart quantity updated", "status": 200}
    else:
        return {"message": "Item not found in cart", "status": 404}
