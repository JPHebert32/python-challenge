# Python Challenges 
# PyPoll / main.py
# JP Hebert
#---------------------------------------------------------------------------------------------------------------
# You will be give a set of poll data called election_data.csv. 
# The dataset is composed of three columns: Voter ID, County, and Candidate.
# Your task is to create a Python script that analyzes the votes and calculates each of the following:

# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.
#---------------------------------------------------------------------------------------------------------------


# FIRST IMPORT MODULES
import os
import csv

# FIND FILE PATHS 
print(os.listdir('../'))

# ASSIGN FILE PATH
#C:\Users\JPHeb\JPH-Data-Class\du-den-data-pt-03-2020-u-c\Homework-3-Python\PyBank\Resources
csvpath = os.path.join('C:/Users/JPHeb/JPH-Data-Class/du-den-data-pt-03-2020-u-c/Homework-3-Python/PyPoll/Resources/election_data.csv')

# CREATE BLANK VARIABLES 
polling_info={}
casted_votes = 0
# OPEN ELECTION_DATA AS ELECTION_CSV
with open(csvpath) as election_csv:
    csvreader = csv.reader(election_csv, delimiter=",")

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"{csv_header}")

    for row in csvreader:
        casted_votes += 1
        print(casted_votes)
        print(len(row[0]))
    
