# import modules
from pathlib import Path
import csv

# define function for Overheads
def overheads_function():
    """
    - This function reads data from the Overheads csv file and write into summary report text file
    - It will find the highest overhead category
    """
 # a variable to hold all the data being read from csv file 
    overheads = []

 # a dictionary to hold the highest overheads category and the percentage 
    highest = {
        'Category': None,
        'Overheads': 0
    }

    # file path (both csv file and the summary report file)
    fp_read = Path.cwd()/"TEAM5"/"csv_reports"/"Overheads.csv"
    fp_write = Path.cwd()/"TEAM5"/"summary_report.txt"

    # read the data from the csv file
    with fp_read.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)

        next(reader) # skip the header row 
        for row in reader:
            category = row[0]
            overheads_amount = float(row[1]) # cast string to float

            overheads.append([category, overheads_amount]) # add current row to the lsit
    
    for detail in overheads: # detail refer to the overheads for each category
        overhead = detail[1] # extracting the percentage of the overheads

        if overhead > highest['Overheads']: # if the current overheads percentage is higher


           # a dictionary to overwrite the previous data if conditions are met 
            highest = {
                'Category': detail[0],
                'Overheads': detail[1]
            }
    
    
    # write result to the summary report text file
    with fp_write.open(mode="a", encoding="UTF-8", newline="") as file:
        file.write(f"[HIGHEST OVERHEADS] {highest['Category']}: {highest['Overheads']}%\n")
