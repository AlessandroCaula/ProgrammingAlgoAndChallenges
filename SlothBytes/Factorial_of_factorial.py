############################
## Factorial of Factorial ##
############################

# Create a function that takes an integer n and returns the factorial of factorials.
# See below examples for a better understanding:
# 
# Examples:
# 
# fact_of_fact(4)
# output = 288
# Explanation: 4! * 3! * 2! * 1! = 288
# 
# fact_of_fact(5)
# output = 34560
# fact_of_fact(6)
# output = 24883200

# Recursive Function used to return the simple factorial of a number
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

# Recursive Function used to compute the factorial of the other simple factorials.
def fact_of_fact(n):
    if n == 1:
        return 1
    return factorial(n) * fact_of_fact(n - 1)    

print(fact_of_fact(5))
print(fact_of_fact(6))
