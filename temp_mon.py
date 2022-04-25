# temp_sensor.py
import os
import time
import datetime
from log_write_to_text_file import log_write_to_text_file


def measure_temp():
        while True:
                temp = os.popen("cat /sys/class/thermal/thermal_zone0/temp").readline()
                # return (temp.replace("temp=",""))
                temp = (temp.replace("temp=",""))
                now = datetime.datetime.now()
                """
                # temp = measure_temp()
                print('#############################')
                print(now)
                print(temp)
                """
                # log_write_to_text_file('msg')
                log_write_to_text_file('temp: {0}'.format(temp))
                time.sleep(60)



if __name__ == '__main__':
    measure_temp()
