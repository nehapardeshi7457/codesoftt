import random
import string

# Function to generate the password
def generate_password(length, use_special_chars=True, use_digits=True, use_uppercase=True, use_lowercase=True):
    # Create the pool of characters based on the user's preferences
    characters = ""
    
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
    
    # Generate a password of the specified length using random.choice
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Main program
print("Welcome to the Password Generator!")

# Get user input for password length and complexity
length = int(input("Enter the desired length of the password: "))

# Optional: Get user preferences for complexity
use_special_chars = input("Include special characters (e.g., @, #, $)? (yes/no): ").lower() == 'yes'
use_digits = input("Include digits (0-9)? (yes/no): ").lower() == 'yes'
use_uppercase = input("Include uppercase letters (A-Z)? (yes/no): ").lower() == 'yes'
use_lowercase = input("Include lowercase letters (a-z)? (yes/no): ").lower() == 'yes'

# Ensure at least one character set is selected
if not (use_special_chars or use_digits or use_uppercase or use_lowercase):
    print("Error: You must include at least one character set (lowercase, uppercase, digits, or special characters).")
else:
    # Generate the password based on user input
    password = generate_password(length, use_special_chars, use_digits, use_uppercase, use_lowercase)
    
    # Display the generated password
    print(f"Your generated password is: {password}")
