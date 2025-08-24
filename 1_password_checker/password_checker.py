def password_strength_checker(password):
    if len(password) < 8:
        return False

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in "!@#$%^&*":
            has_special = True

    return has_upper and has_lower and has_digit and has_special


# Test examples
if __name__ == "__main__":
    print("Strong password:", password_strength_checker("Password123!"))  # True
    print("Too short:", password_strength_checker("Short1!"))             # False
    print("No uppercase:", password_strength_checker("password123!"))     # False
