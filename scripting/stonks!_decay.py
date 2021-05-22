from matplotlib import pyplot as plt
import numpy as np

def find_value(round=False):
    val = [0,0]

    for x in range(120):
        eq = 130*x/(x+50)
        gain = eq-x
        if round:
            gain = int(gain)
        if gain > val[0]:
            val[0] = gain
            val[1] = x

    return val

z = np.linspace(0,100,100)

plt.plot(130*z/(z+50))

y,x = find_value()
y = round(y,2)
plt.plot([x, x], [0, 100],color='green',label=f"If game don't round down, stop : {x} - gain : {y}")
y,x = find_value(True)
plt.plot([x, x], [0, 100],color='red',label=f"If game round down, stop : {x} - gain : {y}") 


plt.xlabel("Talent's Level")
plt.ylabel("Points given")
plt.title("Where to stop leveling up Stonks!")
plt.legend(loc='best')
# log y
# plt.semilogy()
plt.grid(True, linewidth=0.5, linestyle='--')
plt.show()