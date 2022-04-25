import RPi.GPIO as GPIO
import time


# does a boot loop if not turned on here
def gpio_power_on():
    power_key = 4
    print('SIM7080X power on:')
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(power_key,GPIO.OUT)
    time.sleep(0.1)
    GPIO.output(power_key,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(power_key,GPIO.LOW)
    time.sleep(1)
    print('SIM7080X is starting up')
    """
    time.sleep(3)
    power_key = 4
    power_key_two = 2
    power_key_three = 1
    power_key_four = 17
    print('SIM7080X power off ')
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    print('one')
    GPIO.setup(power_key,GPIO.OUT)
    time.sleep(0.1)
    GPIO.output(power_key,GPIO.LOW)
    time.sleep(3)
    GPIO.output(power_key,GPIO.HIGH)
    time.sleep(2)
    print('two')
    GPIO.setup(power_key_two, GPIO.OUT)
    GPIO.output(power_key_two, GPIO.LOW)
    time.sleep(3)
    GPIO.output(power_key_two, GPIO.HIGH)
    time.sleep(2)
    print('three')
    GPIO.setup(power_key_three, GPIO.OUT)
    GPIO.output(power_key_three, GPIO.LOW)
    time.sleep(3)
    GPIO.output(power_key_three, GPIO.HIGH)
    time.sleep(2)
    print('four')
    GPIO.setup(power_key_four, GPIO.OUT)
    GPIO.output(power_key_four, GPIO.LOW)
    time.sleep(3)
    GPIO.output(power_key_four, GPIO.HIGH)
    time.sleep(2)
    print('Good bye')
    """


def gpio_power_off():
    power_key = 4
    power_key_two = 2
    power_key_three = 1
    power_key_four = 17
    print('SIM7080X power off ')
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(power_key,GPIO.OUT)
    time.sleep(0.1)
    GPIO.output(power_key,GPIO.HIGH)
    time.sleep(3)
    GPIO.output(power_key,GPIO.LOW)
    time.sleep(2)
    """
    print('two')
    GPIO.setup(power_key_two, GPIO.OUT)
    GPIO.output(power_key_two, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(power_key_two, GPIO.LOW)
    time.sleep(2)
    print('three')
    GPIO.setup(power_key_three, GPIO.OUT)
    GPIO.output(power_key_three, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(power_key_three, GPIO.LOW)
    time.sleep(2)
    print('four')
    GPIO.setup(power_key_four, GPIO.OUT)
    GPIO.output(power_key_four, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(power_key_four, GPIO.LOW)
    time.sleep(2)
    print('Good bye')
    """
