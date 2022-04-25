import time
import obd, serial, subprocess, threading, datetime
import variables
from at_connections import at_gps_start, at_gps_stop, at_internet_stop
from at_gps import at_get_gps_position
from db_connect import db_create_connection
from temp_mon import *
from gpio import gpio_power_on, gpio_power_off
from rest_communicate import post_to_server
from log_write_to_text_file import log_write_to_text_file
from variables import *


# user vars
token = variables.token
auth_user_id = variables.auth_user_id
apn_var = variables.apn_var


# go to writeable dir
os.chdir('/pi-auto')


# log_write_to_text_file('msg')
log_write_to_text_file('Program Started')


# db connect
database = r"data.db"
db_file = database
conn = db_create_connection(db_file)
# get records
# db_select_all(conn)


# gpio_power_on()
ser = serial.Serial('/dev/ttyS0',9600)
    # ser = serial.Serial('/dev/ttyUSB3',115200) # seems to work
    # ser = serial.Serial('/dev/ttyAMA0',115200)
    # ser = serial.Serial('/dev/serial1',115200)
    # windows connect
    # ser = serial.Serial('COM5', 115200)
# ser_internet = serial.Serial('/dev/ttyUSB3',115200)


# sudo rfcomm bind rfcomm0 00:1D:A5:68:C3:E2
bluetooth_folder_check = os.path.isdir('/dev/rfcomm0')
if bluetooth_folder_check == False:
    subprocess.run(['sudo', 'rfcomm', 'bind', 'rfcomm0', '00:1D:A5:68:C3:E2'])

obd.logger.setLevel(obd.logging.DEBUG)
obd_connection = obd.OBD(portstr='/dev/rfcomm0', baudrate='115200', protocol='6')
time.sleep(5)  # this fix?


def gps_start(ser):
    at_gps_start(ser)


def gps_start_app(ser, obd_connection):
    at_get_gps_position(ser, obd_connection)


def gps_stop(ser):
    at_gps_stop(ser)


def startup():
    gpio_power_on()


def shutdown(ser):
    at_internet_stop(ser)
    at_gps_stop(ser)
    # ser.write(("AT+CREBOOT \r \n").encode())
    gpio_power_off()
    ser.close()


def sleep_short():
    time.sleep(.5)


def sleep_long():
    time.sleep(2)


def temp_start():
    t = threading.Thread(target=measure_temp, args=())
    t.start()


# todo. need to put some of these into var, is this the best way to do it?
def internet_start():
    result = subprocess.run(['sudo', './sakis3g', 'connect', 'OTHER="USBMODEM"', 'USBMODEM="1e0e:9205"',
                          'USBINTERFACE="3"',
    'APN="telstra.wap"', '--noprobe'], capture_output=True)
    log_write_to_text_file('Internet_start: {0} {1}'.format(result.stdout, result.stderr))


def internet_stop():
    result = subprocess.run(['sudo', './sakis3g', 'disconnect'], capture_output=True)
    log_write_to_text_file('Internet_start: {0} {1}'.format(result.stdout, result.stderr))


# todo. turn into a PyPi package
def update_check_thread():
    def update_check():
        try:
            print('Updating')
            log_write_to_text_file('Updating')
            result = subprocess.run(['pip3', 'install',
                            'https://github.com/LukeKeam/pi-auto/archive/refs/heads/main.zip'], capture_output=True)
            log_write_to_text_file('Internet_start: {0} {1}'.format(result.stdout, result.stderr))
        except:
            pass
    t = threading.Thread(target=update_check, args=())
    t.start()


def update_datetime_thread():
    def update_datetime():
        print('before update_datetime: ', datetime.datetime.now())
        log_write_to_text_file('before update_datetime: {0}'.format(datetime.datetime.now()))
        subprocess.run(['sudo', 'mount', '-o', 'remount,rw', '/'])
        subprocess.run(['sudo', 'timedatectl', 'set-ntp', 'True'])
        subprocess.run(['sudo', 'mount', '-o', 'remount,ro', '/', '-force'])
        print('after update_datetime: ', datetime.datetime.now())
        log_write_to_text_file('after update_datetime: {0}'.format(datetime.datetime.now()))
    update_datetime()


if __name__ == '__main__':
    # test connection to waveshare at_test_device_connection(ser)
    temp_start()
    shutdown(ser)
    startup()
    ser = serial.Serial('/dev/ttyS0', 9600)
    internet_start()
    update_datetime_thread()
    # update_check_thread()
    post_to_server(conn=conn, token=token, auth_user_id=auth_user_id)
    internet_stop()
    # plan b
    shutdown(ser)
    startup()
    ser = serial.Serial('/dev/ttyS0', 9600)
    gps_stop(ser)
    gps_start(ser)
    gps_start(ser)
    gps_start(ser)
    gps_start_app(ser, obd_connection)
