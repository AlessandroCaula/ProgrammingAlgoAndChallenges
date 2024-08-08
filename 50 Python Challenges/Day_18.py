# Day 18

## Any Number of Arguments

'''
Write a function called any_number that can receive any number of arguments(integers and floats) and return the average of those integers. 
If you pass 12, 90, 12, 34 as arguments your function should return 37.0 as average. If you pass 12, 90 your function should return 51.0 as average. 
'''

'''
In this exercise, you get to know about *args. You can use any word you want as a parameter as long as you use the * sign at the beginning of the word. 
However, it's a common convention to use args. The *args simply tells the function that we are not sure how many arguments we will need, so the function lets us add as many arguments as possible.
In *args make functions more flexible.
'''

def any_num(*args):
    average = sum(args) / len(args)
    return f"The average is {average}"

print(any_num(12, 34, 54, 234, 53))


##############################################
# Other solution by keep on asking to the user.

def any_num1():
    keep_asking = True
    total_sum = 0
    tot_numbers = 0
    while keep_asking:
        number = input("Inser number if you wanna add numbers to compute the average: ")
        if not number.isdigit():
            keep_asking = False
        else:
            number = float(number)
            total_sum += number
            tot_numbers += 1
    average = total_sum / tot_numbers
    return f"Final average is: {average}"

print(any_num1())