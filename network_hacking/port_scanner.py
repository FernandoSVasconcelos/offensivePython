import socket

def scan():
	s = socket.socket()
	for i in range(80):
		if(s.connect_ex(("192.168.2.5", i)) == 0):
			print(f"Porta {i} aberta")
		else:
			print(f"Porta {i} fechada")

if __name__ == '__main__':
	scan()
