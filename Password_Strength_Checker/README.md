# Password Strength Checker

## Overview
This is a **Password Strength Checker** developed as part of my **cybersecurity internship at Brainwave Matrix Solutions**. The script analyzes the strength of passwords based on various security factors and provides suggestions for stronger passwords.
If you want only password strength checker without suggestion then the code is present in "Other codes" section

## Features
- **Evaluates password security** based on length, complexity, and uniqueness.
- **Checks against common passwords** from `rockyou.txt`.
- **Provides real-time feedback** to enhance weak passwords.
- **Generates a stronger password** suggestion if the input password is weak.

## Installation & Usage
### Prerequisites
- Python 3.x
- A password list file (`rockyou.txt`) for detecting common passwords. You can download it from [WeakPass](https://weakpass.com/) or other sources.

### Running the Script
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/password-strength-checker.git
   cd password-strength-checker
   ```
2. Ensure `rockyou.txt` is in the same directory.
3. Run the script:
   ```bash
   python Password_Strength_Checker.py
   ```

### Example Output
```
Enter a password: password123
Password Strength: Weak
How to improve:
- Use a more unique password that isn't found in common password lists.
- Add a special character like @, #, $, etc.
Suggested Stronger Password: Pa$$word123!
```

### Exiting the Script
Type `exit` when prompted to quit the script.

## Disclaimer
This tool is intended for **educational and security awareness purposes only**. Do not use it for unauthorized security testing.

## License
MIT License

