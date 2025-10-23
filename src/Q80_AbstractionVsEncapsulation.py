# Write a program to demonstrate the difference between abstraction and encapsulation.

# Abstraction - hiding complex implementation details
class Car:
    def start(self):
        print("Car started")  # User doesn't know internal mechanism
    
    def stop(self):
        print("Car stopped")  # Hides complex braking system

# Encapsulation - bundling data and methods together
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable (encapsulated)
    
    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited: {amount}")
    
    def get_balance(self):
        return self.__balance

# Using abstraction
print("=== Abstraction ===")
car = Car()
car.start()  # Simple interface, complex details hidden
car.stop()

# Using encapsulation
print("\n=== Encapsulation ===")
account = BankAccount(1000)
account.deposit(500)
print(f"Balance: {account.get_balance()}")

print('This code is written and executed by Kaivalaya Dua 0231BCA205')
