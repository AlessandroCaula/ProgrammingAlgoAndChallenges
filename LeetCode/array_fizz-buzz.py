# LEETCODE-STYLE INTERVIEW EXAMPLE

# Write an algorithm that takes an array of numbers as an argument and return the same array. If an element in the array is a multiple of three, the output should be "fizz". If an element in the array is a multiple of five, the output value should be "buzz". If an element in the array is a multiple of both three and five, the output value should be "fizzbuzz"

# In computing, the modulo operation returns the remainder or signed remainder of a division, after one number is divided by another, called the modulus of the operation. 
# For example, the expression "5 mod(%) 2" evaluates to 1, because 5 divided by 2 has a quotient of 2 and a remainder of 1 (2 * 2 = 4 + 1 = 5), while "9 mod(%) 3" would evaluate to 0, because 9 divided by 3 has a quotient of 3 and a remainder of 0.

def fizz_buzz(arr: list) -> list:
    for i, el in enumerate(arr):
        fizz_buzz_str = ""
        if el % 3 == 0:
            fizz_buzz_str += "fizz"
        if el % 5 == 0:
            fizz_buzz_str += "buzz"
        arr[i] = fizz_buzz_str if fizz_buzz_str != "" else arr[i]
    return arr

print(fizz_buzz([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))