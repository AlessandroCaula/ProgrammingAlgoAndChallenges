######################
# Challenge 25/06/2024
######################
# TEST for PULL 
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
    final_box = ""
    # Create first and last row
    first_and_last_row = ""
    for i in range(n):
        first_and_last_row += "#"
    # Create middle rows
    middle_rows = ""
    for i in range(n):
        if i == 0 or i == n - 1:
            middle_rows += "#"
        else:
            middle_rows += " "
    for i in range(n):
        if i == 0 or i == n - 1:
            final_box += first_and_last_row 
            if i == 0:
                final_box += "\n"
            else: 
                final_box += ""
        else:
            final_box += middle_rows + "" + "\n"            
    return final_box

print(makeBox(5))


def makeBox1(n):
    final_box = ""
    # loop through the rows
    for row in range(n):
        row_string = ""
        # First and Last Rows
        if row == 0 or row == n - 1:
            for col in range(n):
                row_string += "#"
        # Middle rows
        else:
            for col in range(n):
                if col == 0 or col == n - 1:
                    row_string += "#"
                else:
                    row_string += " "
        if row != n - 1:
            row_string += "\n"
        final_box += row_string
    return final_box

print(makeBox1(5)) 
