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
                if len(change_to_give) > 0 and sum(change_to_give) == tot_change_to_give:
                    for el in change_to_give:
                        change.remove(el)
                    change.append(money)
                else:
                    return False
    return True

print(lemonade([5, 5, 5, 10, 20]))