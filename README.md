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
- As long as the 'mqit-quantum-sw' kernel is selected as the kernel of the VS Code, the environment should work. If you want to run the test, please use pytest after activating the mqit-quantum-sw environment in the powershell. 

## How to run
- If you have the mqit-quantum-sw environment installed, you already have all the dependencies available. Please run that environment after the repo is cloned.
- If you want to run the test files, please run the test files using pytest. If that is not installed in your environment, activate the mqit-quantum-sw virtual environment in PowerShell, make sure you are in the root directory of the qaoa_maxcut and use pip to install pytest. Then, run in the same root directory, it will find the test automatically and run the test files:
- `pytest`

