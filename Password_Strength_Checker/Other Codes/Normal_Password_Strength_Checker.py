import re
import string
from collections import Counter

def load_common_passwords(filename="rockyou.txt"):
    common_passwords = set()
    try:
        with open(filename, "r", encoding="utf-8", errors="ignore") as file:
            common_passwords.update(line.strip().lower() for line in file)
    except FileNotFoundError:
        print(f"Warning: {filename} not found. Skipping.")
    return common_passwords

common_passwords = load_common_passwords()

def check_password_strength(password):
    strength_score = 0
    feedback = []
    suggestions = []
    
    # Check if the password is in common password list
    if password.lower() in common_passwords:
        print("This is a common password and can be easily guessed!")
        return "Weak", ["Your password is too common and can be easily guessed."], 
        ["Use a more unique password that isn't found in common password lists."]
    
    # Check password length
    if len(password) >= 12:
        strength_score += 2
    elif len(password) >= 8:
        strength_score += 1
    else:
        feedback.append("Your password is too short. Aim for at least 12 characters.")
        suggestions.append("Make your password longer (12+ characters).")
    
    # Check for numbers
    if any(char.isdigit() for char in password):
        strength_score += 1
    else:
        feedback.append("Include at least one number to improve security.")
        suggestions.append("Add a digit (0-9) to strengthen your password.")
    
    # Check for uppercase letters
    if any(char.isupper() for char in password):
        strength_score += 1
    else:
        feedback.append("Add an uppercase letter for better security.")
        suggestions.append("Use at least one uppercase letter (A-Z).")
    
    # Check for lowercase letters
    if any(char.islower() for char in password):
        strength_score += 1
    else:
        feedback.append("Lowercase letters help make a strong password.")
        suggestions.append("Include at least one lowercase letter (a-z).")
    
    # Check for special characters
    if any(char in string.punctuation for char in password):
        strength_score += 1
    else:
        feedback.append("Adding a special character makes your password harder to guess.")
        suggestions.append("Use a special character like @, #, $, etc.")
    
    # Avoid excessive repetition of characters
    char_counts = Counter(password)
    if max(char_counts.values()) > len(password) // 2:
        feedback.append("Too many repeated characters make your password weak.")
        suggestions.append("Reduce repeated characters for a stronger password.")
    
    # Determine strength level
    strength_levels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    strength_rating = min(strength_score, 4)  # Limit score index to 4
    
    return strength_levels[strength_rating], feedback, suggestions

# Loop to allow multiple password checks
while True:
    password = input("Enter a password (or type 'exit' to quit): ")
    if password.lower() == "exit":
        print("Goodbye! Exiting the program.")
        break
    
    strength, feedback, suggestions = check_password_strength(password)
    print(f"Password Strength: {strength}")
    if feedback:
        print("How to improve:")
        for suggestion in suggestions:
            print(f"- {suggestion}")
    print("\n")  # Adds a new line for better readability
