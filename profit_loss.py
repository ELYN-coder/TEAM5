# import modules
from pathlib import Path
import csv

# create function for Profits and Loss
def profitloss_function():
    """
    - This function reads data from the Overheads csv file and write into summary report text file
    - It will find the difference in Net Profit if net profit for current day is lower than previous day
    """
    
    
    profit_loss = []
    net = []

    
    fp_read = Path.cwd()/"TEAM5"/"csv_reports"/"Profits and Loss.csv"
    fp_write = Path.cwd()/"TEAM5"/"summary_report.txt"

    
    with fp_read.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)

        next(reader) 
        for row in reader:
            day = row[0]
            net_profit = int(row[4]) 

            profit_loss.append([day, net_profit]) 

    
    total_row = len(profit_loss)

   
    for i in range(1, total_row):


        today = profit_loss[i]
        
        yesterday = profit_loss[i-1]

       
        today_pl = today[1]
        
        yesterday_pl = yesterday[1]

      
        if today_pl < yesterday_pl:
            day = today[0]
            
            different = yesterday_pl - today_pl

            
            net.append([day, different])

    with fp_write.open(mode="a", encoding="UTF-8", newline="") as file:

        
        for loss in net:
            day = loss[0]
            amount = loss[1]
            
           
            file.write(f"[PROFIT DEFICIT] DAY: {day}, AMOUNT: USD{amount}\n")
