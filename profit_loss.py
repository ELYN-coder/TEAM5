# import modules
from pathlib import Path
import csv

# create function for Profits and Loss
def profitloss_function():
    """
    - This function reads data from the Overheads csv file and write into summary report text file
    - It will find the difference in Net Profit if net profit for current day is lower than previous day
    """
    
    # variable to hold all data read from csv file
    profit_loss = []
    net = []

    # file path (both csv file and the summary report file)
    fp_read = Path.cwd()/"TEAM5"/"csv_reports"/"Profits and Loss.csv"
    fp_write = Path.cwd()/"TEAM5"/"summary_report.txt"

    # read data from the csv file
    with fp_read.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)

        next(reader) # skip the header row
        for row in reader:
            day = row[0]
            net_profit = int(row[4]) # cast string to integer

            profit_loss.append([day, net_profit]) # add current row to the list

    # calculate total number of rows
    total_row = len(profit_loss)

    # start looping from second row
    # need at least 2 days of data for comparison to find the difference
    for i in range(1, total_row):

        # extract the current day of PL
        today = profit_loss[i]
        # extract the previous day of PL
        yesterday = profit_loss[i-1]

        # extract the PL amount from the current day
        today_pl = today[1]
        # extract the PL amount from the previous day
        yesterday_pl = yesterday[1]

        # check if today PL is lesser than yesterday PL
        if today_pl < yesterday_pl:
            day = today[0]
            # calculation of difference in loss
            different = yesterday_pl - today_pl

            # putting into the list created under net
            net.append([day, different])

    with fp_write.open(mode="a", encoding="UTF-8", newline="") as file:

        # write the data into the file
        for loss in net:
            day = loss[0]
            amount = loss[1]
            
            # write result to the summary report file
            file.write(f"[PROFIT DEFICIT] DAY: {day}, AMOUNT: USD{amount}\n")
