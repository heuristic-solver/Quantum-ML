from qiskit import QuantumCircuit,transpile, Aer
import matplotlib.pyplot as plt 
from qiskit.visualization import plot_histogram



simulator = Aer.get_backend("aer_simulator")
circ = QuantumCircuit(2,2) 
circ.h(0)
circ.cx(0,1) 
circ.save_statevector(label="V1")
circ.measure([0,1], [0,1])

comp = transpile(circ,simulator)
job = simulator.run(comp,shots = 10000)

result = job.result()
counts = result.get_counts(circ)

print("\nTotals for 00 and 11 are:",counts)


