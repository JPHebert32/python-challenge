# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
#print(os.listdir('../../'))



# Module for reading CSV files
import csv
csvpath = os.path.join('C:/Users/JPHeb/JPH-Data-Class/du-den-data-pt-03-2020-u-c/Homework-3-Python/PyBank/Resources/budget_data.csv')


P_and_L = 0
date = []
revenue = []
Gr_Increase = 0
Gr_Decrease = 0
Average_Change = float(0)

# Open the CSV
with open(csvpath) as budget_csv:
    csvreader = csv.reader(budget_csv, delimiter=",")

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #print(f"{csv_header}")
   
    # Iterate through CSV 
    for row in csvreader:
        #print(f'{row[0]},{row[1]}') 
                   
        # Add to Date List
        date.append(row[0])

        # Add to Revenue List
        revenue.append(int(row[1]))

total_months = len(date)
total_revenue = sum(revenue)

         

print(f'Financial Analysis')
print("----------------------------")
print(f'Total Months: {total_months}')  
print(f'TOTAL P&L: {total_revenue}')
print(f'Average  Change: $') #$-2315.12
print(f'Greatest Increase in Profits: ') #Feb-2012 ($1926159)
print(f'Greatest Decrease in Profits: ') #Sep-2013 ($-2196167)

