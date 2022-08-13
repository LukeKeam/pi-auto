import RPi.GPIO as GPIO
import time


def gpio_power_on():
    power_key = 4
    print('SIM7080X power on:')
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(power_key, GPIO.OUT)
    time.sleep(0.1)
    GPIO.output(power_key, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(power_key, GPIO.LOW)
    time.sleep(1)
    print('SIM7080X is starting up')


def gpio_power_off():
    power_key = 4
    # notes
    # power_key_two = 2
    # power_key_three = 1
    # power_key_four = 17
    print('SIM7080X power off ')
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(power_key, GPIO.OUT)
    time.sleep(0.1)
    GPIO.output(power_key, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(power_key, GPIO.LOW)
    time.sleep(2)
