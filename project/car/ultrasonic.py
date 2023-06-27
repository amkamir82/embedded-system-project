import RPi.GPIO as GPIO
import time
import urllib

def measure_distance():
    TRIG = 18
    ECHO = 16

    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    while True:
        print("distance measurment in progress")
        GPIO.output(TRIG,True)
        print("waiting for sensor to settle")
        time.sleep(0.00001)
        GPIO.output(TRIG,False)
        while GPIO.input(ECHO)==0:
            pulse_start=time.time()
        while GPIO.input(ECHO)==1:
            pulse_end=time.time()
        pulse_duration = pulse_end-pulse_start
        distance=(pulse_duration*34000)/2
        distance=round(distance,2)
        print("distance:",distance)
        time.sleep(0.1)
        return distance
