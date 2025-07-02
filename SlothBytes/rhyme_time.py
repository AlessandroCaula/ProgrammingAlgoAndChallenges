################
## Rhyme Time ##
################

# Create a function that returns true if two lines rhyme and false otherwise. For the purpose of this exercise, two lines rhyme if the last word from each sentence contains the same vowels. 
# 
# EXAMPLES
# 
# doesRhyme("Sam I am!", "Green eggs and ham.")
# output = True
# doesRhyme("Sam I am!", "Green eggs and HAM.")
# output = True
# # Capitalization and punctuation should not matter.
# doesRhyme("You're built like a seat", "I bet you like to eat")
# output = True
# doesRhyme("You are off to the races", "a splendid day.")
# output = False
# doesRhyme("and frequently do?", "you gotta move.")
# output = False

def doesRhyme(first_line: str, second_line: str) -> bool:
    # Split the first and second line.
    first_line_split = first_line.split(" ")
    second_line_split = second_line.split(" ")
    # Retrieve the last word of the first and second line.
    last_first_line = first_line_split[len(first_line_split) - 1]
    last_second_line = second_line_split[len(second_line_split) - 1]
    # Retrieve and store only the vowels of the last word.
    vowels_list = ["a", "e", "i", "o", "u"]
    vowels_first = ""
    vowels_second = ""
    # Loop thorough the characters in the last word of the first line. 
    for ch in last_first_line:
        if ch.isalpha():
            ch = ch.lower()
            # Check if the character is a vowel
            if ch in vowels_list:
                vowels_first += ch
    # Loop through the characters in the last word of the second line. 
    for ch in last_second_line:
        if ch.isalpha():
            ch = ch.lower()
            # Check if the character is a vowel
            if ch in vowels_list:
                vowels_second += ch

    return vowels_first == vowels_second

print(doesRhyme("Sam I am!", "Green eggs and ham."))
print(doesRhyme("Sam I am!", "Green eggs and HAM."))
print(doesRhyme("You're built like a seat", "I bet you like to eat"))
print(doesRhyme("You are off to the races", "a splendid day."))
print(doesRhyme("and frequently do?", "you gotta move."))