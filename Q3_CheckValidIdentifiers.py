# Program to check valid identifiers

def is_valid_identifier(identifier):
    """Check if the given string is a valid Python identifier."""
    return identifier.isidentifier()

if __name__ == "__main__":
    user_input = input("Enter an identifier to check: ")
    if is_valid_identifier(user_input):
        print(f"'{user_input}' is a valid identifier.")
    else:
        print(f"'{user_input}' is NOT a valid identifier.")

print('This code is written and executed by Kaivalaya Dua 0231BCA205')