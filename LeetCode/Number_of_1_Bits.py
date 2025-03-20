######################
## Number of 1 Bits ##
######################

# Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

# Example 1:
#
# Input: n = 11
# Output: 3
# Explanation:
# The input binary string 1011 has a total of three set bits. 
#
#
# Example 2
# Input: n = 2147483645
# Output: 30
# Explanation:
# The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

# SOLUTION
# To count the number of set bits (1s) in a binary number, we can use Brian 

def number_of_bits(n: int) -> int:
    # Converting the int to a binary string
    binary_string = f"{n:032b}"
    count = 0
    print('Binary string', binary_string)
    # Loop through all the char values, count how many 1s there are 
    for c in binary_string:
        if (c == '1'):
            count += 1
    return f'Number of Bits: {count}'


n = 11
print(number_of_bits(n))

n = 2147483645
print(number_of_bits(n))