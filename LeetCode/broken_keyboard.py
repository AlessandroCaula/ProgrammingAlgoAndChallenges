#####################
## Broken Keyboard ##
#####################

# Given what is supposed to be typed and what is actually typed, write a function that returns the broken key(s).
# The function looks like this:
# 
# find_broken_keys(correct phrase, what you actually typed)
# 
# Examples:
# 
# find_broken_keys("happy birthday", "hawwy birthday") ➞ ["p"]
# 
# find_broken_keys("starry night", "starrq light") ➞ ["y", "n"]
# 
# find_broken_keys("beethoven", "affthoif5") ➞ ["b", "e", "v", "n"]
# 
# - Broken keys should be ordered by when they first appear in the sentence
# - Only one broken key per letter should be listed
# - Letters will all be in lower case

def find_broken_keys(correct: str, typed:str) -> list[str]:
    # Create a set from both the words (correct, typed), avoiding letters doubles
    correct_list_unique = []
    for l in correct:
        if l not in correct_list_unique and l != " ":
            correct_list_unique.append(l)

    typed_list_unique = []
    for l in typed:
        if l not in typed_list_unique and l != " ":
            typed_list_unique.append(l)
    
    broken_keys = []
    for i in range(len(correct_list_unique)):
        if correct_list_unique[i] != typed_list_unique[i]:
            broken_keys.append(correct_list_unique[i])

    return broken_keys

print(find_broken_keys("happy birthday", "hawwy birthday"))
print(find_broken_keys("starry night", "starrq light"))
print(find_broken_keys("beethoven", "affthoif5"))