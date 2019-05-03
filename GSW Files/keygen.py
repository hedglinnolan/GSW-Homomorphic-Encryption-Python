'''This file implements key generation for GSW encryption.'''

import numpy as np
import random

# Python 3 program to print all sophie
# german prime number till n.

# Function to detect prime number
def sieve(n, prime) :
    p = 2
    while( p * p <= n ):
        # If prime[p] is not changed,
        # then it is a prime
        if (prime[p] == True) :

            # Update all multiples of p
            for i in range(p * 2, n, p) :
                prime[i] = False

        p += 1


def printSophieGermanNumber(n) :
    # We have made array till 2*n +1
    # so that we can check prime number
    # till that and conclude about sophie
    # german prime.
    prime = [True]*(2 * n + 1)

    sieve(2 * n + 1, prime)

    for i in range(2, n + 1) :

        # checking every i whether it is
        # sophie german prime or not.
        if (prime[i] and prime[2 * i + 1]) :
            print(i)


# Driver Code
n = 25
printSophieGermanNumber(n)
