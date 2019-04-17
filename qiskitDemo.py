''' This is just a small demo to see if we can create bell states and access an actual QC like in the video.

For more info on the basics of qiskit, check out the jupyter notebooks on their github. https://github.com/Qiskit

I only imported the visulatization tools I thought were sufficient/cool, but there are plenty more.
'''

import qiskit as qk
from qiskit.tools.visualization import plot_histogram, plot_state_qsphere, plot_bloch_vector, plot_bloch_multivector, circuit_drawer
import Qconfig
import quantumFunctions as qf
import seaborn as sns
sns.set()

#Store values for number of qubits and the qubits being addressed 
gateDepth = 2
qr,cr,qc = qf.createQC(gateDepth)

#Creating a circuit to prepare the bell state. All functions can be found in quantumFunctions.py
qubitI = 0
qubitJ = 1

qf.bellState(qubitI,qubitJ,qc,qr)

#Initialize measurement circuits
measure_Z = qf.basisMeasure(qr,cr)
measure_X = qf.hadamardMeasure(qr,cr)

#Split the original circuit to perform Z measurment and X measurement
#Append circuits using the addition operator
test_Z = qc + measure_Z
test_X = qc + measure_X

#Draw the quantum circuit
qc.draw()

#Running the circuits on a quantum simulator with 1000 trials
job_1 = qk.execute([test_Z,test_X], backend = qf.sim, shots = 1000)
result_1 = job_1.result()

counts_1Z = result_1.get_counts(test_Z)
counts_1X = result_1.get_counts(test_X)

print(counts_1Z)
print(counts_1X)

#psi = result_1.get_statevector(test_Z) #Should return the equation for a bell state
#plot_state_qsphere(psi) #plotting it on the bloch sphere!

#Running the circuits on an actual IBM quantum computer (refer to quantumFunctions.py for name of backend)
job_2 = qk.execute([test_Z,test_X], backend = qf.ibmqxf, shots = 1000)
result_2 = job_2.result()

counts_2Z = result_2.get_counts(test_Z)
counts_2X = result_2.get_counts(test_X)

print(counts_2Z)
print(counts_2X)

#Plot the results. There are a ton of different ways to plot using qiskit
legend = ['QASM Simulator',qf.ibmqxf]
plot_histogram([counts_1Z, counts_2Z], legend = legend, title='Entanglement Generation Fidelity (computational basis)').savefig('standard.png')
plot_histogram([counts_1X, counts_2X], legend = legend, title= 'Entanglement Generation Fidelity (Hadamard basis)').savefig('hadamard.png')
