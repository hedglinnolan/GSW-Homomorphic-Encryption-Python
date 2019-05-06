'''This file calls all the functions needed in order to decrypt a GSW ciphertext (in matrix form)
and puts them together into one large function.'''

import numpy as np

def decrypt(sk, c):
    return np.dot(sk, c) > 0.5
