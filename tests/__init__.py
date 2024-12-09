import pytest
from app import EcommerceApp
from db import db


@pytest.fixture(scope="module")
def client():
    ecommerce_app = EcommerceApp(
        config={"SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"}
    )
    app = ecommerce_app.app
    app.config["TESTING"] = True
    with app.app_context():
        db.create_all()
    yield app.test_client()
    with app.app_context():
        db.drop_all()
