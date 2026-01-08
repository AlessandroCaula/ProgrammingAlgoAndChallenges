# Write a function that removes the last vowel in each word in a sentence.
#
# Examples
#
# removeLastVowel("Those who dare to fail miserably can achieve greatly.")
# output = "Thos wh dar t fal miserbly cn achiev gretly."
#
# removeLastVowel("Love is a serious mental disease.")
# output = "Lov s  serios mentl diseas"
#
# removeLastVowel("Get busy living or get busy dying.")
# output = "Gt bsy livng r gt bsy dyng"
#
# removeLastVowel("If you want to live a happy life, tie it to a goal, not to people.")
# output = "f yo wnt t liv  hppy lif, ti t t  gol, nt t peopl."

def remove_last_vowel(sentence: str) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u']
    split_sentence = sentence.split(" ")
    sentence_without_vowel = ""
    for s in split_sentence:
        if s[len(s) - 1] == ".":
            s = s[: -1]
        if s[0].lower() in vowels:
            s = s[1:]
        if len(s) != 0 and s[len(s) - 1].lower() in vowels:
            s = s[: -1]

        sentence_without_vowel += s + " "

    return sentence_without_vowel


print(remove_last_vowel("Those who dare to fail miserably can achieve greatly."))
print(remove_last_vowel("Love is a serious mental disease."))
print(remove_last_vowel("Get busy living or get busy dying."))
print(remove_last_vowel(
    "If you want to live a happy life, tie it to a goal, not to people."))
