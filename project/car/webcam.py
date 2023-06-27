import RPi.GPIO as GPIO
import requests
import socket
from time import sleep
from socket_msg import send_msg

MOB_IP = "192.168.43.1"
MOB_PORT = 8080

def capture_img():
    print("CAPTURING IMAGE...")
    resp = requests.get(f"http://{MOB_IP}:{MOB_PORT}/photo.jpg")
    print(resp.status_code)
    send_msg(resp.content)
    print("IMAGE SENT")

capture_img()