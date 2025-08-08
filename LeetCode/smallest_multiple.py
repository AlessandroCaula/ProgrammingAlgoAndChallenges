# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the number from 1 to 20.

def smallest_divisible_up_to_n(n):
    smallest_divisible = n
    while True:
        is_found = True
        # Check if the number is divisible by all the numbers from 1 to 20
        for j in range(1, n + 1):
            if smallest_divisible % j != 0:
                is_found = False
                break
        if is_found:
            break
        else:
            smallest_divisible += n
    return smallest_divisible

print(smallest_divisible_up_to_n(20))