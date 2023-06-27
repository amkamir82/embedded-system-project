from time import sleep
import RPi.GPIO as GPIO

def play_sound(loop_count,sleep_duration):
    i = loop_count
    while i>0:
        GPIO.setup(17,GPIO.OUT)
        GPIO.output(17,True)
        print("buzzer is on")
        sleep(sleep_duration)
        GPIO.output(17,False)
        print("buzzer is off")
        sleep(sleep_duration)
        i-=1
    
