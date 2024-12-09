
# EcommerceApp - Flask Application

This is a modular Flask-based e-commerce application. It includes functionalities for managing carts, orders, and administrative tasks such as generating discount codes and viewing reports. The application uses SQLAlchemy for database interactions and provides RESTful APIs for interaction.

---

## Features

### 1. **Cart Management**
   - **Add items to the cart**
   - **Remove items from the cart**

### 2. **Order Management**
   - **Checkout order**
   - **Apply discount codes during checkout**

### 3. **Admin Panel**
   - **Generate discount codes**
   - **View admin reports**

---

## Application Structure

```plaintext
ecommerce_app/
│
├── app.py              # Main application entry point
├── db.py               # Database initialization
├── models.py           # Database models
├── routes/
│   ├── cart_routes.py  # Routes for cart operations
│   ├── order_routes.py # Routes for order operations
│   └── admin_routes.py # Routes for admin operations
└── services/           # Business logic for each feature
    ├── cart_service.py
    ├── order_service.py
    └── admin_service.py
```

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/ecommerce_app.git
   cd ecommerce_app
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Initialize the database:
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

4. Run the application:
   ```bash
   python app.py
   ```

---

## API Endpoints

### Cart Endpoints
- `POST /cart/add` - Add item to the cart.
- `POST /cart/remove` - Remove item from the cart.

### Order Endpoints
- `POST /checkout/` - Checkout and place an order.

### Admin Endpoints
- `POST /admin/generate-discount` - Generate a discount code.
- `GET /admin/report` - View admin report.

---

## Technologies Used
- **Backend:** Flask, Flask-SQLAlchemy
- **Database:** SQLite (default)
- **Others:** Python 3.8+, SQLAlchemy

---

## Author
Developed by Subham omar
