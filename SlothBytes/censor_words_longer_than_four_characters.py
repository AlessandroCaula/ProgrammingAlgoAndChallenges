##############################################
## Censor Words Longer Than Four Characters ##
##############################################

# Create a function that takes a string and censors words over four characters with *.

def censor(string: str):
    # Splitting the string
    string_list = string.split(" ")
    final_string = ""
    for i, s in enumerate(string_list):
        if len(s) <= 4:
            final_string += s 
            if i != len(string_list) - 1: final_string += " "
        else:
            censored_s = "".join(["*" for el in s])
            final_string += censored_s
            if i != len(string_list) - 1: final_string += " "
        
    return final_string;

print(censor("The code is fourty")) # output = "The code is ******"

print(censor("Two plus three is five"))

print(censor("aaaa aaaaa 1234 12345"))