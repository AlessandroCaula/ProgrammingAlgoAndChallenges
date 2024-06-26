######################
# Challenge 25/06/2024
######################

# Create a function that creates a box based on dimension n.
#
# makeBox(5) ➞ [
#   "#####",
#   "#   #",
#   "#   #",
#   "#   #",
#   "#####"
# ] 5x5 box

# makeBox(3) ➞ [
#   "###",
#   "# #",
#   "###"
# ] 3x3 box

# makeBox(2) ➞ [
#   "##",
#   "##"
# ] 2x2 box

# makeBox(1) ➞ [
#   "#"
# ] 1x1 box

def makeBox(n):
    # Create first and last row
    first_and_last_row = ""
    for i in range(n):
        first_and_last_row + "#"
    # Create middle row