'''This file calls all the functions needed in order to encrypt a bit using GSW
and puts them together into one large function.'''

from util import *
import numpy as np
from scipy.linalg import block_diag

def buildGadget(l, n):
    #
    # the gadget matrix [G] is an n×m matrix (n rows, m = n×l columns)
    #
    # the secret vector [s] is an (n-1)-dimensional vector,
    #   the secret key [t] is -s‖1, an n-dimensional vector
    #
    # the error vector [e] is an m-dimensional vector
    #
    # the matrix [A] is an (n-1)×m matrix (n-1 rows, m = n×l columns)
    #
    # the public key [B] is (   A  )
    #                       ( sA+e )
    #
    g = 2**np.arange(l)
    return block_diag(*[g for null in range(n)])

def encrypt(keys, message):
    stat("Encrypting message")
    R = np.random.randint(2, size=(keys.m, keys.m), dtype=np.int64).astype(keys.datatype)
    G = buildGadget(keys.l, keys.n)
    return (np.dot(keys.PK, R) + message*G) % keys.q

if __name__ == '__main__':
    from keygen import keygen
    keys = keygen(16)
    encrypt(keys, 1)
