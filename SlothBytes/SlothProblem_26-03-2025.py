####################
## Lemonade Stand ##
####################

# At a lemonade stand, each lemonade costs $5
# 
# Customers are standing in a queue to buy from you, and order one at a time (in the order specified by bills).abs
# 
# Each customer will only buy one lemonade and pay with either a $5, $10 or $20 bill.abs
# 
# You need to give each customer the right amount of change so that they end up paying $5.
# 
# - For $5 bills: No change needed
# - For $10 bills: You need to give $5 back
# - For $20 bills: You need to give $15 back (best using one $10 and one $5, or three $5 bills)
# 
# Return true if and only if you can provide every customer with correct change.
#
# EXAMPLE
# 
# lemonade([5, 5, 5, 10, 20])
# """ 
# First three customers pay with $5: Now you have three $5 bills
# Fourth customer pays $10: You give $5 change, now have two $5 bills and one $10 bill
# Fifth customer pays $20: You can give $15 change (one $10 + one $5)
# """
# output = True
# 
# 
# lemonade([5, 5, 10, 10, 20])
# """ 
# First two customers pay with $5: Now you have two $5 bills
# Third customer pays $10: You give $5 change, now have one $5 bill and one $10 bill
# Fourth customer pays $10: You give $5 change, now have zero $5 bills and two $10 bills
# Fifth customer pays $20: You need to give $15 change but you can't because you only have $10 bills!
# """
# output = False
# 
# 
# lemonade([10, 10])
# output = False
# 
# 
# lemonade([5, 5, 10])
# output = True

def lemonade(arr: list) -> bool:
    change = []
    for money in arr:
        change.sort(reverse=True)
        # compute the sum of the entire change that we have:
        if money == 5:
            change.append(money)
        else:
            # Compute the amount of change that I have to give back to the client
            tot_change_to_give = money - 5

            # if the change to give is higher than the total change that you have, then return False
            if tot_change_to_give > sum(change):
                return False
            else:
                # Loop backward through 
                change_to_give = []
                for c in change:
                    if c <= tot_change_to_give and c + sum(change_to_give) <= tot_change_to_give:
                        change_to_give.append(c)
                    if tot_change_to_give == sum(change_to_give):
                        break
                if len(change_to_give) > 0 and sum(change_to_give) == tot_change_to_give:
                    for el in change_to_give:
                        change.remove(el)
                    change.append(money)
                else:
                    return False
    return True

print(lemonade([5, 5, 5, 10, 20]))
# print(lemonade([5, 5, 10, 10, 20]))
# print(lemonade([10, 10]))
# print(lemonade([5, 5, 10]))


# IMPROVEMENT
#
# Code inefficiencies
# 1. Sorting in Every iteration
#   - Sorting has an average time complexity of O(n log n). Since sort in every loop iteration, this makes the solution significantly slower than needed.
#   - Instead, it's better to use two counter (five and ten) instead of storing all bills in a list and sorting them.
# 2. Summing the Change List
#   - Summing a list takes O(n) time. 
#   - Since it is done repeatedly inside the loop, it makes the solution inefficient
#   - Instead, maintaining separate counter for $5 and $10 bills allows constant-time lookups
# 3. Looping through `change` to find change (for c in change)
#   - This is an unnecessary check when you can just use conditional logic to reduce the correct bills.
#   - The greedy approach (prioritizing $10 bills before $5 bills) ensures an optimal solution. 

def lemonade1(arr: list) -> bool:
    count_five, count_ten = 0, 0
    tot_change = 0
    
    for money in arr:
        if money == 5:
            count_five += 1
        elif money == 10:
            if count_five > 0:
                count_ten += 1
                count_five -= 1
            else:
                return False
        else: # if money is equal to 20
            # 15 $ change
            if count_ten > 0 and count_five > 0:
                count_five -= 1
                count_ten -=1
            elif count_five >= 3:
                count_five -= 3
            else:
                # There is no change 
                return False
    return True

# print(lemonade1([5, 5, 5, 10, 20]))
print(lemonade1([5, 5, 10, 10, 20]))
