#####################
## Next Happy Year ##
#####################

# Sloth needs your help to find out the next happy year.abs
# A Happy Year is the year with only distinct digits (no duplicates).abs
# Create a function that takes an integer year and returns the next happy year. 
# 
# EXAMPLES
# 
# happyYear(2017)
# output = 2018
# # 2018 is the next happy year with all numbers being different.
# 
# happyYear(1990)
# output = 2013
# # 2013 is the next happy year with all numbers being different.
# 
# happyYear(2021)
# output = 2031
# # 2031 is the next happy year with all numbers being different.

def happyYear(year: int):
    while True:
        year += 1 
        # convert year to string
        year_str = str(year)
        if len(year_str) == len(set([s for s in year_str])):
            return year

print(happyYear(2017))
print(happyYear(1990))
print(happyYear(2021))