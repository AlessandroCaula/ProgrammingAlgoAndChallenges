#######################
## Splitting Numbers ##
#######################

# Create a function that takes a number num and returns each place value in the number. 
#
# Examples:

# num_split(39)
# output =[30, 9]

# num_split(-434)
# output = [-400, -30, -4]

# num_split(100)
# output =[100, 0, 0]

def num_split(num:int): 
    is_negative = True if num < 0 else False
    num_list = [el for el in str(num) if el != "-"]
    final_list = []
    if is_negative:
        num_list = ["-" + el for el in num_list]
    for i, el in enumerate(num_list):
        if el != 0:
            el = el + ("0" * (len(num_list) - 1 - i))
        final_list.append(int(el))
    return final_list
    
print(num_split(39))

print(num_split(-434))

print(num_split(100))