import RPi.GPIO as GPIO
from gpiozero import Buzzer
import config
from button import for_back_handler
from buzzer import play_sound
from ultrasonic import measure_distance
import time
from buzzer_back import buzzer_highway, buzzer_not_highway
from bluetooth import send_notif
from webcam import capture_img
from socket_msg import create_socket




def forward_controller():
    if config.HIGHWAY:
        sock = create_socket(65429)
        while True:
            distance = measure_distance()
            time.sleep(0.5)
            highway_buzzer_controller(distance, sock)
    else:
        while True:
            distance = measure_distance()
            time.sleep(0.5)
            no_highway_buzzer_controller(distance)
            

def highway_buzzer_controller(distance, sock):
    if distance<50:
        buzzer_highway()
        capture_img(sock)
        send_notif("notif.txt")

def no_highway_buzzer_controller(distance):
    if distance<50:
        buzzer_not_highway()

def backward_buzzer_controller():
    while True:
        distance = measure_distance()
        time.sleep(0.5)
        if 40<distance<50:
            play_sound(1,1)
        elif 30<distance<40:
            play_sound(3,0.7)      
        elif 20<distance<30:
            play_sound(4,0.5)
        elif 10<distance<20:
            play_sound(5,0.3)
        elif 0<distance<10:
            play_sound(6,0.1)

if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    direction = for_back_handler()
    
    if direction:
        forward_controller()
    else:
        backward_buzzer_controller()
