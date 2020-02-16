import os
import csv
row_count=0
net_amount=0
amount=0
avg_change=0
max_loss=0
max_profit=0 
Y=0

file=os.path.join('budget_data.csv')
with open (file,newline='') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    #print(csvreader)

    header = next(csvreader)
    for x in csvreader:
        row_count+=1
        net_amount=net_amount+int(x[1])
        
        if amount!=0:
            x.append(int(x[1])-amount)
            Y =(int(x[1])-amount)
            if max_profit < (int(x[1])-amount):
                max_profit = (int(x[1])-amount)
                max_profit_month=x[0]
            if max_loss > (int(x[1])-amount):
                max_loss = (int(x[1])-amount)
                max_loss_month=x[0]

        avg_change = avg_change +  Y
        amount=int(x[1])
        
print(f' Financial Analysis \n _____________________\n\n Total Months: {row_count} \n Total: {net_amount} \n Average  Change: {round((avg_change/(row_count-1)),2)} \n Greatest Increase in Profits: {max_profit_month} ({max_profit}) \n Greatest Decrease in Profits: {max_loss_month} ({max_loss})')



