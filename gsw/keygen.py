'''This file implements key generation for GSW encryption.'''

from util import *
from math import ceil, log2
import numpy as np
import random

class GSWKeys:
    def __init__(self, k, q, t, e, A, B, datatype):
        self.n  = k
        self.q  = q
        self.l  = ceil(log2(q))
        self.m  = self.n * self.l
        self.SK = t
        self.e  = e
        self.A  = A
        self.PK = B
        self.datatype = datatype

def keygen(k):
    if k > 29:
        datatype = 'object'
    else:
        datatype = np.int64
    # pick a random Sophie Germain prime [q] in the range 2...2**k
    #   and get its bit length [l]
    stat("Generating modulus")
    q = generateSophieGermainPrime(k)
    l = ceil(log2(q))
    print(" "*12 + "q = %d" % q)
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
    stat("Generating secret key")
    n = k
    m = n*l
    s = np.random.randint(q, size=n-1, dtype=np.int64).astype(datatype)
    t = np.append(s, 1)
    stat("Generating error vector")
    e = np.rint(np.random.normal(scale=1.0, size=m)).astype(np.int).astype(datatype) # This makes me die a little bit on the inside.
    stat("Generating random matrix")
    A = np.random.randint(q, size=(n-1, m), dtype=np.int64).astype(datatype)
    stat("Generating public key")
    B = np.vstack((-A, np.dot(s, A) + e)) % q

    check = np.dot(t, B) % q
    okay = np.all(check == (e % q))
    if okay:
        stat("Keygen check passed") # t⋅B == e
    else:
        stat("\x1B[31;1mKeygen check failed\x1B[0m") # t⋅B != e

    return GSWKeys(k, q, t, e, A, B, datatype)

if __name__ == '__main__':
    keygen(48)
