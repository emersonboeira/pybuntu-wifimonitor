from pathlib import Path
import csv
from datetime import datetime

def createfile(csvname, header):
    # defining the base directory    
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    DATA_DIR = str(BASE_DIR) + "/data"

    # creating the filename
    start_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = DATA_DIR + "/" + f"{csvname}_{start_timestamp}.csv"

    # create / open the file and add the header
    with open(filename, "a", newline="") as f:
        csvwrt = csv.writer(f)
        csvwrt.writerow(header)
    #return filename

# specific for this project
def adddata(filename, data):
    with open(filename, "a", newline="") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(data)