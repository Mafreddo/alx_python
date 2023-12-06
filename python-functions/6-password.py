def validate_password(password):
    if(len(password)>7 and len(password)<9):
        lowerCase = False
        upperCase = False
        num = False

        for char in password:
            if(char.isdigit()):
                num = True
            if (char.islower()):
                lowerCase = True
            if (char.isupper()):
                upper = True
        return lowerCase and upperCase and num and special
    else:
        return False
    
print(validate_password("Abcd1234"))
print(validate_password("abc123"))
print(validate_password("Password 123"))
print(validate_password("password123"))