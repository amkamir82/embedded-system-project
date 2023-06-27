import socket

HOST = "192.168.43.150"
PORT = 65432

def send_msg(data):
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((HOST, PORT))
		s.sendall(data)
		data = s.recv(1024)

	print(f"GOT {data}")