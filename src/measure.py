import signal

from util import csvutil, dirsutil, openconfig
from models.datacollector import DataCollector

# location constants
OFFICE = "office"
BEDROOM = "bedroom"
LIVINGROOM = "livingroom"

# creating the project's directories
dirsutil.creating()
# loading the project's configuration
measconfig = openconfig.load_json()

wifi_collector= DataCollector(
    time_sample = int(measconfig['measurements_config']['sample_time']),
    time_limit = int(measconfig['measurements_config']['total_time']),
    devip = measconfig['device_config']['router_ip'],
    devint = measconfig['device_config']['wifi_interface']
    )

signal.signal(signal.SIGALRM, wifi_collector.time_interruptor)
signal.setitimer(signal.ITIMER_REAL, 1, wifi_collector.time_sample)

# main loop
try:
    print("Starting Measurements...")
    while True:
        pass
except SystemExit:
    print("End.")

csvheader = wifi_collector.data_list[0].keys()
csvname = csvutil.createfile(OFFICE)
csvutil.adddata(filename = csvname, header = csvheader, data = wifi_collector.data_list)