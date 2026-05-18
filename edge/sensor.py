import RPi.GPIO as GPIO
import time


class UltrasonicSensor:
    def __init__(self, trig_pin, echo_pin):
        self.trig = trig_pin
        self.echo = echo_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trig, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)

    def read(self):
        """Return distance in centimeters."""
        GPIO.output(self.trig, False)
        time.sleep(0.1)
        GPIO.output(self.trig, True)
        time.sleep(0.00001)
        GPIO.output(self.trig, False)

        pulse_start = time.time()
        while GPIO.input(self.echo) == 0:
            pulse_start = time.time()

        pulse_end = time.time()
        while GPIO.input(self.echo) == 1:
            pulse_end = time.time()

        distance = (pulse_end - pulse_start) * 17150
        return round(distance, 2)
