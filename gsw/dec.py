'''This file calls all the functions needed in order to decrypt a GSW ciphertext (in matrix form)
and puts them together into one large function.'''

from util import *
import numpy as np

def decrypt(keys, ciphertext):
    stat("Decrypting message")
    msg  = np.dot(keys.SK, ciphertext) % keys.q
    msg_ = np.minimum(msg, keys.q - msg)
    norm = np.dot(msg_, msg_)
    return (0 if norm < keys.q**2 else 1, msg, norm)

if __name__ == '__main__':
    from keygen import keygen
    from enc import encrypt
    keys = keygen(24)
    for idx in range(16):
        c = encrypt(keys, idx%2)
        m = decrypt(keys, c)
        if m[0] != (idx % 2):
            stat('Failed')
            exit()
    stat('Passed')
