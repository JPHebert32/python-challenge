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
#print(os.listdir('../'))

# ASSIGN FILE PATH
#C:\Users\JPHeb\JPH-Data-Class\du-den-data-pt-03-2020-u-c\Homework-3-Python\PyBank\Resources
csvpath = os.path.join('C:/Users/JPHeb/JPH-Data-Class/du-den-data-pt-03-2020-u-c/Homework-3-Python/PyPoll/Resources/election_data.csv')

#initializing the variables 
results = {}
total_votes = 0
candidates = []  
total_candidates_votes = []


# OPEN ELECTION_DATA AS ELECTION_CSV
with open(csvpath, 'r') as election_csv:
    csvread = csv.reader(election_csv)
    next(csvread, None)

    for row in csvread:
        total_votes += 1
        if row[2] in results.keys():
            results[row[2]] = results[row[2]] + 1
        else:
            results[row[2]] = 1 


# Find Total Number of votes for each Candidate
for key, value in results.items():
    candidates.append(key)
    print(candidates)                             # ['Khan', 'Correy', 'Li', "O'Tooley"]
    total_candidates_votes.append(value)
    print(total_candidates_votes)                 # [2218231, 704200, 492940, 105630]


