###########################
### Ctrl + C, Ctrl + V ####
###########################

# Given a sentece containing few instances of  "Ctrl + C" and "Ctrl + V", return the sentence after those keyboard shortcuts have been applied.
#
# - "Ctrl + C" => Will copy all text behing it. 
# - "Ctrl + V" => Will do nothing if there is no "Ctrl + C" before it. 
# - "Ctrl + C" => Which follows another "Ctrl + C" will overwrite what ir copies.
#
#
# #Example 1
# keyboardShortcut("the egg and Ctrl + C Ctrl + V the spoon") 
# output = "the egg and the egg and the spoon"

# #Example 2
# keyboardShortcut("WARNING Ctrl + V Ctrl + C Ctrl + V")
# output=  "WARNING WARNING"

# #Example 3
# keyboardShortcut("The Ctrl + C Ctrl + V Town Ctrl + C Ctrl + V")
# output = "The The Town The The Town"
#
# - Keyboard shortcut commands will appear like normal words in a sentence but shouldn't be copied themselves (see example #2).
# - Pasting should add a space between words.

def keyboardShortcut(text: str):
    text_split = text.split(" ")
    text_to_copy = ""
    final_text = ""
    is_copied = False
    i = 0
    while i < len(text_split):
        word = text_split[i]
        if word == "Ctrl":
            command = text_split[i] + " " + text_split[i+1] + " " + text_split[i+2]
            # If the command is "Ctrl + C" turn to true the isCopied flag. 
            if command == "Ctrl + C":
                text_to_copy = final_text
                is_copied = True
            # If the command is "Ctrl + V" copy the previous text to copy.
            elif command == "Ctrl + V":
                if is_copied:
                    final_text += text_to_copy
                is_copied = False
            # Increase the i counter, to skip the command. 
            i += 3
        # If there is no command ("Ctrl + C" or "Ctrl + V") just add the current word in the finalText. 
        else:
            final_text += word + " "
            i += 1
    return final_text
        
print(keyboardShortcut("The egg and Ctrl + C Ctrl + V the spoon"))

print(keyboardShortcut("The Ctrl + C Ctrl + V Town Ctrl + C Ctrl + V"))

print(keyboardShortcut("This will be copied Ctrl + C This should not be copied Ctrl + V"))