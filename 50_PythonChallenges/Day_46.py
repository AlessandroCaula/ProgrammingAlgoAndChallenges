# Day 46

## Create a DataFrame

'''
Create a Dataframe using pandas. You are going to create a code to put the following into a Dataframe. You will use the information in the table below. 
Basically, you are going to recreate this table using panadas. Use the information in the table to recreate the table.
'''

import pandas as pd

def create_dataframe():
    data = {'Year': [2009, 2002, 2009, 2010, 2009], 'Title': ['Brothers', 'Spider-Man', 'WatchMen', 'Inception', 'Avatar'], 'Genre': ['Drama', 'Sci-fi', 'Drama', 'Sci-fi', 'Fantasy']}
    data_frame = pd.DataFrame(data=data)
    return data_frame

print(create_dataframe())