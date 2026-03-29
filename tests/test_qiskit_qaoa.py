from qiskit import QuantumCircuit

EDGES = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]

def qaoa_maxcut_circuit(num_nodes, edges, gamma, beta, measure=False):
    qc = QuantumCircuit(num_nodes, num_nodes if measure else 0)
    for q in range(num_nodes):
        qc.h(q)
    for u, v in edges:
        qc.cx(u, v)
        qc.rz(-gamma, v)
        qc.cx(u, v)
    for q in range(num_nodes):
        qc.rx(2 * beta, q)
    if measure:
        qc.measure(range(num_nodes), range(num_nodes))
    return qc

def test_qaoa_circuit_width():
    qc = qaoa_maxcut_circuit(4, EDGES, 0.7, 0.4, measure=True)
    assert qc.num_qubits == 4
    assert qc.num_clbits == 4

def test_qaoa_has_measurements_when_requested():
    qc = qaoa_maxcut_circuit(4, EDGES, 0.7, 0.4, measure=True)
    ops = qc.count_ops()
    assert "measure" in ops
