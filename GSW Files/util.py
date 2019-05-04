import numpy as np
from scipy.linalg import block_diag
import random

# Function to detect prime number 
def sieve(n, prime): 
    p = 2
    while( p * p <= n ): 
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * 2, n, p): 
                prime[i] = False
        p += 1
          
                  
def generateSafePrimes(k): 
	''' We have made array till 2*n +1 so that we can check prime number till that and conclude about sophie german prime .
		
	Input: k - security parameter
	Output: q_array - randomly selects q from array of sophie germain primes'''

	q_list = []
	n = 2 ** k # representing k-bit number in base 10
	prime = [True]*(2 * n + 1) 
	sieve(2 * n + 1, prime) 
	for i in range(2, n + 1): # checking every i whether it is sophie german prime or not. 
		if (prime[i] and prime[2 * i + 1]): 
			q_list.append(i)
	q_array = np.array(q_list)
	return q_array


def buildGadget(l, n): # Returns the gadget matrix for a given modulus
    g = np.linspace(0, l - 1, l)[np.newaxis]
    print(g.shape)
    g = 2 ** g
    return block_diag(*[g for i in range(n)])

if __name__ == '__main__':
    pass
