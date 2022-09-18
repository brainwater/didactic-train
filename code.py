import board
import digitalio
import pwmio
import time
import busio
import ipaddress
import ssl
import wifi
import socketpool
import neopixel
try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise
FREQ=1087

class Business:
    # A0 is cool white
    # A1 is warm white

    def __init__(self):
        print("Starting")
        self._initialize()


    def _initLEDs(self):
        self.CW = pwmio.PWMOut(board.A0, duty_cycle=2**16-1, frequency=FREQ)
        self.WW = pwmio.PWMOut(board.A1, duty_cycle=2**16-1, frequency=FREQ)
                                          

    def _initialize(self):
        self._initLEDs()


    @staticmethod
    def percentToDuty(percent):
        f = 1.0 - (percent / 100.0)
        return int(f * (2**16-1))


    def setLED(self, value, led):
        led.duty_cycle = self.percentToDuty(value)


    def setWarm(self, value):
        self.setLED(value, self.WW)


    def setCool(self, value):
        self.setLED(value, self.CW)


    def run(self):
        while True:
            self.setCool(0)
            self.setWarm(2)
            time.sleep(1)
            self.setWarm(5)
            time.sleep(1)
            self.setWarm(10)
            time.sleep(1)
            self.setWarm(20)
            time.sleep(1)
            self.setWarm(40)
            time.sleep(1)
            self.setWarm(70)
            time.sleep(1)
            self.setWarm(100)
            self.setCool(100)
            time.sleep(1)


biz = Business()
biz.setWarm(2)
biz.run()


