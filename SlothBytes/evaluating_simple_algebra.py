###############################
## Evaluating Simple Algebra ##
###############################
## 10/09/2025

# Given a string containing an algebraic equation, calculate and return the value of x.
# 
# You'll only be given equations for simple addition and subtraction.
# 
# EXAMPLES
# 
# eval_algebra("2 + x = 19")
# output = 17

# eval_algebra("4 - x = 1")
# output = 3

# eval_algebra("x + 10 = 53")
# output = 43

# eval_algebra("-23 + x = -20")
# output = 3

# eval_algebra("10 + x = 5")
# output = -5

# eval_algebra("-49 - x = -180")
# output = 131

# eval_algebra("x - 22 = -56")
# output = -34

# Notes
# - There are spaces between every number and symbol in the string.
# - x may be a negative number.

def eval_algebra(equation: str) -> int:
    # Split the equation by the spaces
    equation_split = equation.split(' ')
    
    # print(equation_split)

    # Loop through all the elements of the equation and compute the left and right arithmetics
    left_side_res, right_side_res, partial_res = 0, 0, 0
    operation, invert_sign = 1, 1

    for i, el in enumerate(equation_split):

        # Check if we have reached the '='
        if el == "=":
            left_side_res = partial_res
            operation = 1
            partial_res = 0
            continue

        if el == 'x':
            invert_sign = operation
            continue

        if el == "-" or el == "+":
            if el == "-":
                operation = -1
            else:
                operation = 1
            continue
        
        # Compute the partial result
        partial_res += (operation) * int(el)

        # Assign the result to the right side result if we have reached the end of the array
        if i == len(equation_split) - 1:
            right_side_res = partial_res
    
    # Compute the final result
    final_res = invert_sign * (right_side_res - left_side_res) 

    return final_res

print(eval_algebra("2 + x = 19"))
# output = 17
print(eval_algebra("4 - x = 1"))
# output = 3
print(eval_algebra("x + 10 = 53"))
# output = 43
print(eval_algebra("-23 + x = -20"))
# output = 3
print(eval_algebra("10 + x = 5"))
# output = -5
print(eval_algebra("-49 - x = -180"))
# output = 131
print(eval_algebra("x - 22 = -56"))
# output = -34