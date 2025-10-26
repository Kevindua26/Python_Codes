# Program to check invalid identifiers
print('Q04_CheckInvalidIdentifiers.py')

def is_invalid_identifier(identifier):
    """Return True if the string is NOT a valid Python identifier."""
    return not identifier.isidentifier()

if __name__ == "__main__":
    user_input = input("Enter an identifier to check if it's invalid: ")
    if is_invalid_identifier(user_input):
        print(f"'{user_input}' is NOT a valid identifier.")
    else:
        print(f"'{user_input}' is a valid identifier.")
