# Python Challenges 
# PyBank / main.py
# JP Hebert
#------------------------------------------------------------------------------------------------------------------
# Your task is to create a Python script that analyzes the records to calculate each of the following:

# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

# The average of the changes in "Profit/Losses" over the entire period

#The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in losses (date and amount) over the entire period
#-----------------------------------------------------------------------------------------------------------------

# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
print(os.listdir('../../'))


# Module for reading CSV files
import csv

#C:\Users\JPHeb\JPH-Data-Class\du-den-data-pt-03-2020-u-c\Homework-3-Python\PyBank\Resources
csvpath = os.path.join('C:/Users/JPHeb/JPH-Data-Class/du-den-data-pt-03-2020-u-c/Homework-3-Python/PyBank/Resources/budget_data.csv')


# Open the CSV
with open(csvpath) as budget_csv:
    csvreader = csv.reader(budget_csv, delimiter=",")

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"{csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(f'{row[0]},{row[1]}')