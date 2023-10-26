#Import files
import os
import csv

#Create filepath to csv data
FilePath = "Childers_submission 3/PyBank/Resources/Childers_budget_data.csv"

#Declare variables
total_Months = 0
total_ProfitLoss = 0

#Create list of deltas between each row's profit/loss amount
Deltas = []

last_ProfitLoss = 0

#Set max and min
max_Delta = -999999999
min_Delta = 999999999
max_Month = ""
min_Month = ""

#Read the csv file data and delimiter makes each comma in csv turn into a new column
with open(FilePath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #Read each row after the header
    for row in csvreader:
        print(row)
        
        #Incorporate changes between rows to calculate profit
        if total_Months != 0: #If not equal to 0
            Delta = int(row[1]) - last_ProfitLoss
            Deltas.append(Delta)

            #Check if there is a max/min delta
            if Delta > max_Delta:
                max_Delta = Delta
                max_Month = row[0]
            elif Delta < min_Delta:
                min_Delta = Delta
                min_Month = row[0]
            else:
                pass #Don't do anything with the delta

        #Assign as the last month profit
        last_ProfitLoss = int(row[1])

        #Move to next row
        total_Months = total_Months + 1

        #Calculate profit loss from last month
        total_ProfitLoss = total_ProfitLoss + int(row[1])

        #Profit loss to the variable
        total_ProfitLoss = total_ProfitLoss + int(row[1])

#Calculate average of the deltas and display aka take the total sum of changes and divide by number of deltas
avg_Delta = sum(Deltas) / len(Deltas) 
print(avg_Delta)

#Show the total months listed, profit loss, and greatest decrease/increase
print(total_Months)
print(total_ProfitLoss)
print(min_Delta)
print(min_Month)
print(max_Delta)
print(max_Month)

#Export to a text file
with open("Childers_budgetdata_output_module3.txt", "w") as txt_file:
    output = f"""
Financial Analysis
----------------------------
Total Months: {total_Months}
Total: ${total_ProfitLoss}
Average Change: ${round(avg_Delta, 2)}
Greatest Increase in Profits: {max_Month} (${max_Delta})
Greatest Decrease in Profits: {min_Month} (${min_Delta})"""

    txt_file.write(output)