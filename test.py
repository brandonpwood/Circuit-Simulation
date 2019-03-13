'''
Brandon Wood
Cornell University College of Engineering
ECE 2100 Lab 02

Analog to digital converter simulations-- test circuit for solver methods
'''
import numpy as np

R0 = 100.0
R1 = 100.0
R2 = 200.0
Ra = 50.0
Vin = 1.0
C = np.array([Vin/R2 , 0])
G = np.array([[(1/Ra + 1/R0 + 1/R2), -1/Ra], [-1/Ra, (1/R1+1/Ra)]])
print(G)
print(C)
V = np.linalg.solve(G, C)

print(V)
