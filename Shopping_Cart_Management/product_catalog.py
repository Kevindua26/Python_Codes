class Product:
    def __init__(self, id, name, price, stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Price: {self.price}, Stock: {self.stock}"

class ProductCatalog:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_product_by_id(self, id):
        for product in self.products:
            if product.id == id:
                return product
        return None

    def display_products(self):
        for product in self.products:
            print(product)