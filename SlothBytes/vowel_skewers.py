###################
## Vowel Skewers ##
###################
# 23-07-2025

# An authentic vowel skewer with a delicious and juicy mix of consonants and vowels.
# However, the way they are made must be just right:
# 
# - Skewer must begin and end with a consonant
# - Skewer must alternate between consonants and vowels
# - There must be an even spacing between each letter on the skewer, so that there is a consistent flavour throughout.
# 
# Create a function which returns whether a given vowel skewer is authentic.
# 
# EXAMPLE:
# 
# is_authentic_skewer("B--A--N--A--N--A--S")
# output = True
# 
# is_authentic_skewer("A--X--E")
# output = False
# # Should start and end with a consonant.
# 
# is_authentic_skewer("C-L-A-P")
# output = False
# # Should alternate between consonants and vowels.
# 
# is_authentic_skewer("M--A---T-E-S")
# output = False
# # Should have consistent spacing between letters.
# 
# Notes:
# - All letters will be given in uppercase.
# - Strings without any actual skewer "-" or letters should return False.


def is_authentic_skewer(skewer):
    vowels = ['A', 'E', 'I', 'O', 'U']
    # Check if start and end are consonants
    if skewer[0] in vowels or skewer[len(skewer) - 1] in vowels:
        return False
    # Check if it alternates between vowels and consonants, as well as there is consistent spacing
    should_be_vowel = False
    found_skewer_format = False
    skewer_format = ""
    current_skewer = ""
    for letter in skewer:
        # if skewer_format == "" and letter == "-":
        #     skewer_format += letter
        if letter == "-":
            current_skewer += letter
        else:
            if skewer_format == "":
                skewer_format = current_skewer

            if skewer_format != "" and current_skewer != skewer_format:
                return False
            # Reset current_skewer
            current_skewer = ""

            # Current letter is a consonant
            if letter not in vowels:
                # If it was signed that it should be a vowel, than return False
                if should_be_vowel:
                    return False
                # Set that the next letter should be a vowel
                else:
                    should_be_vowel = True
            # Current letter is a vowel
            else:
                # If it should be a consonant, return False
                if not should_be_vowel:
                    return False
                # Set that the next letter should be a consonant, it should not be a vowel
                else:
                    should_be_vowel = False

    return True


print(is_authentic_skewer("B--A--N--A--N--A--S"))
print(is_authentic_skewer("A--X--E"))
print(is_authentic_skewer("C-L-A-P"))
print(is_authentic_skewer("C-A-L-A-P"))
print(is_authentic_skewer("M--A---T-E-S"))