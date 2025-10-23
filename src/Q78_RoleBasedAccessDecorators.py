# Write a program to create a login system into a role-based access control system using decorators.

# User database
users_db = {
    "admin": {"password": "admin123", "role": "admin"},
    "manager": {"password": "manager123", "role": "manager"},
    "user": {"password": "user123", "role": "user"}
}

# Current logged in user
current_user = {"username": None, "role": None}

# Authentication decorator
def login_required(func):
    """Decorator to check if user is logged in"""
    def wrapper(*args, **kwargs):
        if current_user["username"] is None:
            print("❌ Access Denied! Please login first.")
            return None
        return func(*args, **kwargs)
    return wrapper

# Role-based access decorator
def role_required(required_role):
    """Decorator to check user role"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            if current_user["role"] != required_role:
                print(f"❌ Access Denied! This action requires '{required_role}' role.")
                print(f"   Your role: '{current_user['role']}'")
                return None
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Admin level access
def admin_access(func):
    """Decorator for admin-only access"""
    def wrapper(*args, **kwargs):
        if current_user["role"] != "admin":
            print(f"❌ Admin access required! Your role: '{current_user['role']}'")
            return None
        return func(*args, **kwargs)
    return wrapper

# Functions with different access levels
@login_required
def view_profile():
    """Function accessible to all logged-in users"""
    print(f"\n✓ Profile: {current_user['username']}")
    print(f"  Role: {current_user['role']}")

@login_required
@role_required("manager")
def manage_team():
    """Function accessible only to managers"""
    print("\n✓ Manager Dashboard")
    print("  - View team members")
    print("  - Assign tasks")
    print("  - Generate reports")

@login_required
@admin_access
def delete_user():
    """Function accessible only to admins"""
    print("\n✓ Admin Panel")
    print("  - Delete user function executed")
    print("  - User deletion privileges granted")

@login_required
def view_dashboard():
    """Dashboard accessible to all logged-in users"""
    print(f"\n✓ Welcome to Dashboard, {current_user['username']}!")
    print(f"  Your role: {current_user['role']}")

# Login function
def login(username, password):
    """Login function"""
    if username in users_db:
        if users_db[username]["password"] == password:
            current_user["username"] = username
            current_user["role"] = users_db[username]["role"]
            print(f"\n✓ Login successful! Welcome {username}")
            print(f"  Role: {current_user['role']}")
            return True
        else:
            print("\n❌ Invalid password!")
            return False
    else:
        print("\n❌ User not found!")
        return False

# Logout function
def logout():
    """Logout function"""
    if current_user["username"]:
        print(f"\n✓ {current_user['username']} logged out successfully!")
        current_user["username"] = None
        current_user["role"] = None
    else:
        print("\n❌ No user is logged in!")

# Main program
print("=" * 50)
print("   ROLE-BASED ACCESS CONTROL SYSTEM")
print("=" * 50)
print("\nAvailable Users:")
print("  1. Username: admin, Password: admin123, Role: admin")
print("  2. Username: manager, Password: manager123, Role: manager")
print("  3. Username: user, Password: user123, Role: user")

while True:
    print("\n" + "=" * 50)
    print("1. Login")
    print("2. View Profile")
    print("3. View Dashboard")
    print("4. Manage Team (Manager only)")
    print("5. Delete User (Admin only)")
    print("6. Logout")
    print("7. Exit")
    
    choice = input("\nEnter choice: ")
    
    if choice == "1":
        username = input("Username: ")
        password = input("Password: ")
        login(username, password)
    
    elif choice == "2":
        view_profile()
    
    elif choice == "3":
        view_dashboard()
    
    elif choice == "4":
        manage_team()
    
    elif choice == "5":
        delete_user()
    
    elif choice == "6":
        logout()
    
    elif choice == "7":
        print("\nExiting system. Goodbye!")
        break
    
    else:
        print("\n❌ Invalid choice!")

print('This code is written and executed by Kaivalaya Dua 0231BCA205')
