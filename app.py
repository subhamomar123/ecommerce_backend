from flask import Flask
from routes.cart_routes import cart_blueprint
from routes.order_routes import order_blueprint
from routes.admin_routes import admin_blueprint
from db import db


class EcommerceApp:
    def __init__(self, config=None):
        self.app = Flask(__name__)
        self.config = config or {
            "SQLALCHEMY_DATABASE_URI": "sqlite:///ecommerce.db",
            "SQLALCHEMY_TRACK_MODIFICATIONS": False,
        }
        self._configure_app()
        self._initialize_extensions()
        self._register_blueprints()
        # self._print_routes()

    def _configure_app(self):
        for key, value in self.config.items():
            self.app.config[key] = value

    def _initialize_extensions(self):
        db.init_app(self.app)

    def _register_blueprints(self):
        self.app.register_blueprint(cart_blueprint, url_prefix="/cart")
        self.app.register_blueprint(order_blueprint, url_prefix="/checkout")
        self.app.register_blueprint(admin_blueprint, url_prefix="/admin")

    def _print_routes(self):
        with self.app.app_context():
            for rule in self.app.url_map.iter_rules():
                print(rule)

    def run(self, debug=True):
        with self.app.app_context():
            db.create_all()
        self.app.run(debug=debug)


if __name__ == "__main__":
    ecommerce_app = EcommerceApp()
    ecommerce_app.run(debug=True)
