import RPi.GPIO as GPIO
from gpiozero import Buzzer

from buzzer import play_sound
from ultrasonic import measure_distance

if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    while True:
        print("hi")
        distance = measure_distance()
        if distance >50:
            play_sound(1,1)
        elif 40<distance<50:
            play_sound(1,1)
        elif 30<distance<40:
            play_sound(2,1)      
        elif 20<distance<30:
            play_sound(3,0.5)
        elif 10<distance<20:
            play_sound(3,0.3)
        elif 0<distance<10:
            play_sound(5,0.1)
