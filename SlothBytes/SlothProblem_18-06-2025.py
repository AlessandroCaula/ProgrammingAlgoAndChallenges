###########################
## Birthday Cake Candles ##
###########################

"""
You are in charge of the cake for a child's birthday. It will have one candle for each year of their total age. 
They will only be able to blow out the tallest of the candles.

The task is to count how many candles are the tallest. 

Examples:

birthdayCakeCandles([4,4,1,3])
output = 2
// The tallest candles are 4. There are 2 candles with this height, so the function should return 2.
birthdayCakeCandles([1, 1, 1, 1])
output = 4
// All candles are the same height, so all are the tallest.
birthdayCakeCandles([])
output = 0
// No candles, so nothing to blow out.
"""

def birthday_cake_candles(candles: list[int]) -> int:
    # If there are no candles, return 0
    if len(candles) == 0:
        return 0
    # Find max value (tallest candle). Count and return the occurrences of the tallest value    
    return candles.count(max(candles))

print(birthday_cake_candles([4,4,1,3]))
print(birthday_cake_candles([1,1,1,1]))
print(birthday_cake_candles([]))