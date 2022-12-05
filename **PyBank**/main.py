# import modules
import os
import csv

# read in CSV file and print to text file
csvpath = os.path.join("/Users/cesarsepulveda/Desktop/ClassData/python-challenge/**PyBank**/Resources/budget_data.csv")
file_to_output = os.path.join("/Users/cesarsepulveda/Desktop/ClassData/python-challenge/**PyBank**/Resources/budget_analysis.txt")

# create lists
numberofMonths = 0
monthlydifferences = []
differenceslist =[]
greatestIncrease = ["", 0]
greatestDecrease = ["", 999999999999] 
incomeTotal = 0

with open(csvpath) as budgetData:

    csvreader = csv.reader(budgetData, delimiter= ',')
# skip header row
    csv_header = next(csvreader)

# assign variable to data without header row
    firstrow = next(csvreader)

# assign variable to months counted 
    numberofMonths += 1 

# assign variable to total income
    incomeTotal += int(firstrow[1])

# assign variable to previous income row  
    previousincomeTotal = int(firstrow[1])

# create for loop 
    for row in csvreader:
        numberofMonths += 1 
        incomeTotal += int(row[1])

# assign variable to income differences total counter
        differencesTotal = int(row[1]) - previousincomeTotal
        previousincomeTotal = int(row[1])

# assign variable to list containing differences 
        differenceslist += [differencesTotal]
        monthlydifferences += [row[0]]

# create conditional statements to find greatest increase and decrease in differences
        if differencesTotal > greatestIncrease [1]:
            greatestIncrease[0] = row[0]
            greatestIncrease[1] = differencesTotal
        
        if differencesTotal < greatestDecrease [1]:
            greatestDecrease[0] = row[0]
            greatestDecrease[1] = differencesTotal

# create variable for average change 
averagedifference= sum(differenceslist)/len(differenceslist)

# print output into format
output = (
f'Financial Analysis\n'
f'----------------------------\n'
f'Total Months: {numberofMonths}\n'
f'Total: ${incomeTotal}\n'
f'Average Change: ${averagedifference}\n'
f'Greatest Increase in Profits: {greatestIncrease[0]} (${greatestIncrease[1]})\n'
f'Greatest Decrease in Profits: {greatestDecrease} (${greatestDecrease[1]})\n'
)
print(output)

# export results to txt file
with open (file_to_output, "w") as txt_file:
    txt_file.write(output)