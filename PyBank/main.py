# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
#print(os.listdir('../../'))

# Module for reading CSV files
import csv
csvpath = os.path.join('C:/Users/JPHeb/JPH-Data-Class/du-den-data-pt-03-2020-u-c/Homework-3-Python/PyBank/Resources/budget_data.csv')

date = []
revenue = []
Increase = 0
Decrease = 0
Average_Change = float(0)

# Open the CSV
with open(csvpath) as budget_csv:
    csvreader = csv.reader(budget_csv, delimiter=',')

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
total = sum(revenue)

Monthly_diff =[]

# using zip() 
# generate successive difference list 
Monthly_diff = [j - i for i, j in zip(revenue[: -1], revenue[1 :])] 
#print(Monthly_diff)

#Find Greatest Increase Using MAX on Monthly_Diff
Increase = (max(Monthly_diff))

#Find corresponding Date Index for INCREASE
Increase_index = (Monthly_diff.index(Increase)) +1

#Find Greatest Decrease Using min on Monthly_Diff
Decrease = (min(Monthly_diff))

#Find corresponding Date Index for DECREASE
Decrease_index =(Monthly_diff.index(Decrease)) +1


#Calulating Average Change 
Total_Diff = sum(Monthly_diff)
diff_count = len(Monthly_diff)
Average_Change = Total_Diff / diff_count


print(f'Financial Analysis')
print('----------------------------')
print(f'Total Months: {total_months}')  #86
print(f'TOTAL P&L: ${total}') # $38382578
print(f'Average Change: ${round(Average_Change, 2)}') #$-2315.12
print(f'Greatest Increase in Profits: {date[Increase_index]}  ${Increase}') #Feb-2012 ($1926159)
print(f'Greatest Decrease in Profits: {date[Decrease_index]}  ${Decrease}') #Sep-2013 ($-2196167)


# Writng output files
PyBank = open('output.txt','w+')

PyBank.write(f'Financial Analysis\n')
PyBank.write('----------------------------\n')
PyBank.write(f'Total Months: {total_months}\n')
PyBank.write(f'TOTAL P&L: ${total}\n') 
PyBank.write(f'Average Change: ${round(Average_Change, 2)}\n')
PyBank.write(f'Greatest Increase in Profits: {date[Increase_index]}  ${Increase}\n')
PyBank.write(f'Greatest Decrease in Profits: {date[Decrease_index]}  ${Decrease}\n')
