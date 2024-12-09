from tests import client


def test_add_to_cart_valid(client):
    data = {"item": "popcorn", "quantity": 2, "user_id": 123}
    response = client.post("/cart/add", json=data)
    assert response.status_code == 201
    assert "message" in response.json
    assert response.json["message"] == "Item added to cart"


def test_add_to_cart_missing_item(client):
    data = {"quantity": 2, "user_id": 123}
    response = client.post("/cart/add", json=data)
    assert response.status_code == 400
    assert "message" in response.json
    assert response.json["message"] == "Invalid input"


def test_add_to_cart_missing_quantity(client):
    data = {"item": "popcorn", "user_id": 123}
    response = client.post("/cart/add", json=data)
    assert response.status_code == 200
    assert "message" in response.json
    assert response.json["message"] == "Cart quantity updated"


def test_add_to_cart_invalid_quantity(client):
    data = {"item": "popcorn", "quantity": -2, "user_id": 123}
    response = client.post("/cart/add", json=data)
    assert response.status_code == 400
    assert "message" in response.json
    assert response.json["message"] == "Invalid quantity"


def test_add_to_cart_missing_user_id(client):
    data = {"item": "popcorn", "quantity": 2}
    response = client.post("/cart/add", json=data)
    assert response.status_code == 400
    assert "message" in response.json
    assert response.json["message"] == "Invalid input"


# Test Remove from Cart


def test_remove_from_cart_valid(client):
    data = {"item": "popcorn", "user_id": 123, "quantity": 1}
    response = client.post("/cart/remove", json=data)
    assert response.status_code == 200
    assert "message" in response.json
    assert response.json["message"] == "Cart quantity updated"


def test_remove_from_cart_item_not_in_cart(client):
    data = {"item": "chopcorn", "user_id": 123, "quantity": 1}
    response = client.post("/cart/remove", json=data)
    assert response.status_code == 404
    assert "message" in response.json
    assert response.json["message"] == "Item not found in cart"


def test_remove_from_cart_missing_item(client):
    data = {"user_id": 123, "quantity": 1}
    response = client.post("/cart/remove", json=data)
    assert response.status_code == 400
    assert "message" in response.json
    assert response.json["message"] == "Invalid input"


def test_remove_from_cart_invalid_item_id(client):
    data = {"item": "invalid_item", "user_id": 123, "quantity": 1}
    response = client.post("/cart/remove", json=data)
    assert response.status_code == 404
    assert "message" in response.json
    assert response.json["message"] == "Item not found in cart"


def test_remove_from_cart_missing_data(client):
    data = {}
    response = client.post("/cart/remove", json=data)
    assert response.status_code == 400
    assert "message" in response.json
    assert response.json["message"] == "Invalid input"


def test_remove_from_cart_negative_quantity(client):
    # Attempt to remove a quantity larger than available
    data = {"item": "popcorn", "user_id": 123, "quantity": -1}
    response = client.post("/cart/remove", json=data)
    assert response.status_code == 400
    assert "message" in response.json
    assert response.json["message"] == "Invalid quantity"


def test_remove_from_cart_quantity_exceeds_available(client):
    # Simulate a scenario where the quantity exceeds what's in the cart
    data = {"item": "popcorn", "user_id": 123, "quantity": 5}
    response = client.post("/cart/remove", json=data)
    assert response.status_code == 400
    assert "message" in response.json
    assert response.json["message"] == "Quantity cannot be less than 0"
