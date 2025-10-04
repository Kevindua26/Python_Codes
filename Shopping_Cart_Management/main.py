from product_catalog import ProductCatalog, Product
from shopping_cart import Cart
from payment_processing import PaymentProcessor

def main():
    # Initialize catalog
    catalog = ProductCatalog()
    catalog.add_product(Product(101, 'Laptop', 50000, 10))
    catalog.add_product(Product(102, 'Mouse', 500, 50))
    catalog.add_product(Product(103, 'Keyboard', 1500, 30))

    cart = Cart(catalog)
    processor = PaymentProcessor()

    while True:
        print("\n1. Browse Products")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Update Cart")
        print("5. Remove from Cart")
        print("6. Checkout")
        print("7. Save Cart")
        print("8. Load Cart")
        print("9. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            catalog.display_products()
        elif choice == '2':
            try:
                id = int(input("Enter product ID: "))
                qty = int(input("Enter quantity: "))
                product = catalog.get_product_by_id(id)
                if product:
                    cart.add_item(product, qty)
                    print("Added to cart")
                else:
                    print("Product not found")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == '3':
            cart.display_cart()
            total = cart.get_total()
            print(f"Total: {total}")
        elif choice == '4':
            try:
                id = int(input("Enter product ID: "))
                qty = int(input("Enter new quantity: "))
                cart.update_quantity(id, qty)
                print("Updated")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == '5':
            id = int(input("Enter product ID: "))
            cart.remove_item(id)
            print("Removed")
        elif choice == '6':
            total = cart.get_total()
            discount_code = input("Enter discount code (or leave blank): ")
            discount = cart.apply_discount(discount_code)
            final_total = total * discount
            print(f"Final total: {final_total}")
            payment_info = {'card_number': input("Enter card number (16 digits): ")}
            try:
                if processor.process_payment(final_total, payment_info):
                    print("Checkout successful")
                    cart.items = []  # Clear cart
            except Exception as e:
                print(f"Checkout failed: {e}")
        elif choice == '7':
            cart.save_to_file()
            print("Cart saved")
        elif choice == '8':
            cart.load_from_file()
            print("Cart loaded")
        elif choice == '9':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()