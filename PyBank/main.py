import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

#initialize variables
total_months = 0
profit = 0
net = 0
changes = []
previous_value = 867884
greatest_increase = 0
greatest_decrease = 0
total_net = 0

#loop
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ',')
    csvheader = next(csvreader)
    for row in csvreader:
        current_value = int(row[1])
        total_months += 1
        profit += current_value
        net = current_value - previous_value
        changes.append(net)
        if net > greatest_increase:
            greatest_increase = net
            increase_month = row[0]
        elif net < greatest_decrease:
            greatest_decrease = net
            decrease_month = row[0]

        previous_value = current_value
        #print(net)
        
    
   
    #print(changes)
    for x in range(len(changes)):
        total_net = total_net + changes[x]
        #print(total_net)
        average = total_net/(total_months-1)

    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months: "+str(total_months))
    print("Total: $" + str(profit))
    print(f"Total Change: ${round(average,2)}")
    print(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})")
    print(f"Greatest Increase in Profits: {decrease_month} (${greatest_decrease})")

    file = os.path.join('analysis', 'PyBank.txt')

    with open(file,'w') as text:
        text.write("Financial Analysis \n-----------------------------------\n")
        text.write("Total Months: "+str(total_months) + '\n')
        text.write("Total: $" + str(profit) +'\n')
        text.write(f"Total Change: ${round(average,2)}\n")
        text.write(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})\n")
        text.write(f"Greatest Increase in Profits: {decrease_month} (${greatest_decrease})")