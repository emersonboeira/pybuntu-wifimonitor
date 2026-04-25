# pybuntu-wifimonitor

Python project to monitor my wifi signal on my Ubuntu OS. 

Measures: Latency, RSSI (Received Signal Strength Indicator) to the router.

Uses the Ubuntu system `ping` command and the `iw` command.

## System and Python Versions

* Ubuntu = 24.04
* Python = 3.12.3
  
## Installing Python Packages

### Installation

Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

Install Python dependencies:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## Ubuntu Requirements

Two Ubuntu packages are necessary to run this software: `iputils-ping`, `iw`.

The following packages are required to use `ping` and `iw` via subprocess:

```bash
sudo apt update
sudo apt install -y iputils-ping iw
```

## Run the WiFi Measurements

Go to the project's directory file and run:
```bash
python3 src/measure.py
```