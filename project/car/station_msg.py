import socket
from socket import SHUT_RDWR
from time import sleep


HOST = "192.168.43.150"  # Standard loopback interface address (localhost)
PORT = 65420  # Port to listen on (non-privileged ports are > 1023)


from psutil import process_iter
from signal import SIGTERM # or SIGKILL


CAR_IP = "192.168.43.16"
CAR_PORT = 65432

def create_car_sock():
     print(CAR_IP)
     print(CAR_PORT)
     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     s.connect((CAR_IP, CAR_PORT))
     return s
     
     
def inform_car(s):
     s.sendall(b"REDUCE YOUR SPEED")
     print("DATA SENT")


def run():
    print("SERVER IS RUNNING")
    car_sock = create_car_sock()
    print("CAR SOCKET CREATED")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
       s.bind((HOST, PORT))
       s.listen()
       conn, addr = s.accept()
       print(str(addr) +" CONNECTED")
       sleep(5)
       inform_car(car_sock)
       while True:
               data = conn.recv(1024)
               if not data:
                   sleep(0.001)
                   continue
               print(data)
               conn.sendall(b"THANKS")


run()
