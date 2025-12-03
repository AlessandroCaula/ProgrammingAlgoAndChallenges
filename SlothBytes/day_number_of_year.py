# Day Number of Year
# 
# 03-12-2025
# 
# You're given a date string in the format moth/day/year, based on the gregorian calendar (https://en.wikipedia.org/wiki/Gregorian_calendar).
# Your task is to return which day of the year that date corresponds to (1-365 or 1-366 for leap years).
# 
# Examples
# dayOfYear("12/13/2020")
# output = 348

# dayOfYear("11/16/2020")
# output = 321

# dayOfYear("1/9/2019")
# output = 9

# dayOfYear("3/1/2004")
# output = 61

# dayOfYear("12/31/2000")
# output = 366 # leap year
# dayOfYear("12/31/2019")
# output = 365 #non leap year 

def day_of_year(date: str) -> int:
    months_days = { 1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31 }

    date_month, date_day, date_year = date.split("/")
    date_month, date_day, date_year = int(date_month), int(date_day), int(date_year)

    tot_days = 0
    # count the days of the months before the one in the date
    for key, val in months_days.items():
        if key == date_month:
            break
        tot_days += months_days[key]
    
    # Add the days of the current month
    tot_days += date_day
    
    # Check if the current year is a leap year, in that case add 1 if february is included
    if date_month >= 2:
        if date_year % 400 == 0 or (date_year % 4 == 0 and date_year % 100 != 0):
            tot_days += 1

    return tot_days

print(day_of_year("1/9/2019"))
print(day_of_year("11/16/2020"))
print(day_of_year("12/31/2019"))