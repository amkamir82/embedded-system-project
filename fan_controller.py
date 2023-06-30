import socket
from time import sleep

HOST = "192.168.43.16"
PORT = 65432

def run():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("CAR SERVER IS RUNNING")
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        print(str(addr) + "CONNECTED")
        while True:
            data = conn.recv(1024)
            if not data:
                sleep(0.001)
                continue
            print(data)
            conn.sendall(b"GOT IT")
            
run()
