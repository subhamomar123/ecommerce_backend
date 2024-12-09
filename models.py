from db import db


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    item = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, default=1)

    def __repr__(self):
        return f"<Cart {self.id} - {self.item}, Quantity: {self.quantity}>"


class Order(db.Model):
    __tablename__ = "orders"

    order_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    discount_code = db.Column(
        db.String, db.ForeignKey("discount_code.code"), nullable=True
    )
    discount_applied = db.Column(db.Float, default=0.0)
    order_amount = db.Column(db.Float, nullable=False)
    order_items = db.relationship("OrderItems", backref="order", lazy=True)

    def __repr__(self):
        return f"<Order {self.order_id} - User {self.user_id}>"


class OrderItems(db.Model):
    __tablename__ = "order_items"

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.order_id"), nullable=False)
    item = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<OrderItem {self.id} - {self.item}, Quantity: {self.quantity}>"


class DiscountCode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String, nullable=False, unique=True)
    is_used = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=db.func.now())

    def __repr__(self):
        return f"<DiscountCode {self.code}>"
