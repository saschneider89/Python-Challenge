#Load dependencies
import os
import csv


#Create variables or lists to store data
Months = 0
Dates = []
Profits = []

#Use encoding='utf-8 for Windows
csvpath = os.path.join("..","Resources","PyBank_Resources_budget_data.csv")
with open(csvpath, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #Skip Header
    next(csvreader, None)
    for row in csvreader:
        Months += 1
        Dates.append(row[0])
        Profits.append(float(row[1]))

#Set initial values, Profits[0] is first value in list
Total_Profits = Profits[0]
Total_Change = 0
Biggest_Increase = 0
Biggest_Decrease = 0

#Only 85 changes between month to month
for n in range (1, Months):
    #Loop through column 1 to find total profits
    Total_Profits += Profits[n]
    
    #Calculate the change between this month and the month before it and then add it to the totaled changes
    Month_Change = Profits[n] - Profits[n-1]
    Total_Change += Month_Change
    
    #Loop through above totals, find months with biggest increases/decreases
    if Month_Change > Biggest_Increase:
        Biggest_Increase = Month_Change
        Biggest_Increase_Date = Dates[n]
    elif Month_Change < Biggest_Decrease:
        Biggest_Decrease = Month_Change
        Biggest_Decrease_Date = Dates[n]

#Print Results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {Months}")
print(f"Total: ${(int(Total_Profits))}")
print(f"Average Change: $ {Average_Change:.2f}")
print(f"Greatest Increase in Profits: {Biggest_Increase_Date} (${(int(Biggest_Increase))})")
print(f"Greatest Decrease in Profits: {Biggest_Decrease_Date} (${(int(Biggest_Decrease))})")

#Write Results to .txt file
output_file = os.path.join("..","Analysis","PyBank.txt")
with open(output_file, "w", encoding='utf-8') as datafile:

    datafile.write("Financial Analysis\n")
    datafile.write("----------------------------\n")
    datafile.write(f"Total Months: {Months}\n")
    datafile.write(f"Total: ${(int(Total_Profits))}\n")
    datafile.write(f"Average Change: $ {Average_Change:.2f}\n")
    datafile.write(f"Greatest Increase in Profits: {Biggest_Increase_Date} (${(int(Biggest_Increase))})\n")
    datafile.write(f"Greatest Decrease in Profits: {Biggest_Decrease_Date} (${(int(Biggest_Decrease))})\n")

#Correct values for reference
#Financial Analysis
#----------------------------
#Total Months: 86
#Total: $38382578
#Average  Change: $-2315.12
#Greatest Increase in Profits: Feb-2012 ($1926159)
#Greatest Decrease in Profits: Sep-2013 ($-2196167)