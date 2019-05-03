'''This file implements key generation for GSW encryption.'''

import numpy as np
import random    
 

# Keygen function
def keyGen(k):
	''' Generates the secret key and pulic key given a security parameter k.

	Input: k - security parameter (i.e. # of bits in key)
	Output: sk - secret key
			pp = (n.q) - parameters known to the public'''
	q_array = generateSophieGermainPrimes(k)
	q = random.choice(q_array)
	l = np.ceil(q)
	return q, l


k = 20 # security parameter