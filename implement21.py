import math
from qiskit import QuantumProgram, QuantumCircuit

QuantumExperience_1 = QuantumProgram()

# Allocating a 9-qubit Quantum Computer, and creating a Quantum Circuit
qr = QuantumExperience_1.create_quantum_register("qr", 10)
cr = QuantumExperience_1.create_classical_register("cr", 10)
qc = QuantumExperience_1.create_circuit("implementation21", [qr], [cr])
# Quantum Circuit Created

# Note: All Gates Available: h, x, cx, u1, u2, u3, y, z, s, t, tdg, iden, measure, barrier

# Define Quantum Fourier Transform
def qft(circ, q, n):
    # n-qubit QFT on q in circ
    for j in range(n):
        for k in range(j):
            circ.cu1(math.pi / float(2 ** (j - k)), q[j], q[k])
        circ.h(q[j])


# QFT defined

# Define SWAP Gate
def swap(circ, q1, q2):
    circ.cx(q2, q1)
    circ.cx(q1, q2)
    circ.cx(q2, q1)
# SWAP Gate Defined

# Customer Gate: QFT, SWAT

# Applying Quantum Assembly Code

qc.x(qr[1])

# U2,21 Gate
# Note: Applicable 1 2 4 6 8; Zeroes: 3 5 7 9
qc.x(qr[3])
qc.x(qr[4])
qc.x(qr[5])
qc.x(qr[7])
qc.x(qr[8])
qc.ccx(qr[1],  qr[2], qr[3])
qc.ccx(qr[3],  qr[4], qr[5])
qc.ccx(qr[5],  qr[6], qr[7])
qc.ccx(qr[7],  qr[8], qr[9])
qc.ccx(qr[5],  qr[6], qr[7])
qc.x(qr[8])
qc.x(qr[9])
qc.ccx(qr[3],  qr[4], qr[5])
qc.x(qr[7])
qc.x(qr[4])
qc.cx(qr[9], qr[4])
qc.ccx(qr[3],  qr[4], qr[5])
qc.cx(qr[9], qr[8])
qc.ccx(qr[5],  qr[6], qr[7])
qc.ccx(qr[7],  qr[9], qr[8])
qc.ccx(qr[5],  qr[6], qr[7])
qc.ccx(qr[5],  qr[9], qr[6])
qc.ccx(qr[3],  qr[4], qr[5])
qc.x(qr[3])
qc.x(qr[5])
qc.ccx(qr[3], qr[9], qr[4])
qc.ccx(qr[1], qr[2], qr[3])
qc.ccx(qr[9],  qr[1], qr[2])
qc.cx(qr[9], qr[1])
swap(qc, qr[6], qr[8])
swap(qc, qr[4], qr[6])
swap(qc, qr[2], qr[4])
swap(qc, qr[1], qr[2])
qc.cx(qr[9], qr[1])
qc.cx(qr[1], qr[9])
# End of U2,21 Gate

# Measurement
qc.measure(qr, cr)

# Get & Print result
result = QuantumExperience_1.execute(["implementation21"], backend='local_qasm_simulator', shots=128)
print(result)
print(result.get_data("implementation21"))

# Quantum Assembly Code Fully Applied