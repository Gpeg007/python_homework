import os
import csv

csvpath = os.path.join('budget_data.csv')

with open(csvpath, 'r') as csvreader:
    csvreader = csv.reader(csvreader, delimiter=",")

    print("Financial Report")
    print("----------------------------")
    
    total_months = sum(1 for row in csvreader)
    print(f"Total Months: " + str(total_months))

    total = sum(2 for row[1] in csvreader)
    print(f"Total: " + str(total))
