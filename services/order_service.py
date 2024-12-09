from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import DiscountCode, Order, OrderItems

N = 5


def checkout_order(data):
    user_id = data.get("user_id")
    order_items_data = data.get("order_items")
    order_amount = data.get("order_amount")
    discount_code = data.get("discount_code")

    missing_fields = []

    if not user_id:
        missing_fields.append("user_id")
    if not order_items_data:
        missing_fields.append("order_items")
    if order_amount is None:
        missing_fields.append("order_amount")

    if missing_fields:
        return {
            "message": "Invalid input",
            "missing_fields": missing_fields,
            "status": 400,
        }

    try:
        total_orders = Order.query.filter_by(user_id=user_id).count()
        discount_applied = 0.0
        if (total_orders + 1) % N == 0 and discount_code:
            discount = DiscountCode.query.filter_by(
                code=discount_code, is_used=False
            ).first()
            if discount and discount.code == discount_code:
                discount_applied = 0.10 * order_amount
                order_amount -= discount_applied
                discount.is_used = True
                db.session.add(discount)

        order = Order(
            user_id=user_id,
            discount_code=discount_code if discount_applied > 0 else None,
            discount_applied=discount_applied,
            order_amount=order_amount,
        )

        db.session.add(order)
        db.session.commit()

        order_items = [
            OrderItems(
                order_id=order.order_id,
                item=item_data.get("item"),
                quantity=item_data.get("quantity", 1),
            )
            for item_data in order_items_data
        ]

        db.session.add_all(order_items)

        db.session.commit()

        return {
            "message": "success",
            "order_id": order.order_id,
            "order_amount": order_amount,
            "discount_applied": discount_applied,
            "status": 201,
        }

    except SQLAlchemyError as e:
        db.session.rollback()
        return {"message": "Error processing the order", "status": 500, "error": str(e)}
