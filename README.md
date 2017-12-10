# Quantum Computing

## Introduction
Our code gives simple examples of implementations of _ Quantum Computing _. With Python and SDKs provided, we can stimulate a Quantum Computer on our classical computer, or to upload our code to IBM Bluemix and run in IBMQ Quantum Computers.

## SDK
** Python 3.5 ** or above is required.
[QISkit and other SDKs](https://github.com/QISKit/qiskit-sdk-py) are required. These SDKs can also be downloaded from pip. SDK requirements and recommended versions are listed below: 
- _ QISKIT _
	Latest Version.
- _ IBMQuantumExperience _
	Latest Version.
_ Qconfig _ could be found in the _ qiskit_ folder, and API Token of which can be attained from [IBM Quantum Experience](https://quantumexperience.ng.bluemix.net/qx) once you register an IBMQ Account.

## Shor’s Algorithm
Shor’s Algorithm is considered to be the most efficient way to _ decrypt RSA crypto system _, due to its ability to fracture a large integer N into prime numbers p1 and p2. Simply quantum gate to fracture 15 is available on IBMQ computer, while others could be done by simulating quantum computers with large qubits.

## Implementation 21
The first implementation here is Shor’s Algorithm on fracturing 21. The main step of Shor’s Algorithm is to design a quantum gate that would accomplish y=ax%N. Now suppose we define such a quantum gate as U(a,N), so in this example, an U(2,21) gate is defined.

