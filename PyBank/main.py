#csvpath = os.path.join("..","Resources","03-Python_hw_Instructions_PyBank_Resources_budget_data.csv")


#python 3.2.12 example
import os
import csv

csvpath = os.path.join("..","Resources","03-Python_hw_Instructions_PyBank_Resources_budget_data.csv")

date = []
PL = []

with open(csvpath, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    for row in csvreader:
        date.append(row[0])
        PL.append(row[1])
        
cleaned_csv = zip(date, PL)

output_file = os.path.join