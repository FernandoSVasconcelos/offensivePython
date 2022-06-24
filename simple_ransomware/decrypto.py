import os
from pathlib import Path
from cryptography.fernet import Fernet

dir = Path(r'C:\Users\Fernando\Documents\igti\pwned')
ext = ('.txt', '.pdf')
key_path = 'key.txt'

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

decrypto()