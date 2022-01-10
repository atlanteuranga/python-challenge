import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

#initialize variables
total_months = 0
profit = 0
net = 0
changes = []
#inital previous value is 867884
#since we don't need the change for the first month (the change would be 0)
previous_value = 867884
greatest_increase = 0
greatest_decrease = 0
total_net = 0

#read the csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ',')
    #store the header row
    csvheader = next(csvreader)
    for row in csvreader:

        #get the current profit/loss to add to the total
        current_value = int(row[1])

        #calculate the total months by adding 1 for each row we iterate through
        total_months += 1

        #add the current value to the total
        profit += current_value

        #get the change from the previous month for our comparison
        net = current_value - previous_value

        #add to a new list that we will use to find the average
        changes.append(net)

        #compare the nets to each other to find the greatest increase and decrease
        if net > greatest_increase:
            greatest_increase = net
            increase_month = row[0]
        elif net < greatest_decrease:
            greatest_decrease = net
            decrease_month = row[0]

        previous_value = current_value
        #print(net)
        
    
   
    #print(changes)
    # add up all of the nets inside of the list changes
    for x in range(len(changes)):
        total_net = total_net + changes[x]
        #print(total_net)
        
        #total_months - 1 because we don't count the first month
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