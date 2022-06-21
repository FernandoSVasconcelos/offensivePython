import socket

def scan():
	s = socket.socket()
	abertas = []
	for i in range(9000):
		if(s.connect_ex(("192.168.2.5", i)) == 0):
			print(f"Porta {i} aberta")
			abertas.append(i)
		else:
			print(f"Porta {i} fechada")
	print(f"-----------[Portas Abertas]------------")
	print(abertas)

if __name__ == '__main__':
	scan()