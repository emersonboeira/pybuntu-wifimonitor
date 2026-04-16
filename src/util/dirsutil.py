from pathlib import Path

def creating():
    # creating the data directory for this project
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    DATA_DIR = str(BASE_DIR) + "/data"
    Path(DATA_DIR).mkdir(parents=True, exist_ok=True)
