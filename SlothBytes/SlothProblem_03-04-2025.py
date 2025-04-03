########################
## Message from Space ##
########################

# You have received an encrypted message from space. Your task is to decrypt the message with the following simple rules:
# - Message string will consist of capital letters, number, and brackets only
# - When there is a block of code inside the brackets, such as [10AB], it means you need to repeat the letters AB for 10 times. 
# - Message can be embedded in multiple layers of blocks. 
# - Final decrypted message will only consist of capital letters. 
#
# Create a function that takes encrypted message str and returns the decrypted message:
#
# Example:
# 
# SpaceMessage("ABCD")
# output = "ABCD"
# 
# spaceMessage("AB[3CD]")
# output = "ABCDCDCD"
# # "AB" = "AB"
# # "[3CD]" = "CDCDCD"
# # Combine both = "ABCDCDCD"

# spaceMessage("IF[2E]LG[5O]D")
# output = "IFEELGOOOOOD"

def spaceMessage(message: str) -> str:
    # loop through the letters of the message
    decrypted_message = ''
    in_brackets = False
    n_repeater = 0
    string_to_repeat = ''
    for i, l in enumerate(message):
        if not in_brackets and l != '[':
            decrypted_message += l
        # Check if the repeater has started
        elif l == '[':
            in_brackets = True
        # Check if we have reached the end of the repeater
        elif l == "]":
            # Repeat the string_to_repeat
            for i in range(n_repeater):
                decrypted_message += string_to_repeat
            # Reset everything
            in_brackets = False
            n_repeater = 0
            string_to_repeat = ''
        # Check if we are inside the "[]" for repetition
        elif in_brackets ==  True:
            if l.isnumeric():
                n_repeater = int(l)
            else:
                string_to_repeat += l

    return decrypted_message

print(spaceMessage("AB[3CD]"))
print(spaceMessage("IF[2E]LG[5O]D"))
