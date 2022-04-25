import time
from gpio import gpio_power_on, gpio_power_off


# test connection
def at_test_device_connection(ser):
    connection = False
    i = 0
    while connection == False:
        try:
            i = i + 1
            ser.flush()
            ser.write(("AT \r \n").encode())
            time.sleep(2)
            data = ser.read_all().decode()
            print(i, 'data:', data)
            if i >= 10:
                gpio_power_off()
                time.sleep(1)
                gpio_power_on()
                i = 0
            if 'OK' in str(data):
                print('connected')
                connection = True
                return connection
        except:
            print('except', i, ' of 10')
            time.sleep(4)
            if i >= 10:
                connection = True
                return connection


# ping
def at_ping(ser_internet):
    # ser_internet.flush()
    ser_internet.write(('AT+SNPING4="techgeek.biz",1,16,1000 \r \n').encode())
    time.sleep(2)
    data = ser_internet.read_all().decode()
    #data2 = ser_internet.read().decode()
    print('data', data)
    if 'ERROR' in str(data):
        print('error')
        success = False
        return success
    if 'OK' in str(data):
        print('success')
        success = True
        return success
    else:
        print('else')


def at_internet_stop(ser_internet):
    try:
        ser_internet.write(("AT+CACLOSE=0 \r \n").encode())
        time.sleep(.2)
        data = ser_internet.read_all()
        print('data', data)
        ser_internet.write(("AT+CNACT=0,0 \r \n").encode())
        time.sleep(.2)
        data = ser_internet.read_all()
        print('data', data)
    except:
        pass


# open connections, ,this should stay open pretty much indefinitely
def at_internet_start(ser_internet):
    success = False
    while success == False:
        try:
            # AT+CNACT=0,1
            ser_internet.flush()
            ser_internet.write(("AT+CNACT=0,1 \r \n").encode())
            time.sleep(1)
            data = ser_internet.read_all()
            print('data', data)
            if 'ACTIVE' in str(data):
                print('Connected ACTIVE, "AT+CNACT=0,1')
                success = True
            #
            #
            # AT+CACID=0
            ser_internet.flush()
            ser_internet.write(("AT+CACID=0 \r \n").encode())
            time.sleep(1)
            data = ser_internet.read_all()
            print('data', data)
            if 'OK' in str(data):
                print('connected AT+CACID=0')
            else:
                time.sleep(5)
                print('at test')
                at_test_device_connection(ser_internet)
                print('at internet stop')
                at_internet_stop(ser_internet)
                time.sleep(1)
                data = ''
                continue
                #print('restarting now...')
                #ser.write(("AT+CREBOOT \r \n").encode())
        except KeyboardInterrupt:
            break
        except:
            if ser_internet != None:
                print('except')
            """
            # close gprs connection
            send_at('AT+CACLOSE=0', 'OK', 1) # AT+CACLOSE=0
            send_at('AT+CNACT=0,0', 'OK', 1) # AT+CNACT=0,0
            """


def at_gps_start(ser):
    try:
        ser.write(("AT+CGNSPWR=1 \r \n").encode())
        time.sleep(.5)
        data = ser.read_all()
        print('data', data)
        if str(data).startswith("b'AT+CGNSPWR=1") == True:
            print('connected')
    except:
        if ser != None:
            print('except')


def at_gps_stop(ser):
    try:
        ser.write(("AT+CGNSPWR=0 \r \n").encode())
        time.sleep(.5)
        data = ser.read_all()
        print('data', data)
        if str(data).startswith("b'AT+CGNSPWR=0") == True:
            print('disconnected')
    except:
        if ser != None:
            print('except')

