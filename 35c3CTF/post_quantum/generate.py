
from challenge import CodeBasedEncryptionScheme

from random import SystemRandom
from os import urandom



if __name__ == "__main__":
    cipher = CodeBasedEncryptionScheme.new()
    random = SystemRandom()
    for i in range(1024 + 512):
        pt = urandom(2)
        ct = cipher.encrypt(pt)
        with open("plaintext_{:03d}".format(i), "wb") as f:
            f.write(pt)
        with open("ciphertext_{:03d}".format(i), "wb") as f:
            f.write(ct)
        assert(pt == cipher.decrypt(ct))

    with open("flag.txt", "rb") as f:
       flag = f.read().strip()

    if len(flag) % 2 != 0:
        flag += b"\0"

    cts = list()
    for i in range(len(flag) // 2):
        cts.append(cipher.encrypt(flag[i*2:i*2 + 2]))

    for i, ct in enumerate(cts):
        with open("flag_{:02d}".format(i), "wb") as f:
            f.write(ct)
