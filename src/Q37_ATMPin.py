# Write a program to check the ATM pin using the break statement.

# Set the correct PIN
correct_pin = 1234

# Give user 3 attempts
for attempt in range(1, 4):
    # Get PIN input from user
    entered_pin = int(input(f"Attempt {attempt}: Enter your ATM PIN: "))
    
    # Check if PIN is correct
    if entered_pin == correct_pin:
        print("PIN accepted! Access granted.")
        break
    else:
        print("Incorrect PIN!")
        if attempt == 3:
            print("Card blocked! Too many incorrect attempts.")

print('This code is written and executed by Kaivalaya Dua 0231BCA205')
