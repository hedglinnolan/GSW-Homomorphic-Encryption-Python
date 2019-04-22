import numpy as np
from qiskit_aqua import Operator, run_algorithm
from qiskit_aqua.input import EnergyInput
from qiskit_aqua.translators.ising import partition
from qiskit import Aer
import threading
import time


''' This file creates a random list of numbers and then partitions the list into two disjoint sets such that the distance between
them is minimized.
'''

#A mini progress tracker to see how long the program has been running
def progress():
  threading.Timer(10.0, progress).start()
  print('still running...')

progress()

#Generate a random list of numbers to be partitioned
np.random.seed(10)
n=5
number_list = partition.random_number_list(n, weight_range=25)

#Turn the number list into ciphertext
m = 0x1d7777c38863aec21ba2d91ee0faf51
e = 0x5abb
d = 0x1146bd07f0b74c086df00b37c602a0b
c_list = []
for i in range(n):
	c_list.append(pow(int(number_list[i]), int(e), int(m)))

#Load the number list into the quantum register
qubitOp, offset = partition.get_partition_qubitops(np.array(c_list))
algo_input = EnergyInput(qubitOp)
print(number_list)
print(c_list)

#Encrypt the number list using RSA encryption


to_be_tested_algos = ['ExactEigensolver', 'VQE']
#print(to_be_tested_algos)

#Build a dictionary for solving this problem using the E
algorithm_cfg = {
    'name': 'ExactEigensolver',
}

params = {
    'problem': {'name': 'ising'},
    'algorithm': algorithm_cfg
}
result = run_algorithm(params,algo_input)

#Partition the set using the exact eigensolver (classical) algorithm
x = partition.sample_most_likely(result['eigvecs'][0])
print('energy:', result['energy'])
print('partition objective:', result['energy'] + offset)
print('solution:', x)
print('solution objective:', partition.partition_value(x, np.array(c_list)))

print('...\nRunning VQE')


#Build a dictionary for the variational quantum eigensolver. It is a type of optimization algorithm that uses the quantum computer
algorithm_cfg = {
    'name': 'VQE',
    'operator_mode': 'matrix'
}

optimizer_cfg = {
    'name': 'L_BFGS_B',
    'maxfun': 6000
}

var_form_cfg = {
    'name': 'RYRZ',
    'depth': 3,
    'entanglement': 'linear'
}

params = {
    'problem': {'name': 'ising'},
    'algorithm': algorithm_cfg,
    'optimizer': optimizer_cfg,
    'variational_form': var_form_cfg
}

#Choose your backend and run the partition task using that backend
backend = Aer.get_backend('statevector_simulator')
result = run_algorithm(params, algo_input, backend=backend)

x = partition.sample_most_likely(result['eigvecs'][0]) #Assigns the number in that position of the list to either Set 0 or Set 1
print('energy:', result['energy'])
print('time:', result['eval_time'])
print('partition objective:', result['energy'] + offset)
print('solution:', x)