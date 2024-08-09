# Day 24

## Average Calories

'''
Create a function called average_calories that calculates the average calories intake of a user. The function should ask the user to input their calories intake for any number of days and once they hit done, it should calculate and return the average intake. 
'''

def average_calories():
    calories_list = []
    while True:
        cal = input("Insert your calories intake ('done' for the result): ")
        if cal == "done": 
            break
        else:
            if cal.isdigit(): calories_list.append(float(cal))

    return f"Yuor average intake is: {sum(calories_list) / len(calories_list)}"

print(average_calories())