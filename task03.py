import re

def assess_password_strength(password):
    """Assess the strength of a password and provide feedback."""
    score = 0
    feedback = []

    # Criteria checks
    length_ok = len(password) >= 8
    upper_ok = re.search(r'[A-Z]', password) is not None
    lower_ok = re.search(r'[a-z]', password) is not None
    digit_ok = re.search(r'\d', password) is not None
    special_ok = re.search(r'[^A-Za-z0-9]', password) is not None

    # Scoring based on criteria
    if length_ok:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if upper_ok:
        score += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    if lower_ok:
        score += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    if digit_ok:
        score += 1
    else:
        feedback.append("Password should include at least one number.")

    if special_ok:
        score += 1
    else:
        feedback.append("Password should include at least one special character.")

    # Strength feedback
    if score == 5:
        strength = "Strong"
        feedback.append("Your password is strong.")
    elif score >= 3:
        strength = "Medium"
        feedback.append("Your password is medium. Consider improving it.")
    else:
        strength = "Weak"
        feedback.append("Your password is weak. Please improve it.")

    return {
        "strength": strength,
        "score": score,
        "feedback": feedback
    }

# Example usage
if __name__ == "__main__":
    pwd = input("Enter your password: ")
    result = assess_password_strength(pwd)
    print(f"Strength: {result['strength']}")
    for msg in result['feedback']:
        print("- " + msg)