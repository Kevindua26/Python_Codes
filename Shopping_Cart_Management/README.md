# Shopping Cart Management System

A Python-based online shopping cart system that allows users to browse products, manage their cart, apply discounts, and process checkout. The system is built using object-oriented programming (OOP) principles, with separate modules for product catalog, shopping cart, and payment processing.

## Features

- **Product Catalog**: Browse available products stored as dictionaries with ID, name, price, and stock.
- **Shopping Cart Management**: Add, remove, and update items in the cart using lists to store cart items.
- **Stock Availability Checks**: Control statements ensure stock doesn't go below zero.
- **Discounts**: Apply discount codes (e.g., 'SAVE10' for 10% off) using built-in functions.
- **Checkout and Payment Processing**: Simulate payment with exception handling for errors.
- **Data Persistence**: Save and load cart data using JSON I/O operations.
- **OOP Design**: `Product` and `Cart` classes for encapsulation and modularity.
- **Exception Handling**: Handles invalid quantities, payment errors, and other edge cases.

## Installation and Setup

### Prerequisites

- Python 3.7 or higher installed on your system.
- Git (optional, for cloning the repository).

### Steps

1. **Clone or Download the Repository**:
   - If using Git: `git clone <repository-url>`
   - Or download the ZIP and extract to a folder.

2. **Navigate to the Project Directory**:
   - Open a terminal and change to the project folder: `cd Shopping_Cart_Management`

3. **Set Up a Virtual Environment** (Recommended):
   - Create a virtual environment: `python -m venv .venv`
   - Activate it:
     - On Windows: `.venv\Scripts\activate`
     - On macOS/Linux: `source .venv/bin/activate`

4. **Install Dependencies**:
   - No external dependencies are required (uses only standard library modules like `json`, `os`, `random`).
   - If needed, install any future additions via `pip install -r requirements.txt` (create if necessary).

5. **Run the Application**:
   - Execute: `python main.py`
   - Follow the on-screen menu to interact with the system.

## Usage

The application runs in the console with a menu-driven interface:

1. **Browse Products**: View all available products.
2. **Add to Cart**: Enter product ID and quantity to add items.
3. **View Cart**: Display cart contents and total price.
4. **Update Cart**: Change quantity of an item in the cart.
5. **Remove from Cart**: Remove an item by ID.
6. **Checkout**: Apply discount (optional), enter payment info, and process.
7. **Save Cart**: Save cart data to `cart.json`.
8. **Load Cart**: Load cart data from `cart.json`.
9. **Exit**: Quit the application.

### Example Interaction

- Browse products to see IDs.
- Add product 101 with quantity 2.
- View cart to check total.
- Apply 'SAVE10' for discount.
- Checkout with a 16-digit card number.

## Project Structure

- `main.py`: Entry point with user interface and main loop.
- `product_catalog.py`: Contains `Product` and `ProductCatalog` classes for managing products.
- `shopping_cart.py`: Contains `Cart` class with methods for cart operations, totals, discounts, and I/O.
- `payment_processing.py`: Contains `PaymentProcessor` class for simulating payment.
- `README.md`: This file.
- `__pycache__/`: Compiled Python files (auto-generated).

## Modules and Design

- **Product Catalog Module**: Handles product data as dictionaries. The `Product` class encapsulates attributes, and `ProductCatalog` manages a list of products.
- **Shopping Cart Module**: The `Cart` class uses a list of dictionaries for items. Methods include stock checks, total calculation (using `sum` and list comprehensions), and discount application.
- **Payment Processing Module**: Simulates payment with random success/failure for demonstration.
- **Main Module**: Ties everything together with a loop for user input.

The system uses modules for separation of concerns, making it easy to extend (e.g., add a database for products).

## Scenario-Based Theory Questions

- **How does the system ensure that the stock doesn't go below zero?**  
  Stock is checked in `add_item` and `update_quantity` using if statements. If quantity exceeds stock, a `ValueError` is raised, preventing invalid operations.

- **Why is OOP suitable for modeling products and carts?**  
  OOP allows encapsulation of data and behaviors into classes, improving code organization, reusability, and maintainability. `Product` represents item attributes, while `Cart` handles state and operations.

- **What exceptions might occur during checkout, and how can they be handled?**  
  Exceptions include `ValueError` for invalid amounts or payment info, and payment failures. Handled with try-except blocks to display errors and retry or abort.

- **Discuss how you would design the system using modules and packages.**  
  Use separate modules for each concern (catalog, cart, payment). For scaling, create packages (e.g., `models` for classes, `utils` for helpers) with `__init__.py`. This promotes modularity, testing, and imports.

## Contributing

Feel free to fork and submit pull requests for improvements, such as adding a GUI, database integration, or more discount types.

## License

This project is open-source under the MIT License.
