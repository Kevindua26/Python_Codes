import json
import os

class Cart:
    def __init__(self, catalog):
        self.catalog = catalog
        self.items = []  # list of {'product_id': id, 'quantity': qty}

    def add_item(self, product, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if quantity > product.stock:
            raise ValueError("Not enough stock")
        # Check if already in cart
        for item in self.items:
            if item['product_id'] == product.id:
                if item['quantity'] + quantity > product.stock:
                    raise ValueError("Not enough stock")
                item['quantity'] += quantity
                return
        self.items.append({'product_id': product.id, 'quantity': quantity})

    def remove_item(self, product_id):
        self.items = [item for item in self.items if item['product_id'] != product_id]

    def update_quantity(self, product_id, quantity):
        if quantity <= 0:
            self.remove_item(product_id)
            return
        product = self.catalog.get_product_by_id(product_id)
        if not product:
            raise ValueError("Product not found")
        if quantity > product.stock:
            raise ValueError("Not enough stock")
        for item in self.items:
            if item['product_id'] == product_id:
                item['quantity'] = quantity
                return
        raise ValueError("Product not in cart")

    def get_total(self):
        total = 0
        for item in self.items:
            product = self.catalog.get_product_by_id(item['product_id'])
            if product:
                total += product.price * item['quantity']
        return total

    def apply_discount(self, discount_code):
        # Simple discount: 10% off for 'SAVE10'
        if discount_code == 'SAVE10':
            return 0.9
        return 1.0

    def save_to_file(self, filename='cart.json'):
        with open(filename, 'w') as f:
            json.dump(self.items, f)

    def load_from_file(self, filename='cart.json'):
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                self.items = json.load(f)

    def display_cart(self):
        for item in self.items:
            product = self.catalog.get_product_by_id(item['product_id'])
            if product:
                print(f"{product.name}: {item['quantity']} x {product.price} = {item['quantity'] * product.price}")