"""Script for preparing the Bell state |\Phi^{+}> in Cirq. """

# Import the Cirq library
import cirq


def circuit_Bell(B):
    # Get qubits and circuit
    qreg = [cirq.LineQubit(x) for x in range(2)]
    circ = cirq.Circuit()

    # Add the Bell state preparation circuit
    if B == '00':
        circ.append([cirq.H(qreg[0]),cirq.CNOT(qreg[0], qreg[1])])
    elif B == '10':
        circ.append([cirq.X(qreg[0]),cirq.H(qreg[0]),cirq.CNOT(qreg[0], qreg[1])])
    elif B == '01':
        circ.append([cirq.H(qreg[0]),cirq.CNOT(qreg[0], qreg[1]),cirq.X(qreg[1])])
    elif B == '11':
        circ.append([cirq.X(qreg[0]),cirq.H(qreg[0]),cirq.CNOT(qreg[0], qreg[1]),cirq.X(qreg[1])])  

    circ.append([cirq.CNOT(qreg[0],qreg[1]),cirq.H(qreg[0])])

    # Display the circuit
    print()
    print(circ)

    # Add measurements
    circ.append(cirq.measure(*qreg, key="z"))

    # Simulate the circuit
    sim = cirq.Simulator()
    res = sim.run(circ, repetitions=100)

    # Display the outcomes
    print("\nMeasurements:")
    print(res.histogram(key="z"))

for B,D in {'00':0,'01':1,'10':2,'11':3}.items():
    print("Circuit B{} so we expect to measure {}".format(B,D))
    circuit_Bell(B)
    print('\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n')
