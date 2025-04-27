# Write a function that divides a phrase into word buckets, with each bucket containing
# n or fewer character. Only includes full words inside each bucket.
#
# Examples
# 
# split_into_buckets("she sells sea shells by the sea", 10)
# output = ["she sells", "sea shells", "by the sea"]
# 
# split_into_buckets("the mouse jumped over the cheese", 7)
# output = ["the", "mouse", "jumped", "over", "the", "cheese"]

# split_into_buckets("fairy dust coated the air", 20)
# output = ["fairy dust coated", "the air"]

# split_into_buckets("a b c d e", 2)
# output = ["a", "b", "c", "d", "e"]

def split_into_buckets(phrase: str, max_length: int):
    # Split the phrase
    words_list = phrase.split(' ')
    char_count = 0
    word_bucket = []
    curr_bucket = ""
    for i, word in enumerate(words_list):
        if len(word) + char_count >= max_length:
            word_bucket.append(curr_bucket)
            curr_bucket = word
            char_count = len(word)
        else:
            if i == 0:
                curr_bucket += word
            else:
                curr_bucket += " " + word
            char_count += len(word)
    # Append the last created bucket
    word_bucket.append(curr_bucket)

    return word_bucket

print(split_into_buckets("she sells sea shells by the sea", 10))
print(split_into_buckets("the mouse jumped over the cheese", 7))
print(split_into_buckets("fairy dust coated the air", 20))
print(split_into_buckets("a b c d e", 2))