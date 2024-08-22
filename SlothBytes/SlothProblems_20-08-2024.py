###################
## NEAREST VOWEL ##
###################

# Given a letter, created a funciton which returns the nearest vowel to the letter. If two vowels are equal distance to the given letter, return the earlier vowel.

# Examples

# nearest_vowel("b") 
# output = "a" # closest vowel is a
# nearest_vowel("s") 
# output = "u" # closest vowel is u
# nearest_vowel("c")
# output = "a" # closest vowel is a
# nearest_vowel("i")
# output = "i" # i is a vowel, so return itself

# Notes:
# - All letters will be given in lowercase. 
# - There will be no alphabet wrapping involved, meaning the closest vowel to "Z" should return "u", not "a".

import string

def nearest_vowel(letter):
    # Retrieve the colletion of all the letters of tge alphabet. 
    alphabet = list(string.ascii_lowercase)
    vowels = ['a', 'e', 'i', 'o', 'u']
    dist_curr = 0
    dist_prev = 0
    closest_vowel = ''
    if letter in vowels:
        return f"You have enetered a vowel: {letter}"
    for el in alphabet:
        if el in vowels:
            if closest_vowel == '':
                closest_vowel = el
            else:
                if dist_prev != 0:
                    dist_curr += 1
                    if dist_curr < dist_prev:
                        closest_vowel = el
                    return closest_vowel
                else:
                    closest_vowel = el
                    dist_curr = 0
        elif el == letter:
            dist_curr += 1
            dist_prev = dist_curr
            dist_curr = 0
        else:
            dist_curr += 1
    # if we have looped through all the letters of the alphabet and we have no returned any closest values yes, means that the consonant in input was between the last vowel 'u' and the final 'z'.
    return closest_vowel


print(nearest_vowel('m'))
        