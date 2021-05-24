from matplotlib import pyplot as plt
import numpy as np

xpoints = []
ypoints = []

def xp_formula(x):
    if x == 1:
        return 15

    f1 = 15 + pow(x, 1.9) + 11 * x
    f2 = pow(1.208 - min(0.164, (0.215*x) / (x+100) ),x)

    eq = round(f1 * f2 - 30)
    return eq


for x in range(1,500):
    res = xp_formula(x)
    xpoints.append(x)
    ypoints.append(res)


plt.plot(xpoints,ypoints)
plt.semilogy()
plt.grid(True, linewidth=0.5, linestyle='--')
plt.show()

for i in range(0, 30):
    print("LVL: ", i+1,"\t XP: ", ypoints[i])
