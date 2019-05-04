'''This file implements key generation for GSW encryption.'''

import numpy as np
import random
from util import *
from galois import FFE

def keyGen(k):
	''' Input: k - security parameter

		Output: t,B - secret and public key
	'''
	q_array = generateSafePrimes(k)
	q = random.choice(q_array)
	l = np.ceil(np.log2(q))
	m = k*l
	t = np.arange(k)
	for i in range(k-1):
		t[i] = int(float(FFE(random.randrange(q),q))*(-1))
	t[k-1] = 1
	S = t[:k-1]*(-1)
	e = np.random.normal(size = int(m))
	A = np.array([[float(FFE(random.randrange(q),q)) for y in range(int(k-1))] for x in range(int(m))])
	SAE = np.dot(S,np.transpose(A)) + e# Calculating S*A+e
	SAE = np.transpose([SAE]) # This dumb line of code is so the dimensions work out. I hate python so much (#matlab4lyfe)
	B = np.transpose(np.hstack([A,SAE]))
	return t,B,e


k = [7] # security parameter

for i in k:
	t,B, e = keyGen(i)
	#Check for correctness (t*B = e ideally)
	check = np.dot(t,B)
	print(check)
	print(e)	