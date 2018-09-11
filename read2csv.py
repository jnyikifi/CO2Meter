#!/bin/env python
from CO2Meter import *
from datetime import datetime
import time

def print_measurement(m):
    print("\'" + m.get('timestamp', "") + "', " + \
          str(m.get('co2', 0)) + ", " + \
          str(m.get('temperature', 0)))
 
Meter = CO2Meter("/dev/hidraw3")

print("\'timestamp\', \'co2\', \'temperature\'")

while True:
    measurement = Meter.get_data()
    measurement.update({'timestamp': datetime.now().isoformat(' ')})
    print_measurement(measurement)
    time.sleep(60)
