import os
import csv
import math

#Locate file
budgetdata_csv=os.path.join("budget_data.csv")

#Set Lists and Variables 
total_months=[]
total_profit=[]
profitchange_list=[]


#Open/read file 
with open(budgetdata_csv, newline="",encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    nextreader=next(csvreader)

#Begin iterator for total months and profit 
    for row in csvreader:
        #print(row)
        total_months.append(row[0])
        total_profit.append(int(row[1])) 

#Begin iterator for change in profits 
    for i in range(len(total_profit)-1):
       profitchange_list.append(total_profit[1+i]-total_profit[i]) 

#Greatest increase and decrease and months associated
Greatest_increase= max(profitchange_list)
Greatest_decrease= min(profitchange_list)

Greatestincrease_month=profitchange_list.index(max(profitchange_list)) + 1
Greatestdecrease_month=profitchange_list.index(min(profitchange_list)) + 1


#Final Table 

print("                                  ")
print ("Financial Analysis")
print ("----------------------------")
print (f"Total Months:{len(total_months)}")
print (f"Total: ${sum(total_profit)}")
print (f"Average Change:${round(sum(profitchange_list)/len(profitchange_list),2)}")
print (f"Greatest Increase in Profits:{total_months[Greatestincrease_month]} (${Greatest_increase})")
print (f"Greatest Decrease in Profits:{total_months[Greatestdecrease_month]} (${Greatest_decrease})")


#Text File Output

finaloutput=os.path.join("finaloutput.txt")

with open(finaloutput,"w") as fileoutput:
    fileoutput.write("                                  ")
    fileoutput.write("\n")
    fileoutput.write("Financial Analysis")
    fileoutput.write("\n")
    fileoutput.write("----------------------------")
    fileoutput.write("\n")
    fileoutput.write(f"Total Months:{len(total_months)}")
    fileoutput.write("\n")
    fileoutput.write(f"Total: ${sum(total_profit)}")
    fileoutput.write("\n")
    fileoutput.write(f"Average Change:${round(sum(profitchange_list)/len(profitchange_list),2)}")
    fileoutput.write("\n")
    fileoutput.write(f"Greatest Increase in Profits:{total_months[Greatestincrease_month]} (${Greatest_increase})")
    fileoutput.write("\n")
    fileoutput.write(f"Greatest Decrease in Profits:{total_months[Greatestdecrease_month]} (${Greatest_decrease})")
    fileoutput.write("\n")