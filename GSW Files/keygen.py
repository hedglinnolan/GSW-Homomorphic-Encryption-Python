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
	q = random.choice(q_array).astype(np.int64)
	l = np.ceil(np.log2(q)).astype(np.int64)
	m = k*l
	print(m.dtype)
	t = np.arange(k, dtype = np.int64)
	for i in range(k-1):
		t[i] = int(FFE(random.randrange(q),q))*(-1)
	t[k-1] = 1
	S = t[:k-1]*(-1)
	e = np.rint(np.random.normal(size = int(m))).astype(np.int64)
	A = np.array([[int(FFE(random.randrange(q),q)) for y in range(int(k-1))] for x in range(int(m))])
	SAE = np.dot(S,np.transpose(A)) + e # Calculating S*A+e
	SAE = np.transpose([SAE]) # This dumb line of code is so the dimensions work out. I hate python so much (#matlab4lyfe)
	B = np.transpose(np.hstack([A,SAE]))
	return q,t,B,e


k = [25] # security parameter

for i in k:
	q, t, B, e = keyGen(i)
	#Check for correctness (t*B = e ideally)
	check = np.dot(t,B)%q
	print(check)
	print(e%q)	