'''This file implements key generation for GSW encryption.'''

import numpy as np
import random
from util import *
from galois import FFE

def keyGenParams(k):
	''' Generates the secret key and pulic key given a security parameter k.

	Input:  k - security parameter (i.e. # of bits in key)

	Output: q - safe prime used for all operations
			l - log(q) (used for matrix dimensions)
			m - k*l (also used for dimensions)
	'''
	q_array = generateSafePrimes(k)
	q = random.choice(q_array)
	l = np.ceil(np.log2(q))
	m = k*l
	return q, l, m

def secretKey(k):
	''' Input: k - security paramter

		Output: t - binary secrety key in string form
	'''
	q,l,m = keyGenParams(k)
	S = FFE(random.randrange(q),q)
	print(S)
	t = bin(int(S)).zfill(k-1) + str(1)
	print(t)
	return t

def errorVec(k):
	''' Input: k - security paramter

		Output: e - error vector used for GSW encryption
	'''

def publicKey(k):
	''' Input: k - security parameter
		Output: B - n x m matrix used as public key
	'''

def keyGen(k):
	''' Input: k - security paramter

		Output: t,B - secret and public keys for user
	'''
	t = secretKey(k)
	B = publicKey(k)
	return t, B

k = [5,10,20] # security parameter

for i in k:
	secretKey(i)