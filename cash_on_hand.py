# import modules
from pathlib import Path
import csv

# define function for Cash on Hand
def coh_function():
    """
    - This function reads data from the Overheads csv file and write into summary report text file
    - It will find difference in Cash on Hand if current day is lower than previous day
    """
    
    # a variable to hold all the data being read from the csv file
    cash_on_hand = []
    deficits = []

    # file path (both csv file and the summary report file)
    fp_read = Path.cwd()/"TEAM5"/"csv_reports"/"Cash on Hand.csv"
    fp_write = Path.cwd()/"TEAM5"/"summary_report.txt"

    # read the data from the csv file
    with fp_read.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)

        next(reader) # skip the header row
        for row in reader:
            day = row[0]
            cos = int(row[1]) # cast string to integer

            cash_on_hand.append([day, cos]) # add current row to the list

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

        # check if previous day's coh is greater than current day's coh
        if yesterday_coh > today_coh:
            day = today[0]
            # calculation of difference in coh
            different = yesterday_coh - today_coh

            # putting into the list created under deficits
            deficits.append([day, different])
    
    
    with fp_write.open(mode="a", encoding="UTF-8", newline="") as file:

        # write data into the file
        for deficit in deficits:
            day = deficit[0]
            amount = deficit[1]

            # write the deficit to summary report text file
            file.write(f"[CASH DEFICIT] DAY: {day}, AMOUNT: USD{amount}\n")
