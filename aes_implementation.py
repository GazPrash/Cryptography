import os
import binascii
import random

from cryptography.hazmat.primitives.ciphers import algorithms, modes, Cipher
from cryptography.hazmat.backends import default_backend
from scipy import rand

sys_rand = random.SystemRandom()

main_key = os.urandom(16)
print("Main Key: ", "%s" % binascii.hexlify(main_key), end="\n\n")


aes = Cipher(
    algorithm= algorithms.AES(main_key),
    mode= modes.ECB(),
    backend= default_backend()
)

aes_encryption = aes.encryptor()
plaintext = "\x00"*16

# this may not work with py3 for some reason only followed
# via "Serious Cryptography"
# use pycrypto for proper implementation
ciphertext = aes_encryption.update(plaintext) + aes_encryption.finalize()
print("Encrypted Cipher Text: ", "%s" % binascii.hexlify(ciphertext))



