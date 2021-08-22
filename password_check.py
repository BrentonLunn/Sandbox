"""
Prac 03 Password checker
"""

MINIMUM_LENGTH = 5
password = input("Enter password: ")
while len(password) < MINIMUM_LENGTH:
    print(f"The password must be at least {str(MINIMUM_LENGTH)} characters long.")
    password = input("Enter password: ")
print("*" * len(password))