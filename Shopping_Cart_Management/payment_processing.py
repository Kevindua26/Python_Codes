class PaymentProcessor:
    def process_payment(self, amount, payment_info):
        # Simulate payment processing
        if amount <= 0:
            raise ValueError("Invalid amount")
        # Assume payment_info is a dict with 'card_number', etc., but simple check
        if 'card_number' not in payment_info or len(str(payment_info['card_number'])) != 16:
            raise ValueError("Invalid payment info")
        # Simulate success/failure
        import random
        if random.random() > 0.1:  # 90% success
            print(f"Payment of {amount} processed successfully.")
            return True
        else:
            raise Exception("Payment failed")