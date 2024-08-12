# Day 44

## Save Emails

'''
Create a function called save_emails. This function takes no arguments but asks the user to input email, and it saves the emails in a CSV file.
The user can input as many emails as they want. Once they hit 'done' the function saves the emails and closes the file.
Create another function called open_emails. This function opens and reads the content of the CSV file. Each email must be in its line. 
Here is an example of how the emails must be saved: 
jj@gmail.com 
kate@yahoo.com 
and not like this : 
jj@gmail.comkate@yahoo.com
'''

def save_emails():
    with open('d:/PythonScripts/ProgrammingAlgoAndChallenges/50_PythonChallenges/Day_44_emails.csv', 'w') as file_to_write:
        while True:
            email = input("Insert e-mail (done to close): ")
            if email == "done":
                break
            else:
                file_to_write.write(email + "\n")
        file_to_write.close()

def read_emails():
    with open('d:/PythonScripts/ProgrammingAlgoAndChallenges/50_PythonChallenges/Day_44_emails.csv', 'r') as file_to_read:
        return file_to_read.read()

save_emails()
print()
print("Email Inserted:")
print()
print(read_emails())