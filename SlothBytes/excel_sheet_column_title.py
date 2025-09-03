##############################
## Excel Sheet Column Title ##
##############################
# 03-09-2025
# 
# Given a positive integer, return its corresponding column title displayed in Excel sheet
# 
# For example:
# 
'''
1 -> A
2 -> B
3 -> C
...
26 -> Z
27 -> AA
28 -> AB
...
'''
# 
# EXAMPLES
# 
'''
convert_to_title(1)
output = "A"

convert_to_title(18)
output = "R"

convert_to_title(28)
output = "AB"

convert_to_title(52)
output = "AZ"

convert_to_title(701)
output = "ZY"
convert_to_title(229704)
output = "MATT"
convert_to_title(209380622941)
output = "ZATOICHI"
'''

def convert_to_title(n: int) -> str:
    if n <= 0:
        return None
    
    letters = []
    while n > 0:
        n -= 1
        n, r = divmod(n, 26)    # r in 0.25
        letters.append(chr(ord('A') + r))
    return "".join(reversed(letters))

print(convert_to_title(229704))
print(convert_to_title(209380622941))

'''
STEP-BY-STEP BREAKDOWN

1. n = 229704
    - n -= 1 -> 229703
    - divmod(229703, 26) -> (8834, 19)
    - r = 19 -> chr(ord('A') + 19) = 'T'
    - letters = ['T']
2. n = 8834
    - n -= 1 -> 8833
    - divmod(8833, 26) -> (339, 19)
    - r = 19 -> 'T'
    - letters = ['T', 'T']
3. n = 339
    - n -= 1 -> 338
    - divmod(338, 26) -> (13, 19)
    - r = 0 -> 'A'
    - letters = ['T', 'T', 'A']
4. n = 13
    - n -= 1 -> 12
    - divmod(12, 26) -> (0, 12)
    - r = 12 -> 'M'
    - letters = ['T', 'T', 'A', 'M']
'''




# import string

# def convert_to_title1(column_idx: int) -> str:
#     alphabet = list(string.ascii_uppercase)

#     # Base case in which the column_id is less than the alphabet number
#     if column_idx < len(alphabet):
#         return alphabet[column_idx]

#     alphabet_idx = 0
#     counter = 26
#     flag = False
#     output = ['A', 'A']
#     i, j = 1, 1
#     while counter < column_idx:
#         if output[j] == 'Z':
#             while i >= 0:
#                 if output[i] != 'Z':
#                     # Increment the letter by one letter
#                     prev = alphabet.index(output[i])
#                     output[i] = alphabet[prev + 1]
#                     # output[i + 1] = 'A'
#                     # counter += 1
#                     alphabet_idx = 1
#                     # flag = True
#                     break
#                 else:
#                     output[i] = 'A'
#                     counter += 1

#                     i -= 1

#             # Add a new element possibility to the output if we have finished the possibilities in the current output length
#             if output.count('A') == len(output):
#                 j += 1
#                 output.append('A')
#                 alphabet_idx = 1
#                 counter += 1
#                 i = j - 1

#         else:
#             # Normally add the new letter
#             output[j] = alphabet[alphabet_idx]
#             # Increase the alphabet idx for the next iteration
#             alphabet_idx += 1
#             counter += 1

#     return output


# def convert_to_title(column_idx: int) -> str:
#     alphabet = list(string.ascii_uppercase)

#     # Base case in which the column_id is less than the alphabet number
#     if column_idx < len(alphabet):
#         return alphabet[column_idx]

#     alphabet_idx = 0
#     counter = 26
#     flag = False
#     output = ['A', 'A']
#     i, j = 1, 1
#     while counter < column_idx:
#         if output[j] == 'Z':
#             while i >= 0:
#                 if output[i] != 'Z':
#                     # Increment the letter by one letter
#                     prev = alphabet.index(output[i])
#                     output[i] = alphabet[prev + 1]
#                     # output[i + 1] = 'A'
#                     # counter += 1
#                     alphabet_idx = 1
#                     # flag = True
#                     break
#                 else:
#                     output[i] = 'A'
#                     counter += 1

#                     i -= 1

#             # Add a new element possibility to the output if we have finished the possibilities in the current output length
#             if output.count('A') == len(output):
#                 j += 1
#                 output.append('A')
#                 alphabet_idx = 1
#                 counter += 1
#                 i = j - 1

#         else:
#             # Normally add the new letter
#             output[j] = alphabet[alphabet_idx]
#             # Increase the alphabet idx for the next iteration
#             alphabet_idx += 1
#             counter += 1

#     return output

# print(convert_to_title(703))