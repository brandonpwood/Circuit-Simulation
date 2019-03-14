'''
Brandon Wood
Cornell University College of Engineering
ECE 2100 Lab 02

Analog to digital converter simulations-- Ladder DAC circuit solver
'''
import numpy as np
import csv

def voltage_vector(n):
    voltage = []
    # Binary range is 0-31.
    for i in range(5):
        if n - 2**(4-i) >= 0:
            n -= 2**(4-i)
            voltage.insert(0, 1)
        else:
            voltage.insert(0, 0)
    return voltage
Ra = 50.0
Rb = 100.0


voltages = []
N = list(range(32))
for i in N:
    C = np.array(voltage_vector(i))
    C = C/Ra
    G = np.array([[0, 0, 0, -1/Rb, 1/Ra + 1/Rb],
    [0, 0, -1/Rb, 2/Rb + 1/Ra, -1/Rb],
    [0, -1/Rb, 2/Rb + 1/Ra, -1/Rb, 0],
    [-1/Rb, 2/Rb + 1/Ra, -1/Rb, 0, 0],
    [1/Rb + 2/Ra, -1/Ra, 0, 0, 0]
    ])
    V = np.linalg.solve(G, C)
    voltages.append(V)

# Write to .csv
with open('simulationData.csv', 'w') as f:
    writer = csv.writer(f)
    for i in voltages:
        writer.writerow(i)
