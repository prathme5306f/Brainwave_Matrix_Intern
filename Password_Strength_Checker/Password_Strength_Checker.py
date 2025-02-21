import re
import string
import random
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

def generate_stronger_password(password):
    """Generate a stronger password by improving user input."""
    new_password = list(password)
    
    if not any(char.isdigit() for char in password):
        new_password.append(str(random.randint(0, 9)))
    
    if not any(char.isupper() for char in password):
        new_password.append(random.choice(string.ascii_uppercase))
    
    if not any(char in string.punctuation for char in password):
        new_password.append(random.choice(string.punctuation))
    
    while len(new_password) < 12:
        new_password.append(random.choice(string.ascii_letters + string.digits + string.punctuation))
    
    random.shuffle(new_password)
    return "".join(new_password)

def check_password_strength(password):
    """Check the strength of the provided password and suggest improvements."""
    strength_score = 0
    feedback = []
    suggestions = []
    
    if password.lower() in common_passwords:
        return "Weak", ["Your password is too common and can be easily guessed."], ["Use a more unique password."], generate_stronger_password(password)
    
    if len(password) >= 12:
        strength_score += 2
    elif len(password) >= 8:
        strength_score += 1
    else:
        feedback.append("Your password is too short. Aim for at least 12 characters.")
        suggestions.append("Make your password longer (12+ characters).")
    
    if any(char.isdigit() for char in password):
        strength_score += 1
    else:
        feedback.append("Include at least one number to improve security.")
        suggestions.append("Add a digit (0-9) to strengthen your password.")
    
    if any(char.isupper() for char in password):
        strength_score += 1
    else:
        feedback.append("Add an uppercase letter for better security.")
        suggestions.append("Use at least one uppercase letter (A-Z).")
    
    if any(char.islower() for char in password):
        strength_score += 1
    else:
        feedback.append("Lowercase letters help make a strong password.")
        suggestions.append("Include at least one lowercase letter (a-z).")
    
    if any(char in string.punctuation for char in password):
        strength_score += 1
    else:
        feedback.append("Adding a special character makes your password harder to guess.")
        suggestions.append("Use a special character like @, #, $, etc.")
    
    char_counts = Counter(password)
    if max(char_counts.values()) > len(password) // 2:
        feedback.append("Too many repeated characters make your password weak.")
        suggestions.append("Reduce repeated characters for a stronger password.")
    
    strength_levels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    strength_rating = min(strength_score, 4)
    
    return strength_levels[strength_rating], feedback, suggestions, generate_stronger_password(password) if strength_score < 4 else None

while True:
    password = input("Enter a password (or type 'exit' to quit): ")
    if password.lower() == "exit":
        print("Goodbye! Exiting the program.")
        break
    
    strength, feedback, suggestions, stronger_password = check_password_strength(password)
    print(f"Password Strength: {strength}")
    
    if feedback:
        print("How to improve:")
        for suggestion in suggestions:
            print(f"- {suggestion}")
    
    if stronger_password:
        print(f"Suggested Stronger Password: {stronger_password}")
    
    print("\n")  # Adds a new line for better readability
