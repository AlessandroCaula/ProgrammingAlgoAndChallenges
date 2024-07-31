### Write a function that sorts each string in a list by the letter in alphabetic ascending order (a-z) ###
#
# Examples:
#
#sort_by_letter(["932c", "832u32", "2344b"])
#output = ["2344b", "932c", "832u32"] 
#
#sort_by_letter(["99a", "78b", "c2345", "11d"])
#output = ["99a", "78b", "c2345", "11d"] 
#
#sort_by_letter(["572z", "5y5", "304q2"])
#output = ["304q2", "5y5", "572z"]
#
#sort_by_letter([])
#output = []
#
##here's your starting point :)
#def sort_by_letter(arr):
#
# Each string will only have one (lowercase) letter. 
# If given an empty list, return an empty list. 

def sort_by_letter(arr):
    #define the list with the letter of the alphabet:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    char_in_strings = []
    #loop through the string elements of the array.
    for i, string in enumerate(arr):
        #loop through the single character of the string in order to identify the letter. 
        for c in string:
            #check if the character in the string is a letter.
            if c.isalpha() == True:
                char_in_strings.append(c)
    #sort the letters found in the strings
    char_in_strings_sorted = sorted(char_in_strings)

    arr_sorted = []
    #loop thorough the sorted letters
    for let in char_in_strings_sorted:
        #loop through the not sorted letters and find their position in that not sorted array
        for i in range(len(char_in_strings)):
            if let == char_in_strings[i]:
                arr_sorted.append(arr[i])        
    return arr_sorted

arr = ["932c", "832u32", "2344b"] #["572z", "5y5", "304q2"]
print(sort_by_letter(arr))