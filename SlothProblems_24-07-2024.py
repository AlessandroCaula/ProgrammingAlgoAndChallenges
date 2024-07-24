### Check If It's a Title ###
# Check if a string is formatted as a title. A itle string is when every word of the string start with a upper case letter. 
#
# Example
#
# checkTitle("A Mind Boggling Achievement") ➞ true
# 
# checkTitle("A Simple C++ Program!") ➞ true
# 
# checkTitle("Water is transparent") ➞ false


def checkTitle(title):
    # In order to check every word, first split the string/title in single words.
    title_split = title.split(' ')
    
    # Loop through all the words and check if they start with a capital letter.
    for word in title_split:
        # Convert the first letter to capital and check if is the same already present in the word. 
        capital_first_letter = word[0].upper()
        # Check if this capital letter, which is the first letter in the word, is equal to the letter in the word itself.
        # If it is not, means that at least one word does not start with a capital letter, therefore the title string is not a title.
        if (capital_first_letter != word[0]):
            return False
    return True


print(checkTitle("A Mind Boggling Achievement"))
print()
print(checkTitle("A Simple C++ Program!"))
print()
print(checkTitle("Water is transparent"))