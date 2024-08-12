# Day 47

## Save a JSON

'''
Write a function called save_json. This function takes a dictionary below as an argument and saves it on a file in JSON format.

Wrtie another function called read_json that opens the file that you just saved and reads its content.
'''

import json

# Create and save a Json file.
def save_json(names):
    with open('d:/PythonScripts/ProgrammingAlgoAndChallenges/50_PythonChallenges/Day_47_names.json', 'w') as json_to_written:
        # Saving to file and adding indent
        json.dump(names, json_to_written, indent=4)

names = {"name": "Carol", "sex": "female", "age": 55}
print(save_json(names))

# Second function, Open and Read the Json. 
def read_json():
    with open('d:/PythonScripts/ProgrammingAlgoAndChallenges/50_PythonChallenges/Day_47_emails.json', 'r') as json_to_read:
        json_file = json.load(json_to_read)
    return json_file

print(read_json())