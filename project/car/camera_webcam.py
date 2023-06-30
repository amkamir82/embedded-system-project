import socket
from socket import SHUT_RDWR
from time import sleep
import random

HOST = "192.168.43.150"  # Standard loopback interface address (localhost)
PORT = 65429  # Port to listen on (non-privileged ports are > 1023)


from psutil import process_iter
from signal import SIGTERM # or SIGKILL


def run():
    print("SERVER IS RUNNING")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
       s.bind((HOST, PORT))
       s.listen()
       conn, addr = s.accept()
       while True:
           f_name = f"img_{random.randint(1, 1000)}.jpg"

           while True:
               print(f_name)
               data = conn.recv(1024)
               print(data)
               if data[-4:] == b"NEXT":
                   break

               if not data:
                   sleep(0.001)
                   continue
               print(data)
               with open(f_name, "ab") as f:
                   f.write(data)
                   conn.sendall(b"THANKS")
               conn.sendall(b"THANKS")


run()
