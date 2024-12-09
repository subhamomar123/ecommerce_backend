from models import OrderItems, db, Order, DiscountCode
import uuid
from sqlalchemy import func

NTH_ORDER = 5


def generate_discount_code():
    unused_discount_code = DiscountCode.query.filter_by(is_used=False).first()

    if unused_discount_code:
        return {
            "message": "success",
            "discount_code": unused_discount_code.code,
            "status": 200,
        }

    discount_code = str(uuid.uuid4().hex[:8]).upper()

    new_discount_code = DiscountCode(code=discount_code)
    db.session.add(new_discount_code)
    db.session.commit()

    return {"message": "success", "discount_code": discount_code, "status": 201}


def get_admin_report():
    try:
        result = (
            db.session.query(
                func.count(Order.order_id).label("total_orders"),
                func.sum(OrderItems.quantity).label("total_items_purchased"),
                func.sum(Order.order_amount).label("total_purchase_amount"),
                func.sum(Order.discount_applied).label("total_discount"),
            )
            .join(
                OrderItems, Order.order_id == OrderItems.order_id
            )  # Change Order.id to Order.order_id
            .first()
        )

        if result is None:
            return {
                "total_orders": 0,
                "total_items_purchased": 0,
                "total_purchase_amount": 0.0,
                "total_discount": 0.0,
                "discount_codes": [],
                "status": 200,
            }

        total_orders = result.total_orders
        total_items_purchased = result.total_items_purchased or 0
        total_purchase_amount = result.total_purchase_amount or 0.0
        total_discount = result.total_discount or 0.0

        discount_codes = DiscountCode.query.filter_by(is_used=True).all()
        discount_codes_data = [
            {"code": discount.code, "used_at": discount.created_at}
            for discount in discount_codes
        ]

        return {
            "total_orders": total_orders,
            "total_items_purchased": total_items_purchased,
            "total_purchase_amount": total_purchase_amount,
            "total_discount": total_discount,
            "discount_codes": discount_codes_data,
            "status": 200,
        }

    except Exception as e:
        return {
            "message": "Error generating the report",
            "status": 500,
            "error": str(e),
        }
