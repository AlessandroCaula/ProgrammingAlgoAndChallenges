#########################
### Convenience Store ###
#########################

# Given a total due and an array representing the amount of change in your pocket, determine whether or not you are able to pay for the item. 
#
# Change will always be represented in the following order: quarters, dimes, nickles, pennies.
#
# Example: changeEnough([25, 20, 5, 0], 4.25) return true because:
#
# 25 quarters, 20 dimes, 5 nickels and 0 pennies gives you 6.25 + 2 + .25 + 0 = 8.50.
#
# This means you can afford the item, so return true.
#
# Examples:
# changeEnough([2, 100, 0, 0], 14.11) ➞ false
# changeEnough([0, 0, 20, 5], 0.75) ➞ true
# changeEnough([30, 40, 20, 5], 12.55) ➞ true
# changeEnough([10, 0, 0, 50], 3.85) ➞ false
# changeEnough([1, 0, 5, 219], 19.99) ➞ false
#
# - quarter = 25 cents / $0.25
# - dime = 10 cents / $0.10
# - nickel = 5 cents / $0.05
# - penny = 1 cents/$0.02

def changeEnough(change: list, total_due: int):
    total_change = 0
    values = [0.25, 0.10, 0.05, 0.01]
    for i, val in enumerate(change):
        total_change += (change[i] * values[i])
    return total_change > total_due


change = [25, 20, 5, 0]
total_due = 4.25
print(changeEnough(change, total_due))

change = [30, 40, 20, 5]
total_due = 12.55
print(changeEnough(change, total_due))