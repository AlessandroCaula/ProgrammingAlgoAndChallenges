# Day 12

## Count the Dots

'''
Write a function called count_dots. This function takes a string separated by dots as a parameter and counts how many dots are in the string. 
For example, ‘h.e.l.p.’ should return 4 dots, and ‘he.lp.’ should return 2 dots. 
'''

def count_dots(string):    
    return string.count('.')

string = "h.e.l.p."
print(count_dots(string))

'''
Write a function called age_in_minutes that tells a user how old they are in minutes. Your code should ask the user to enter their year of birth, and it should return their age in minutes (by subtracting their year 
of birth to the current year). Here are things to look out for:

    a. The user can only input a 4 digit year of birth. For example, 1930 is a valid year. However, entering any number longer or less than 4 digits long should render input invalid. Notify the user to input a 
    four digits number. 
    b. If a user enters a year before 1900, your code should tell the user that input is invalid. If the user enters the year after the current year, the code should tell the user, to input a valid year.

The code should run until the user inputs a valid year. Your function should return the user's age in minutes. For example, if someone enters 1930, as their year of birth your function should return: 
You are 48,355,200 minutes old.
'''

from datetime import datetime

def age_in_minutes():
    print("What is your year of birth?")
    year_of_birth = input()
    if len(year_of_birth) < 4 or int(year_of_birth) < 1900:
        return "Invalid year of birth"
    #Retrieve current year.
    current_year = datetime.now().year
    #Compute the age.
    years = current_year - int(year_of_birth)
    #Compute the days.
    days = years * 365
    #Compute the hours
    hours = days * 24
    #Compute the minutes
    minutes = hours * 60

    return "Your age in minutes is " + '{:,}'.format(minutes)

print(age_in_minutes())
