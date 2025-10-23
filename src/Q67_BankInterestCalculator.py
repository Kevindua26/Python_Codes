# Write a program for real life examples to calculate the bank interest.

def calculate_simple_interest(principal, rate, time):
    """Calculate Simple Interest"""
    interest = (principal * rate * time) / 100
    total_amount = principal + interest
    return interest, total_amount

def calculate_compound_interest(principal, rate, time):
    """Calculate Compound Interest (compounded annually)"""
    amount = principal * ((1 + rate / 100) ** time)
    interest = amount - principal
    return interest, amount

def display_bank_info(name, account_no, principal):
    """Display customer information"""
    print("\n" + "="*50)
    print("         BANK INTEREST CALCULATOR")
    print("="*50)
    print(f"Customer Name: {name}")
    print(f"Account Number: {account_no}")
    print(f"Principal Amount: ₹{principal}")
    print("="*50)

# Get customer details
name = input("Enter customer name: ")
account_no = input("Enter account number: ")
principal = float(input("Enter principal amount (₹): "))
rate = float(input("Enter interest rate (%): "))
time = float(input("Enter time period (years): "))

# Display information
display_bank_info(name, account_no, principal)

# Calculate Simple Interest
si, total_si = calculate_simple_interest(principal, rate, time)
print(f"\n--- Simple Interest ---")
print(f"Interest: ₹{si:.2f}")
print(f"Total Amount: ₹{total_si:.2f}")

# Calculate Compound Interest
ci, total_ci = calculate_compound_interest(principal, rate, time)
print(f"\n--- Compound Interest ---")
print(f"Interest: ₹{ci:.2f}")
print(f"Total Amount: ₹{total_ci:.2f}")

print(f"\nDifference: ₹{(ci - si):.2f}")

print('This code is written and executed by Kaivalaya Dua 0231BCA205')
