# Day 14

## Flatten the List

'''
Write a function called flat_list that takes one argument, a nested list. The function converts the nested list into a one-dimension list. 
For example [[2,4,5,6]] should return [2,4,5,6]
'''

def flat_list(list):
    final_linear_list = []
    for l in list:
        for el in l:
            final_linear_list.append(el)

    return final_linear_list

print(flat_list([[2,4,5,6]]))


## Extra Challenge: Teacher's Salary.
'''
A school has asked you to write a program that will calculate teachers' salaries. The program should ask the user to enter the teacher’s name, the number of periods taught in a month, and the rate per period. 
The monthly salary is calculated by multiplying the number of periods by the monthly rate. The current monthly rate per period is $20. If a teacher has more than 100 periods in a month, everything above 100 is overtime. Overtime is $25 per period. 
For example, if a teacher has taught 105 periods, their monthly gross salary should be 2,125. Write a function called your_salary that calculates a teacher’s gross salary. 
The function should return the teacher’s name, periods taught, and gross salary. Here is how you should format your output:

Teacher: John Kelly
Period: 105
Gross salary: 2125
'''

def your_salary():
    name = input("Teacher's name: ")
    num_periods = int(input("Number of Periods: "))
    rate_periods = int(input("Rate per Period: "))

    gross_salary = 0
    if (num_periods < 100):
        gross_salary = num_periods * rate_periods
    else:
        gross_salary = (100 * rate_periods) + ((num_periods - 100) * (rate_periods + 5))

    return f"{name} gross salary = {gross_salary} $"


print(your_salary())
