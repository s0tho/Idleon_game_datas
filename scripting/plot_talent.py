from utils.lavafunc import LavaFunc
from utils.plot import Ploting
from matplotlib import pyplot as plt
import numpy as np
import math


def set_formula(a, b, lvl, func):
    result = LavaFunc(a, b, lvl)
    result.convert_to_func(func)
    return result.result


def create_plot(values, mult, y, label=None, set=[10, 100, 1000]):
    lab = None
    for i,j in enumerate(set):
        if label:
            lab = f"{label} = {j}"

        plot.plot(
            eval(mult) * values,
            label=lab
        )

        plot.set_conf(
            x = (0, 201, 15),
            y = y
        )


z = np.linspace(1,200,200)
plot = Ploting()

# Meatshank formula
values = set_formula(12, 100, z, "decay")

values_per_lvl = []
values_per_lvl.append(values[0])
for i in range(len(values)-1):
    values_per_lvl.append(
        values[i+1] - values[i]
    )
values_per_lvl = np.array(values_per_lvl)

mult = "j"
label = "nb vial"
set = [1, 5, 10,20,30,40,60]

plot.subplot(211)
create_plot(
    values,
    mult,
    (0, 501, 50),
    label,
    set
)

plot.subplot(212)
create_plot(
    values_per_lvl,
    mult,
    (0, 10, 1),
    label,
    set
)

plt.show()