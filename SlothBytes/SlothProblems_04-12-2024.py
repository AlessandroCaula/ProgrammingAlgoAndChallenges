####################
### Invert Color ###
####################

# # Create a function that inverts the rgb values of a given list. 
# 
# color_invert([255, 255, 255])
# output = [0, 0, 0]
# # [255, 255, 255] is the color white.
# # The opposite is [0, 0, 0], which is black.
# 
# color_invert([0, 0, 0])
# output = [255, 255, 255]
# 
# color_invert([165, 170, 221]
# output = [90, 85, 34]

def color_invert(initial_color:list):
    inverted_color = [abs(el - 255) for el in initial_color]
    return inverted_color

print(color_invert([255, 255, 255]))
print(color_invert([0, 0, 0]))
print(color_invert([165, 170, 221]))