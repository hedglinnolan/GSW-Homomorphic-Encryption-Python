'''This file implements key generation for GSW encryption.'''

from util import *
from math import ceil, log2
import numpy as np
import random

def keyGen(k):
    ''' Input: k - security parameter
        Output: t,B - secret and public key
    '''
    # pick a random Sophie Germain prime [q] in the range 2...2**k
    #   and get its bit length [l]
    stat("Generating modulus [q]")
    q = generateSophieGermainPrime(k)
    l = ceil(log2(q)) # l = np.ceil(np.log2(q)).astype(np.int64)
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
    stat("Generating secret key [t]")
    n = k
    m = n*l
    s = np.random.randint(q, size=n-1, dtype=np.int64)
    t = np.append(-s, 1)
    stat("Generating error vector [e]")
    e = np.rint(np.random.normal(scale=1.0, size=m)).astype(np.int64)
    stat("Generating random matrix [A]")
    A = np.random.randint(q, size=(n-1, m), dtype=np.int64)
    stat("Generating public key [B]")
    B = np.vstack((A, np.dot(s, A) + e))
    return q,s,t,e,A,B

if __name__ == '__main__':
    k = 12 # security parameter

    q,s,t,e,A,B = keyGen(k)
    check = np.dot(t,B)
    okay = np.all(check == e)
    if okay:
        stat("Keygen check passed (t⋅B == e)")
    else:
        stat("Keygen check failed (t⋅B != e)")
