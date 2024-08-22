# Day 39

## Password Generator

'''
Create a function called generate_password that generates any length of password for the user. The password should have a random mix of upper letters, lower letters, numbers, and punctuation symbols. 
The function should ask the user how strong they want the password to be. The user should pick from - weak, strong, and very strong. 
If the user picks weak, the function should generate a  5 character long password. If the user picks strong, generate an 8 character password and if they pick very strong, generate a 12 character password. 
'''
import random
import string

def generate_password():
    strong = input("Generate password (weak, strong, very strong): ")
    pssw_length = 0
    if strong == "weak":
        pssw_length = 5
    elif strong == "strong":
        pssw_length = 8
    else:
        pssw_length = 12
    pssw_generated = ""
    #Loop through the length of the password.
    # 0 = upper letter, 1 = lower letter, 2 = number, 3 = punctuation symbol
    used_let = [False, False, False, False]
    for el in range(pssw_length):
        if used_let.count(False) == pssw_length - len(pssw_generated):
            # Get what has still to be added:
            what_to_add = [i for i, val in enumerate(used_let) if val == False]
            random_val = random.choice(what_to_add)
            # If a upper letter (0) needs to be added:
            if random_val == 0:
                pssw_generated += chr(random.randint(ord('A'), ord('Z')))
                used_let[random_val] = True
            # If a lower letter (1) needs to be added:
            elif random_val == 1:
                pssw_generated += chr(random.randint(ord('a'), ord('z')))
                used_let[random_val] = True
            # If a lower letter (2) needs to be added:
            elif random_val == 2:
                pssw_generated += str(random.randint(0, 9))
                used_let[random_val] = True        
            # If a lower letter (3) needs to be added:
            elif random_val == 3:
                pssw_generated += random.choice(string.punctuation)
                used_let[random_val] = True 
        else:
            # Randomly choose what to add in the password, if a lower/upper case, number or punctuation.
            random_val = random.randint(0, 3)
            # If a upper letter (0) needs to be added:
            if random_val == 0:
                pssw_generated += chr(random.randint(ord('A'), ord('Z')))
                used_let[0] = True
            # If a lower letter (1) needs to be added:
            elif random_val == 1:
                pssw_generated += chr(random.randint(ord('a'), ord('z')))
                used_let[1] = True
            # If a lower letter (2) needs to be added:
            elif random_val == 2:
                pssw_generated += str(random.randint(0, 9))
                used_let[2] = True        
            # If a lower letter (3) needs to be added:
            elif random_val == 3:
                pssw_generated += random.choice(string.punctuation)
                used_let[3] = True 
    return pssw_generated

print(f"Your password is ====> {generate_password()}")


## Other solution: That does NOT ensure that there will be always all the elements, lower case, upper case, number and punctuation.

def generate_password1():
    a = string.ascii_letters + string.digits + string.punctuation
    password1 = []
    strong = input("Generate password (weak, strong, very strong): ")
    length = 0
    if strong == "weak":
        length = 5
    elif strong == "strong":
        length = 8
    else:
        length = 12
    for i in range(length):
        password = str(random.choice(a))
        password1.append(password)
    return ''.join(password1)
    
print(f"Other Generated (not always with all the requested constraints) Your password is ====> {generate_password1()}")
