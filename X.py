from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

qc = QuantumCircuit(1,1)
while True:
    inp = int(input("For turn on qubit type '1' esle '0' : "))
    qc.x(0)
    qc.measure(0,0)
    backend = AerSimulator()
    transpiled = transpile(qc, backend)
    job = backend.run(transpiled, shots=1)
    result = job.result()
    counts = result.get_counts()
    print(counts)
