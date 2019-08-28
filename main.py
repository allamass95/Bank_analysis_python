import os
import csv

num_months=[]
total_amount=[]
average_list=[]

csvpath=os.path.join('..','..','RICEHOU201906DATA1','HW','03-Python','Instructions','PyBank','Resources','budget_data.csv')

with open(csvpath,newline='')as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")

    for row in csvreader:
        
        num_months.append(row[0])
        total_amount.append(row[1])
   
    print('Financial Analysis')  
    print('------------------------')  
    print('Number of Months:' + str(len(num_months[1:])))

    for row_two in range(1,len(total_amount)):
        total_amount[row_two] = int(total_amount[row_two])
        int_list=total_amount[1:]
    print('Total:$'+str(sum(total_amount[1:])))

    for average in range(1,len(int_list)):
        individual_averages=(int_list[average]-int_list[average-1])
        average_list.append(individual_averages)

    average_change=(sum(average_list)/(len(average_list)))
    average_change_final=round(average_change,2)
    print('Average Change:$'+ str(average_change_final))

    max_average=max(average_list)
    min_average=min(average_list)

    print('Greatest increase in profits: '+ num_months[26] +" "+"$"+str(max(average_list)))
    print('Greatest decrease in profits: '+ num_months[45]+" "+"$"+str(min(average_list)))

   