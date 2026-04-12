from pathlib import Path
import csv
from datetime import datetime

def createfile(csvname):
    # defining the base directory and creating if it doesn't exist
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    DATA_DIR = str(BASE_DIR) + "/data"

    Path(DATA_DIR).mkdir(parents=True, exist_ok=True)

    # creating the filename
    start_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = DATA_DIR + "/" + f"{csvname}_{start_timestamp}.csv"

    # create the file
    with open(filename, "a", newline="") as f:
        csvwrt = csv.writer(f)
    # return the filename to the main function
    return filename

# specific for this project to add the data to .csv
def adddata(filename, header, data):
    with open(filename, "w", newline="") as f:
        csvwrt = csv.DictWriter(f, fieldnames = header)
        csvwrt.writeheader()
        csvwrt.writerows(data)