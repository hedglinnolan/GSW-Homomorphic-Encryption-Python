import qiskit as qk
import Qconfig
from qiskit import IBMQ

#Choosing a quantum computer as the backend for performing the task
IBMQ.save_account(Qconfig.APItoken)
IBMQ.load_accounts()
ibmqxf = IBMQ.get_backend('ibmq_16_melbourne')

#Creating the quantum register
def createQC(n):
    '''Creates a quantum circuit of depth n (i.e. n qubits being used)

    In: n - # of qubits desired
    
    Out:qr - the register of n qubits to be manipulated
        cr - the corresponding classical register that will be used to store measurements of qubits
        qc - the actual quantum circuit
    '''
    qr = qk.QuantumRegister(n, name = 'qr') #enumerating the qubits we want to use for our circuit
    cr = qk.ClassicalRegister(n, name = 'cr') #created so we can see the output of the quantum computer by mapping qubit measurements to classical values
    qc = qk.QuantumCircuit(qr,cr, name = 'qc')
    return qr,cr,qc

#Preparing a bell state. A bell state is an entangled pair (|00> + |11>)/sqrt(2).
def bellState(i,j,qc,qr):
    '''Manipulates a circuit so that it contains the gates needed to get a bell state between i and j 
    (i.e. i and j are now entangled). Assumes that qubits i,j start in |0> state.

    In: i - the first qubit. Hadamard operation is performed on this qubit.
        j - the second qubit. Controlled by CNOT operation driven by qubit i
        qc - the quantum circuit being changed
        qr - the register where qubits i and j are located
    
    Out: Appends the gates needed to create a bell state to the existing quantum circuit.
    '''
    qc.h(qr[i]) #qr[i] is the ith qubit in the quantum register
    qc.cx(qr[i],qr[j]) #CNOT between i and j qubit

#Creates a GHZ state using qubit i through j. A GHZ state is like a super bell state in the form (|00...0> + |11...1>)/sqrt(2).
def GHZState(i,j,qc,qr):
    '''Creates a GHZ state of all qubits between i and j (i.e. qubits i through j are now entangled). Assumes that qubits i,...,j  all start in |0> state.

    In: i - the first qubit. Hadamard operation is performed on this qubit. Drives the entanglement operation for all subsequency qubits using CNOT gate.
        j - the final qubit to be entangled.
    
    Out: Appends the gates needed to create a GHZ state to the existing quantum circuit.
    '''
    qc.h(qr[i])
    for k in range(i,j+1):
        qc.cx(qr[i],qr[k])

#Creating measurement circuits
def basisMeasure(qr,cr):
    '''Creates a mini-circuit that measures the outcome of a larger circuit in the basis state (i.e. |0> and |1>).

    In: n/a
    
    Out: Appends the gates needed to perform a measurement in the standard computation basis.
    '''
    measure_Z = qk.QuantumCircuit(qr,cr)
    measure_Z.measure(qr,cr)
    return measure_Z

#Measuring in the hadamard basis
def hadamardMeasure(qr,cr):
    '''Creates a mini-circuit that measures the outcome of a larger circuit in the hadamard state (i.e. (|0> + |1>)/sqrt(2) and (|0> - |1>)/sqrt(2)).
    All that is really different from the computational measurement function is that we perform a hadamard gate before measuring.
    
    In: n/a
    
    Out: Appends the gates needed to perform a measurement in the hadamard basis.
    '''
    measure_X = qk.QuantumCircuit(qr,cr)
    measure_X.h(qr)
    measure_X.measure(qr,cr)
    return measure_X
