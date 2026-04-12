import signal

from util import csvutil
from models.datacollector import DataCollector

# project configs
ROUTER_IP = "192.168.0.1"
WIFI_INTERFACE = "wlo1"

# csvconfig
CSVHEADER = ["Timestamp", "Ping", "RSSI"]

# measurements config
TOTAL_TIME = 10 # seconds
SAMPLE = 5 # seconds

# location constants
OFFICE = "office"
BEDROOM = "bedroom"
LIVINGROOM = "livingroom"

wifi_collector= DataCollector(
    time_sample = SAMPLE,
    time_limit = TOTAL_TIME,
    devip = ROUTER_IP,
    devint = WIFI_INTERFACE
    )

signal.signal(signal.SIGALRM, wifi_collector.time_interruptor)
signal.setitimer(signal.ITIMER_REAL, 1, wifi_collector.time_sample)

# main loop
try:
    print("Starting...")
    while True:
        pass
except SystemExit:
    print("End.")

csvheader = wifi_collector.data_list[0].keys()
csvname = csvutil.createfile(OFFICE)
csvutil.adddata(filename = csvname, header = csvheader, data = wifi_collector.data_list)