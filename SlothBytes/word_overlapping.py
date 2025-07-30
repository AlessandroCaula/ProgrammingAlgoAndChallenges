######################
## Word Overlapping ##
######################

# Given two words, overlap them in such a way, morphing the last few letters of the first word with the first few letters for the second

# Return the shortest overlapped word possible 

# EXAMPLE
# 
# overlap("sweden", "denmark")
# output = "swedenmark"
# 
# overlap("honey", "milk")
# output = "honeymilk"
# 
# overlap("dodge", "dodge")
# output = "dodge"

# NOTES
# 
# - All words will be given in lowercase
# 
# - If no overlap is possible, return both words one after the other (example #3).

def overlap(word1: str, word2: str) -> str:
    overlapped_word = ""

    # Loop through the first word
    j = 0
    for i in range(len(word1)):
        if word1[i] == word2[j]:
            j += 1
        else:
            j = 0
        overlapped_word += word1[i]
    
    # Add the remaining of the word2
    for z in range(j, len(word2)):
        overlapped_word += word2[z]

    return overlapped_word


print(overlap("sweden", "denmark"))
print(overlap("honey", "milk"))
print(overlap("dodge", "dodge"))