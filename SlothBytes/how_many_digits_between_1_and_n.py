#####################################
## How Many Digits between 1 and N ##
#####################################

# Imagine you took all the numbers between 0 and n and concatenated them together into long string. 
# 
# How many digits are there between 0 and n> Write a function that can calculate this.
# 
# There are 0 digits between 0 and 1, there are 9 digits between 0 and 10 and there are 189 digits between 0 and 100.
# 
# Examples
# 
# digits(1)
# output = 0

# digits(10)
# output = 9

# digits(100)
# output = 189

# digits(2020)
# output = 6969

def digits(number: int) -> int:
    digits_len = 0
    for n in range(1, number):
        digits_len += len(str(n))
    return digits_len

number = 2020
print(digits(number))

"12345678910"