# QAOA Max-Cut submission scaffold

This folder contains a notebook-first submission scaffold for PHY5003 Assessment 1.

## Files

- `QAOA_MaxCut_Assignment.ipynb` — main explanatory notebook
- `qsharp/QAOAMaxCut.qs` — standalone Q# version of the QAOA circuit
- `tests/test_classical_maxcut.py` — basic classical tests
- `tests/test_qiskit_qaoa.py` — basic Qiskit circuit tests
- `requirements.txt` — Python dependencies

## Notes

- The notebook uses **Qiskit** for the executable quantum workflow and OpenQASM 3 export.
- The Q# path is provided both in the notebook and as a standalone `.qs` file.
- The notebook was generated as a scaffold and should be run in your local environment with Qiskit and the QDK installed.
- As long as the 'mqit-quantum-sw' kernel is selected as the kernel of the vscode, the environment should work. If you want to run the test, please use pytest after activating the mqit-quantum-sw environment in the powershell. 
