import Std.Intrinsic.*;
import Std.Measurement.*;
import Std.Arrays.*;

operation RunQAOAMaxCut(gamma : Double, beta : Double) : Result[] {
    // Same 4-node graph used in the notebook:
    // edges = [(0,1), (1,2), (2,3), (3,0), (0,2)]
    use qubits = Qubit[4];

    // Initial |+>^n state
    for q in qubits {
        H(q);
    }

    // Cost layer using CX-Rz-CX for each edge.
    // Up to a global phase, this corresponds to the Max-Cut cost unitary.
    CNOT(qubits[0], qubits[1]);
    Rz(-gamma, qubits[1]);
    CNOT(qubits[0], qubits[1]);

    CNOT(qubits[1], qubits[2]);
    Rz(-gamma, qubits[2]);
    CNOT(qubits[1], qubits[2]);

    CNOT(qubits[2], qubits[3]);
    Rz(-gamma, qubits[3]);
    CNOT(qubits[2], qubits[3]);

    CNOT(qubits[3], qubits[0]);
    Rz(-gamma, qubits[0]);
    CNOT(qubits[3], qubits[0]);

    CNOT(qubits[0], qubits[2]);
    Rz(-gamma, qubits[2]);
    CNOT(qubits[0], qubits[2]);

    // Mixer layer
    for q in qubits {
        Rx(2.0 * beta, q);
    }

    let results = MeasureEachZ(qubits);
    ResetAll(qubits);
    return results;
}
