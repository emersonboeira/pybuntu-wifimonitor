import re
import subprocess
from datetime import datetime

PING = "ping"
RSSI = "rssi"

class DataCollector:
    def __init__(self, time_sample, time_limit, devip, devint):
        self.count = 0
        self.time_sample = time_sample
        self.time_limit = time_limit

        self.devip = devip
        self.devint = devint

        self.data_list = []

    def run_subprocess(self, function):
        config = {
        "ping": (["ping", "-c", "1", "-W", "1", self.devip], r"time=(\d+\.?\d*)", float),
        "rssi": (["iw", "dev", self.devint, "link"], r"signal:\s+(-?\d+)", int)
    }
        cmd, regex, cast_type = config[function]

        try:
            sub_output = subprocess.check_output(cmd).decode()
            sub_match = re.search(regex, sub_output)
            if sub_match:
                return cast_type(sub_match.group(1)) 
        except subprocess.CalledProcessError:
            return "Timeout"
        
    def time_interruptor(self, signum, frame):
        self.count += self.time_sample

        time_meas = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        ping_meas = self.run_subprocess(PING)
        rssi_meas = self.run_subprocess(RSSI)

        self.data_list.append({
            "timestamp": time_meas,
            "ping": ping_meas,
            "rssi": rssi_meas
        })

        print(f"[{time_meas}, {ping_meas}, {rssi_meas}] Tick {int(self.count / self.time_sample) - 1}")

        if self.count >= (self.time_limit + self.time_sample):
            raise SystemExit