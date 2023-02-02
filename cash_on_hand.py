# import modules
from pathlib import Path
import csv

# create function for Cash on Hand
def coh_function():
    """
    - This function reads data from the Cash On Hand csv file and write into summary report text file
    - It will find difference in Cash on Hand if current day is lower than previous day
    """
    
    # a variable to hold all the data being read from the csv file
    cash_on_hand = []
    deficits = []

    # file path (both csv file and the summary report file)
    # setup file path for reading 
    fp_read = Path.cwd()/"TEAM5"/"csv_reports"/"Cash on Hand.csv"
    # create a path object for summary_report.txt
    fp_write = Path.cwd()/"TEAM5"/"summary_report.txt"

    # read the data from the csv file
    with fp_read.open(mode="r", encoding="UTF-8", newline="") as file:
        # create csv reader object using csv
        reader = csv.reader(file)
        # use next() function to skip the header
        next(reader) 
        # iterate each row with loop
        for row in reader:
            # access to first sub-list, day, by indexing with [inner key]
            day = row[0]
            # access to second sub-list, cash on hand, by indexing with [inner key]
            # cast string to integer
            cos = int(row[1]) 

            # use .append() to add current row to the list
            cash_on_hand.append([day, cos]) 

    # calculate the total number of rows
    total_row = len(cash_on_hand)

    # start looping from second row
    # need at least 2 days of data for comparison to find the difference
    for i in range(1, total_row):

        # extract current day of coh
        today = cash_on_hand[i]
        # extract previous day of coh
        yesterday = cash_on_hand[i - 1]

        # extract coh amount from current day
        today_coh = today[1]
        # extract coh amount from previous day
        yesterday_coh = yesterday[1]

        # use if statement to check if previous day's coh is greater than current day's coh
        if yesterday_coh > today_coh:
            day = today[0]
            # calculation of difference in coh
            different = yesterday_coh - today_coh

            # putting into the list created under deficits
            deficits.append([day, different])
    
    # use mode = "a" to append data to file
    with fp_write.open(mode="a", encoding="UTF-8", newline="") as file:

        # write data into the file
        for deficit in deficits:
            day = deficit[0]
            amount = deficit[1]

            # write the deficit to summary report text file
            file.write(f"[CASH DEFICIT] DAY: {day}, AMOUNT: USD{amount}\n")
