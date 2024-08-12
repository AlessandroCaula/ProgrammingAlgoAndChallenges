# Day 34

## Just Digits

'''
In this challenge, copy the text below and save it as a CSV file. Save it in the same folder as your python file. Save it as python.csv.
Write a function called just_digits that reads the text from the CSV file and returns only digit elements from the file. 
Your function should return 1991, 2, 200, 3, 2008 as a list of strings.

"
Python was released in 1991 for the first time. Python 2 was 
released in 2000 and introduced new features, such as list 
comprehensions and a cycle-detecting garbage collection system 
(in addition to reference counting). Python 3 was released in 2008 
and was a major revision of the language that is not 
completely backward-compatible.
"
Source:Wikipedia
'''

import csv

#def just_digits():
#    with open('python.csv', 'r') as file_to_open:
#        csv_reader = csv.reader(file_to_open)
#        for row in csv_reader:
#            print(row)
#    return


import pandas as pd
def just_digits():
    csv_file = open('D:/PythonScripts/ProgrammingAlgoAndChallenges/50_PythonChallenges/python.txt', 'r')
    for line in csv_file:
        print(line)

print(just_digits())


