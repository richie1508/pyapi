import RPi.GPIO as GPIO
import time

def led(cnt=1):
    ledPin = 18
    lowSec = 0.5
    highSec = 0.5
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ledPin, GPIO.OUT)
    idx = 0
    while idx < cnt:
        # led
        GPIO.output(ledPin, GPIO.LOW)
        time.sleep(lowSec)
        GPIO.output(ledPin, GPIO.HIGH)
        time.sleep(highSec)
        idx += 1