import signal

from util import csvutil, dirsutil, openconfig
from models.datacollector import DataCollector

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

# filename - based on location and wifi type
location = measconfig['measurements_config']['location']
wifi_type = measconfig['measurements_config']['wifi_type']
csvfilename = location + wifi_type

# configuring the signal interruption
signal.signal(signal.SIGALRM, wifi_collector.time_interruptor)
signal.setitimer(signal.ITIMER_REAL, 1, wifi_collector.time_sample)

# main loop
try:
    print("Starting Measurements...")
    while True:
         # without this the code was consuming 1 CPU core = 25% total CPU
        signal.pause()
except SystemExit:
    print("End.")

csvheader = wifi_collector.data_list[0].keys()
csvname = csvutil.createfile(csvname = csvfilename)
csvutil.adddata(filename = csvname, header = csvheader, data = wifi_collector.data_list)