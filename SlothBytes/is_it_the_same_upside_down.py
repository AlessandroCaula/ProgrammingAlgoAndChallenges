#################################
## Is It the Same Upside Down? ##
#################################

# The number 6090609 has a special property: if you turn the number upside down (imagine rotating your screen 180 degrees), you get 6090609 again.
# 
# Write a function that takes a string on the digits 0, 6, 9 and returns true if the number is the same upside down or false otherwise. 
# 
# EXAMPLES 
# 
# sameUpsideDown("6090609")
# output = true
# 
# sameUpsideDown("9669")
# output = false
# # Becomes 6996 when upside down
# 
# sameUpsideDown("9")
# output = false
# 
# sameUpsideDown("0")
# output = true
# 
# sameUpsideDown("6090609")
# output = true
# 
# sameUpsideDown("60906096090609")
# output = true
# 
# sameUpsideDown("966909669")
# output = false
# # Becomes 699606699 when upside down.
# 
# sameUpsideDown("96666660999999")
# output = false

def same_upside_down(number: str):
    # Rotate horizontally the number
    h_rotation = number[::-1]
    # Now replace the 6s with the 9s and the 9s with the 6s
    upside_down_number = ''
    for el in h_rotation:
        if el == '6':
            upside_down_number += '9'
        elif el == '9':
            upside_down_number += '6'
        else:
            upside_down_number += el

    return upside_down_number == number


print(same_upside_down("6090609"))
print(same_upside_down("9669"))
print(same_upside_down("9"))
print(same_upside_down("0"))
print(same_upside_down("6090609"))
print(same_upside_down("60906096090609"))
print(same_upside_down("966909669"))
print(same_upside_down("96666660999999"))

