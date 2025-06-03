# Enter your code here
import string 
def check_password_strength(password):
    score =0
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    
    if has_lower and not (has_upper or has_digit or has_special):
        score = 6
    elif has_lower and has_upper and has_digit and not has_special:
        score = 8
    elif has_lower and has_upper and has_digit and has_special:
        score = 10
    else:
        score = 6 # Default to weak if not matching srtonger critical
        
    if 6 <= score <= 7:
        return "week"
    elif 7 > score <= 8:
        return "strong"
    elif 8 < score <= 10:
        return "very strong"
print(check_password_strength("LIONtiger"))
print(check_password_strength("lionTIGER123"))
print(check_password_strength("lionTiger@123"))
    
    