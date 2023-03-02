#Three lines to make our compiler able to draw:
import sys
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0.019, 0.036, 0.071, 0.102, 0.115])
ypoints = np.array([196.14, 294.21, 392.28, 490.35, 588.42])

plt.plot(xpoints, ypoints, marker = "o", ls = ":")

plt.title("Período em função da deformação")
plt.xlabel("Deformação")
plt.ylabel("Força")

plt.grid()
plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig("Gráfico 1", format="png")