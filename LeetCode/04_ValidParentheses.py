# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([])"
# Output: true

# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

def validParentheses(string):
    parenthesis_dict = {")": "(", "]": "[", "}": "{"}
    stack_for_parentheses = []
    for i, p in enumerate(string):
        # If the parenthesis in the string are opened, add them to the stack. 
        if p in parenthesis_dict.values():
            stack_for_parentheses.append(p)
        # If the parenthesis are closed.
        else:
            # If the parenthesis is closed and no opened one has been inserted in the stack. 
            # Or the closed parenthesis do not correspond to the last opened parenthesis added in the stack, return false.
            if (len(stack_for_parentheses) == 0) or (parenthesis_dict[p] != stack_for_parentheses[len(stack_for_parentheses) - 1]):
                return False
            # If instead the closed parenthesis is correctly closing the last opened parenthesis, remove it from the stack and continue. 
            else:
                stack_for_parentheses.pop()
    # If all the parentheses have been correctly closed, return True.
    if len(stack_for_parentheses) == 0:   
        return True
    else:
        return False

s = "([])"
print(validParentheses(s))