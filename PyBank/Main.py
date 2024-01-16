import os
import csv

# File path
input_file = os.path.join("Resources", "budget_data.csv")
output_file = os.path.join("analysis", "budget_analasis.txt")


# Init variables
total_months = 0
total_profit_losses = 0
previous_profit = 0
current_profit = 0
total_change = 0
greatest_increase = 0
greatest_decrease = 0
greatest_increase_data = ""
greatest_decrease_data = ""
monthly_changes = []
dates =[]

with open(input_file) as in_file:
    reader = csv.reader(in_file)
    header = next(reader)

    # Read first row to initialaize previious_profit
    first_row = next(reader)
    previous_profit = int(first_row[1])
    total_months += 1
    total_profit_losses += previous_profit

    for row in reader:
        total_months += 1
        current_profit = int(row[1])

        # Monthly change
        total_change = current_profit - previous_profit
        monthly_changes.append(total_change)
        # Greatest increase
        if  total_change > greatest_increase:
            greatest_increase = total_change
            greatest_increase_date = row[0]
        elif total_change < greatest_decrease:
            greatest_decrease = total_change
            greatest_decrease_date = row[0]

        # Update previous_profit for the next iteration
        previous_profit = current_profit

# Calculate total profit losses
        total_profit_losses += current_profit

# Calculate average change
        average_change = round(sum(monthly_changes)/ len(monthly_changes), 2)


output = (
    f"Financial Analysis\n"
    f"-----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit_losses}\n"
    f"Average Change: ${average_change}\n"
    f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")

with open(output_file,"w") as out_file:
    out_file.write(output)
    print(output)

