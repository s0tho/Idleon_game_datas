from matplotlib import pyplot as plt
import numpy as np

class Ploting:

    def __init__(self) -> None:
        plt.figure(figsize=(10, 8))
        self.set_color()


    def set_color(self, cmap='plasma'):
        jet= plt.get_cmap(cmap)
        self.colors = iter(jet(np.linspace(0,1,10)))
    

    def subplot(self, val):
        self.set_color()
        plt.subplot(val)


    def set_conf(self, 
        x = (0, 101, 10),
        y = (0, 101, 10),
        xlab = "Talent's lvl",
        ylab = "Effect"
        ):

        plt.ticklabel_format(style='plain')

        plt.xticks(range(*x))
        plt.yticks(range(*y))

        plt.xlabel(xlab)
        plt.ylabel(ylab)

        plt.legend(loc='best')
        plt.grid(True, linewidth=0.5, linestyle='--')


    def plot(self, formula, label=""):
        plt.plot(
            formula,
            color = next(self.colors),
            label = label
        )
