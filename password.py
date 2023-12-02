from random import randint

def get_random_password():
    password = ''
    for _ in range(0,8):
        random_ascii = randint(40,126)
        password += chr(random_ascii)
    return password
    
def is_valid_password(password):
    lenth = 0
    upper = 0
    lower = 0
    numeric = 0
    
    if len(password) == 8: 
        lenth = 8 
    for char in password:
        if char.isupper():
            upper += 1
        if char.islower():
            lower += 1
        if char.isnumeric():
            numeric += 1

    if lenth == 8 and upper >= 1 and lower >= 1 and numeric >= 1:
        return True
    else:
        return False

def get_password():
    count = 0 
    while count <= 100:
        final_password = get_random_password()
        if is_valid_password(final_password):
            return final_password
        else: 
            count += 1
        

print(get_password())
    