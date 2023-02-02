# import modules
from pathlib import Path
import csv

# define function for Overheads
def overheads_function():
    """
    - This function reads data from the Overheads csv file and write into summary report text file
    - It will find the highest overhead category
    """
    
    overheads = []

  
    highest = {
        'Category': None,
        'Overheads': 0
    }

    fp_read = Path.cwd()/"TEAM5"/"csv_reports"/"Overheads.csv"
    fp_write = Path.cwd()/"TEAM5"/"summary_report.txt"

    with fp_read.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)

        next(reader) 
        for row in reader:
            category = row[0]
            overheads_amount = float(row[1]) 

            overheads.append([category, overheads_amount]) 
    
    for detail in overheads: 
        overhead = detail[1] 

        if overhead > highest['Overheads']: 

            
            highest = {
                'Category': detail[0],
                'Overheads': detail[1]
            }
    
    
    with fp_write.open(mode="a", encoding="UTF-8", newline="") as file:
        file.write(f"[HIGHEST OVERHEADS] {highest['Category']}: {highest['Overheads']}%\n")