from src.ROM_basis import ROM_basis
import parser # user-defined parser
import numpy as np
import matplotlib.pyplot as plt

basis = ROM_basis()

data="data/"
omegas, matrices, F = parser.parse(data)
basis.load(omegas=omegas, snapshots=matrices, F=F)

basis.next_snapshot()

targets = np.linspace(0, 40, 2000)+1.0j
_, S = basis.evaluate(targets)

plt.figure()
plt.plot(targets,S)
plt.show()
