from time   import time
from math   import floor
from random import randint

import numpy as np
from scipy.linalg import block_diag

start = None
def stat(msg):
    global start
    now = time()
    if start is None:
        start = now
    print("%10.4f  %s" % (now-start, msg))

def powmod(a, b, m):
    """ Returns the power a**b % m """
    # a^(2b) = (a^b)^2
    # a^(2b+1) = a * (a^b)^2
    if b==0:
        return 1
    return ((a if b%2==1 else 1) * powmod(a, b//2, m)**2) % m

def is_prime(p):
    """ Returns whether p is probably prime """
    for null in range(16):
        a = randint(1,p-1)
        if powmod(a,p-1,p) != 1:
            return False
    return True

def gen_prime(b):
    """ Returns a prime p with b bits """
    p = randint(2**(b-1), 2**b)
    while not is_prime(p):
        p = randint(2**(b-1), 2**b)
    return p

def generateSophieGermainPrime(k):
    """ Return a Sophie Germain prime p with k bits """
    p = gen_prime(k-1)
    sp = 2*p + 1
    while not is_prime(sp):
        p = gen_prime(k-1)
        sp = 2*p + 1
    return p

#def sieve(n):
#    ''' Returns a list of `n` booleans, where the
#        i-th boolean is the primality of i.
#    '''
#    p = 2
#    prime = [False, False] + [True]*(n-2)
#    for p in range(2, floor(n**0.5)+1):
#        if prime[p]:
#            for i in range(p*2, n, p):
#                prime[i] = False
#    return prime
#
#def generateSophieGermainPrimes(k):
#    ''' Return a list of Sophie Germain primes up to 2**k. '''
#    sg = []
#    n = 2**k
#    prime = sieve(2*n+1)
#    for i in range(2, n+1):
#        if prime[i] and prime[2*i+1]:
#            sg.append(i)
#    sg = np.array(sg)
#    return sg

def buildGadget(l, n):
    g = np.linspace(0, l-1, l)[np.newaxis]
    g = 2**g
    return block_diag(*[g for i in range(n)])

