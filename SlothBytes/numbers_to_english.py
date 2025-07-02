#################################
#### Numbers to English #########
#################################

# Write a function that accepts a positive integer between 0 and 999 inclusvie and returns a string representation of that integer written in English.
#
# EXAMPLES
# numToEng(0)
# output = "zero"

# numToEng(18)
# output = "eighteen"

# numToEng(126)
# output = "one hundred twenty six"

# numToEng(909)
# output = "nine hundred nine"
# 
# There are no hyphens used (e.g. "thirty five" not "thyrty-five")
# The word "and" is not used. (e.g. "one hundred one" not "one hundred and one")


def numToEng(int_number: int):
    # create a dictionary which contains the conversion to string of the most usefult integere number
    int_to_string_number = {
        "0": ["zero"], "1": ["one"], "2": ["two", "twenty"], "3": ["three", "thirty"], "4": ["four"], "5": ["five", "fifty"], "6": ["six"], "7": ["seven"], "8": ["eight"], "9": ["nine"],
        "10": ["ten"], "11": ["eleven"], "12": ["twelve"], "13": ["thirteen"], "15": ["fifteen"]
    }
    
    # Initialize the final string variable which will contain the converted number to string. 
    final_string_number = ""
    
    # Convert the interger input number to string. 
    str_number = str(int_number)
    # loop the digits of the input integer number from left to right. 
    for i in range(len(str_number)):
        digit = str_number[i]
        # Set the inverted index as if it indicates in which power we are right now. Like 
        inverted_i = len(str_number) - i - 1       
        # Check the length of the number at the current digit. If we are dealing with a tens (teens), hundreds, thousands number. 
        # 
        # - Thousands 
        if inverted_i == 3 and digit != "0":
            final_string_number += int_to_string_number[digit][0] + " thousand "
        # - Hundreds
        if inverted_i == 2 and digit != "0":
            final_string_number += int_to_string_number[digit][0] + " hundred "
        # - Teens (Tens)
        if inverted_i == 1 or inverted_i == 5 and digit != "0":
            # Check if the entire teens number is present in the dictionary. I.e. 10, 11, 12, 13, 15. 
            if str_number[i:] in int_to_string_number:
                final_string_number += int_to_string_number[str_number[i:]][0]
                return final_string_number
            # If it is not entirely defined in the dictionary, construct it.
            else:
                # Check if it is a teen (between 10 and 19) or a Tens (20, 30, 40, etc.)
                if digit == "1":
                    final_string_number += int_to_string_number[str_number[i + 1]][0] + "teen"
                    return final_string_number
                elif digit != "0":
                    final_string_number += (int_to_string_number[digit][1] if len(int_to_string_number[digit]) > 1 else int_to_string_number[digit][0] + "ty ")
                    if str_number[i + 1] != "0":
                        final_string_number += " " + int_to_string_number[str_number[i + 1]][0]
                    return final_string_number
        # - Decimal-digits
        if inverted_i == 0:
            if digit == "0":
                if len(str_number) == 1:
                    final_string_number += int_to_string_number[digit][0]
            else:
                final_string_number += int_to_string_number[digit][0]

    return final_string_number
    
# print(numToEng(54000))


#######################
## Up to 1 million.####
#######################
#
def numToEng1(int_number: int):
    # create a dictionary which contains the conversion to string of the most usefult integere number
    int_to_string_number = {
        "0": ["zero"], "1": ["one"], "2": ["two", "twenty"], "3": ["three", "thirty"], "4": ["four"], "5": ["five", "fifty"], "6": ["six"], "7": ["seven"], "8": ["eight"], "9": ["nine"],
        "10": ["ten"], "11": ["eleven"], "12": ["twelve"], "13": ["thirteen"], "15": ["fifteen"]
    }
    # Initialize the final string variable which will contain the converted number to string. 
    final_string_number = ""
    # Convert the interger input number to string. 
    str_number = str(int_number)
    # loop the digits of the input integer number from left to right. 
    for i in range(len(str_number)):
        digit = str_number[i]
        # Set the inverted index as if it indicates in which power we are right now. 
        inverted_i = len(str_number) - i - 1       
        # Check the length of the number at the current digit. If we are dealing with a tens (teens), hundreds, thousands number. 
        # 
        # - Million 
        if inverted_i == 6:
            final_string_number += int_to_string_number[digit][0] + " million "
        # - Thousands 
        if inverted_i == 3:
            if len(str_number) > 4:
                final_string_number += " thousand "
            elif digit != "0":
                final_string_number += int_to_string_number[digit][0] + " thousand "
        # - Hundreds
        if (inverted_i == 2 or inverted_i == 5) and digit != "0":
            final_string_number += int_to_string_number[digit][0] + " hundred "
        # - Teens (Tens)
        if (inverted_i == 1 or inverted_i == 4) and digit != "0":
            # Check if the entire teens number is present in the dictionary. I.e. 10, 11, 12, 13, 15. 
            if str_number[i:i + 2] in int_to_string_number:
                final_string_number += int_to_string_number[str_number[i:i + 2]][0]
                if len(str_number) <= 4:
                    return final_string_number
            # If it is not entirely defined in the dictionary, construct it.
            else:
                # Check if it is a teen (between 10 and 19) or a Tens (20, 30, 40, etc.)
                if digit == "1":
                    final_string_number += int_to_string_number[str_number[i + 1]][0] + "teen"
                    if len(str_number) <= 4:
                        return final_string_number
                elif digit != "0":
                    final_string_number += (int_to_string_number[digit][1] if len(int_to_string_number[digit]) > 1 else int_to_string_number[digit][0] + "ty ")
                    if str_number[i + 1] != "0":
                        final_string_number += " " + int_to_string_number[str_number[i + 1]][0]
                    if len(str_number) <= 4:
                        return final_string_number
        # - Decimal-digits
        if inverted_i == 0:
            if digit == "0":
                if len(str_number) == 1:
                    final_string_number += int_to_string_number[digit][0]
            else:
                final_string_number += int_to_string_number[digit][0]

    return final_string_number
    
print(numToEng1(1150003))


def numToEng2(int_number: int):
    # create a dictionary which contains the conversion to string of the most usefult integere number
    single_digits = {
        "0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine",
    }
    teens = {
        "10": "ten", "11": "eleven", "12": "twelve", "13": "thirteen", "14": "frouteen", "15": "fifteen", "16": "sixteen", "17": "seventeen",  "18": "eighteen",  "19": "nineteen"
    }
    tens = {
        "20": "twenty", "30": "thirty", "40": "fourty", "50": "fifthy", "60": "sixty", "70": "seventy", "80": "eighty", "90": "ninety"
    }
    # Initialize the final string variable which will contain the converted number to string. 
    final_string_number = ""
    # Convert the interger input number to string. 
    str_number = str(int_number)
    i = 0
    # loop the digits of the input integer number from left to right. 
    while i < len(str_number):
        digit = str_number[i]
        # Set the inverted index as if it indicates in which power we are right now. 
        inverted_i = len(str_number) - i - 1       
        # Check the length of the number at the current digit. If we are dealing with a tens (teens), hundreds, thousands number. 
        # 
        # - Million 
        if inverted_i == 6:
            final_string_number += single_digits[digit] + " million "
            i += 1
        # - Thousands         
        if inverted_i == 3:
            if len(str_number) > 4:
                final_string_number += " thousand "
            elif digit != "0":
                final_string_number += single_digits[digit] + " thousand "
            i += 1
        # - Hundreds
        if (inverted_i == 2 or inverted_i == 5):
            if (digit != "0"):
                final_string_number += single_digits[digit] + " hundred "
            i += 1
        # - Teens (Tens)
        if (inverted_i == 1 or inverted_i == 4):
            if (digit != "0"):
                # Check if it is a teen (between 10 and 19) or a Tens (20, 30, 40, etc.)
                if digit == "1":
                    final_string_number += teens[str_number[i:i+2]] + " "
                elif digit != "0":
                    final_string_number += tens[str_number[i]+"0"] + " "
            if str_number[i + 1] == "0":
                i += 2
            else:
                i += 1
        # - Decimal-digits
        if inverted_i == 0:
            final_string_number += single_digits[digit]
            i += 1

    return final_string_number
    
print(numToEng2(5703))