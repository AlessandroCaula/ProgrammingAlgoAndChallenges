#################
## Not Yelling ##
#################

# Create a function that transforms sentences ending with multiple question marks ? or exclamation marks ! into a sentence only ending with one without changing punctuation in the middle of the sentences.
# 
# Examples:
# 
# noYelling("What went wrong??????????")
# # output = "What went wrong?"
# 
# noYelling("Oh my goodness!!!")
# output = "Oh my goodness!"
# 
# noYelling("I just!!! can!!! not!!! believe!!! it!!!")
# output = "I just!!! can!!! not!!! believe!!! it!"
# # Only change repeating punctuation at the end of the sentence.
# 
# noYelling("Oh my goodness!")
# output = "Oh my goodness!"
# # Do not change sentences where there exists only one or zero exclamation marks/question marks.

def noYelling(sentence: str) -> str:
    # Retrieve the last punctuation
    last_punct = sentence[len(sentence) - 1]
    count = 0
    # loop the string from the end of the sentence
    for i in range(len(sentence) - 1, -1, -1):
        # count the number of last_punct from the end of the sentence
        if sentence[i] == last_punct:
            count += 1
        else:
            break
    # remove the last punctuations, leaving only one
    final_sentence = sentence[:len(sentence) - count + 1]
    return final_sentence

print(noYelling("What went wrong?????????"))
print(noYelling("Oh my goodness!!!"))
print(noYelling("I just!!! can!!! not!!! believe!!! it!!!"))
print(noYelling("Oh my goodness!"))