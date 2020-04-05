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
        total_votes += 1                            #ADD 1 TO TOTAL VOTES
        if row[2] in results.keys():
            results[row[2]] = results[row[2]] + 1
        else:
            results[row[2]] = 1 


# Find Total Number of votes for each Candidate
for key, value in results.items():
    candidates.append(key)
    #print(candidates)                             # ['Khan', 'Correy', 'Li', "O'Tooley"]
    total_candidates_votes.append(value)
    #print(total_candidates_votes)                 # [2218231, 704200, 492940, 105630]

# Find Percentage of votes for each Candidate
    percentage_votes = []
    for i in total_candidates_votes:
        percentage_votes.append(round(i/total_votes * 100, 1))
        #print(percentage_votes)                      #  [63.0, 20.0, 14.0, 3.0]
 
    # Zip list together for final results
    offical_results = zip(candidates, total_candidates_votes, percentage_votes)



  # Print all data
print("Election results")
print("-----------------------------------")
print(f"Total Votes:   ({total_votes})") #3521001
print("-----------------------------------")
print(f"{candidates[0]}:     {percentage_votes[0]}% ({total_candidates_votes[0]})")      #Khan: 63.000% (2218231)
print(f"{candidates[1]}:   {percentage_votes[1]}%  ({total_candidates_votes[1]})")      #Correy: 20.000% (704200)
print(f"{candidates[2]}:       {percentage_votes[2]}%  ({total_candidates_votes[2]})")  #Li: 14.000% (492940)
print(f"{candidates[3]}:  {percentage_votes[3]}%  ({total_candidates_votes[3]})")       #O'Tooley: 3.000% (105630)
print("-----------------------------------")
print(f"Winner: {candidates[0]}") #Khan

# Writng output files
PyPoll = open('output.txt','w+')
PyPoll.write("Election results\n")
PyPoll.write("-----------------------------------\n")
PyPoll.write(f"Total Votes:   ({total_votes})\n") #3521001
PyPoll.write("-----------------------------------")
PyPoll.write(f"{candidates[0]}:     {percentage_votes[0]}% ({total_candidates_votes[0]})\n")
PyPoll.write(f"{candidates[1]}:   {percentage_votes[1]}%  ({total_candidates_votes[1]})\n")
PyPoll.write(f"{candidates[2]}:       {percentage_votes[2]}%  ({total_candidates_votes[2]})\n")
PyPoll.write(f"{candidates[3]}:  {percentage_votes[3]}%  ({total_candidates_votes[3]})\n")
PyPoll.write("-----------------------------------\n")
PyPoll.write(f"Winner: {candidates[0]}\n")

