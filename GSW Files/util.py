import numpy as np
from scipy.linalg import block_diag

def buildGadget(l, n): # Returns the gadget matrix for a given modulus
	g = np.linspace(0, l - 1, l)[np.newaxis]
	print(g.shape)
	g = 2 ** g
	return block_diag(*[g for i in range(0, n)]) 

if __name__ == '__main__':
	print(buildGadget(10, 30))