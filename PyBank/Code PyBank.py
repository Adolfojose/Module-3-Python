import csv
import os

file_path = os.path.join("PyBank", "Resources", "budget_data.csv")

total_months = 0
total_profit_loss = 0
prev_profit_loss = 0
profit_loss_change = 0
total_profit_loss_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]

with open(file_path) as financial_data:
    csvreader = csv.reader(financial_data)

    header = next(csvreader)

    for row in csvreader:

        total_months += 1

        total_profit_loss += int(row[1])

        profit_loss_change = int(row[1]) - prev_profit_loss

        prev_profit_loss = int(row[1])

        if total_months > 1:
            total_profit_loss_change += profit_loss_change

        if profit_loss_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = profit_loss_change

        if profit_loss_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = profit_loss_change

average_change = round(total_profit_loss_change / (total_months - 1), 2)

print("Financial Analysis")
print("-----------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

with open("PyBank/Analysis/Financial_Analysis.txt", "w") as analysis_file:
    analysis_file.write("Financial Analysis\n")
    analysis_file.write("-----------------------------------\n")
    analysis_file.write(f"Total Months: {total_months}\n")
    analysis_file.write(f"Total: ${total_profit_loss}\n")
    analysis_file.write(f"Average Change: ${average_change}\n")
    analysis_file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    analysis_file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")