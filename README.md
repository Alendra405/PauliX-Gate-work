# Pauli-X Gate Demonstration in Qiskit

This repository presents a minimal yet educational implementation of the **Pauli-X gate** using Qiskit, designed as an introductory example to single-qubit quantum operations.

## Overview

The Pauli-X gate, often referred to as the quantum equivalent of the classical NOT gate, performs a bit flip on a qubit:

- |0⟩ → |1⟩
- |1⟩ → |0⟩

It is represented by the following matrix:

```
[[0, 1],
 [1, 0]]
```

In this project:
- A single qubit is initialized in the standard |0⟩ state.
- The Pauli-X gate is applied.
- The qubit is measured multiple times to demonstrate the state flip.
- Results are visualized via a histogram.

## Key Features

- Construction of a basic single-qubit quantum circuit.
- Application of the Pauli-X gate to invert the qubit state.
- Execution on the Qiskit Aer simulator.
- Histogram visualization confirming approximately 100% probability for the |1⟩ outcome.

## Requirements

- Qiskit
- qiskit-aer
- matplotlib

Installation command:
```bash
pip install qiskit qiskit-aer matplotlib
```

## Usage

Run the script:
```bash
python pauli_x_demo.py
```

Expected output: A histogram displaying near-100% probability for the |1⟩ state, confirming successful application of the Pauli-X gate.

## Educational Value

This project serves as an excellent entry point for learners exploring fundamental quantum gates and circuit execution in Qiskit. It illustrates the deterministic nature of the Pauli-X operation while introducing core concepts such as measurement and probability distribution in quantum computing.

Contributions, stars, and feedback are greatly appreciated.

#QuantumComputing #Qiskit #QuantumGates #PauliX #QuantumEducation
