users = []

def register():
    print("Register a new user:")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    confirm_password = input("Confirm your password: ")
    mobile_phone = input("Enter your mobile phone (Egyptian format): ")

    # Validate mobile phone number
    if not mobile_phone.startswith("+20") or (len(mobile_phone) < 10 or len(mobile_phone)>14):
        print("Invalid mobile phone number. Please try again.")
        return

    # Check if email is already registered
    if any(user["email"] == email for user in users):
        print("Email already registered. Please try again.")
        return

    # Create a new user
    user = {"id": len(users) + 1, "first_name": first_name, "last_name": last_name, "email": email, "password": password}
    users.append(user)
    print("User registered successfully!")

def login():
    print("Login:")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    # Check if email is registered
    user = next((user for user in users if user["email"] == email), None)
    if user is None:
        print("Email not registered. Please try again.")
        return

    # Check if password is correct
    if user["password"] != password:
        print("Incorrect password. Please try again.")
        return

    print("Login successful! You are now logged in.")