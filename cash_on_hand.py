# import modules
from pathlib import Path
import csv

# define function for Cash on Hand
def coh_function():
    """
    - This function reads data from the Overheads csv file and write into summary report text file
    - It will find difference in Cash on Hand if current day is lower than previous day
    """
    
   
    cash_on_hand = []
    deficits = []

   
    fp_read = Path.cwd()/"TEAM5"/"csv_reports"/"Cash on Hand.csv"
    fp_write = Path.cwd()/"TEAM5"/"summary_report.txt"

  
    with fp_read.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)

        next(reader) 
        for row in reader:
            day = row[0]
            cos = int(row[1]) 

            cash_on_hand.append([day, cos]) 

   
    total_row = len(cash_on_hand)

  
    for i in range(1, total_row):

       
        today = cash_on_hand[i]
       
        yesterday = cash_on_hand[i - 1]

      
        today_coh = today[1]
       
        yesterday_coh = yesterday[1]

        
        if yesterday_coh > today_coh:
            day = today[0]
           
            different = yesterday_coh - today_coh

           
            deficits.append([day, different])
    
    
    with fp_write.open(mode="a", encoding="UTF-8", newline="") as file:

    
        for deficit in deficits:
            day = deficit[0]
            amount = deficit[1]

          
            file.write(f"[CASH DEFICIT] DAY: {day}, AMOUNT: USD{amount}\n")
