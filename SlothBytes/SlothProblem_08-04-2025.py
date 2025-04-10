########################
## Sticky Keys Typing ##
########################

# Someone is typing on the sticky keyboard. Occasionally a key gets stuck and more than intended number of characters of a particular letter is being added into the string. 
# The function input contains original and typed strings. 

# Determine if the typed string has been made from the original. Return true if it is and false if the typed string cannot have been made from the original. 

# EXAMPLE
#
# function: isLongPressed(original, typed)
# isLongPressed("alex", "aaleex")
# output = true
#
# isLongPressed("saeed", "ssaaedd")
# original contains 2 E's, but the typed only has 1. Not a sticky key issue.
# output = false
#
# isLongPressed("leelee", "lleeelee") 
# output = true
#
# isLongPressed("Tokyo", "TTokkyoh") 
# #An h was typed, not a sticky key problem, just skill issues.
# output = false
#
# isLongPressed("laiden", "laiden") 
# output = true


def isLongPressed(original: str, typed: str) -> bool:
    original_letters, original_count = count_occurrence(original)
    typed_letters, typed_count = count_occurrence(typed)

    # If they have different length, then return False
    if len(original_letters) != len(typed_letters): return False

    # Loop through each of the letters and their count. 
    for i, let in enumerate(original_letters):
        # If the letters are different between the original and the typed. Then, return False
        if original_letters[i] != typed_letters[i]:
            return False
        # If the count of the letters in the typed is lower, then return False
        if original_count[i] > typed_count[i]:
            return False

    return True


def count_occurrence(world: str) -> list:
    letters_order = []
    letters_count = []
    prev = ''
    for i, let in enumerate(world):
        if prev != let:
            letters_order.append(let)
            letters_count.append(1)
            prev = let
        else:
            letters_count[len(letters_count) - 1] += 1
    return letters_order, letters_count


# print(isLongPressed("alex", "aaleex"))
# print(isLongPressed("saeed", "ssaaedd"))
# print(isLongPressed("leelee", "lleeelee")) 
print(isLongPressed("Tokyo", "TTokkyoh"))



def isLongPressed1(original: str, typed: str) -> bool:
    # If the typed string has more different letters than the original. False needs to be returned
    if len(set(typed)) > len(set(original)):
        return False
    j = 0
    for i, curr_orig in enumerate(original):
        curr_typed = typed[j]
        if curr_orig != curr_typed:
            return False
        while curr_orig == typed[j] and j < len(typed) - 1:
            j += 1
    return True


# print(isLongPressed1("alex", "aaleex"))
# print(isLongPressed1("saeed", "ssaaedd"))
# print(isLongPressed1("leelee", "lleeelee")) 
# print(isLongPressed1("Tokyo", "TTokkyoh"))


def isLongPressed2(original: str, typed: str) -> bool:
    # If the typed string has more different letters than the original. False needs to be returned
    if len(set(typed)) > len(set(original)):
        return False
    j = 0
    i = 0
    while (j <= len(typed) - 1 or i <= len(original) - 1):
        curr_origin = original[i]
        curr_typed = typed[j]
        if curr_origin != curr_typed:
            return False
        count_origin = 0
        count_typed = 0
        # Count the occurrences of the same (current) letter in this part of the original word
        while i < len(original) and original[i] == curr_origin:
            count_origin += 1
            i += 1
        # Count the occurrences of the same (current) letter in this part of the typed word
        while j < len(typed) and typed[j] == curr_typed:
            count_typed += 1
            j += 1
        
        # The letter count of the typed word needs to be higher than the origin, to ensure that is a keyboard problem.
        if count_typed < count_origin:
            return False

    return True


# print(isLongPressed2("alex", "aaleex"))
# print(isLongPressed2("saeed", "ssaaedd"))
# print(isLongPressed2("leelee", "lleeelee")) 
# print(isLongPressed2("Tokyo", "TTokkyoh"))