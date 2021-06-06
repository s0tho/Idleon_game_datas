from matplotlib import pyplot as plt
import numpy as np
import math



xp_dic = {
    "class" :       (15, 1.9, 11, 1.208, 0.164, 0.215, 100, 15),
    "skill" :       (15, 2.0, 15, 1.225, 0.164, 0.135,  50, 30),
    "alchemy" :     (15, 2.0, 15, 1.225, 0.18, 0.135,  50, 30),
    "smithing" :    (15, 2.0, 13, 1.225, 0.164, 0.135,  50, 30),
    "construction": (10, 2.81, 4, 1.117, math.inf, 0.135,  5, 6),
    "worship" :     (15, 1.3, 6, 1.17, 0.07, 0.135,  50, 26),
}


def xp_formula(x, choice):
    try:
        values = xp_dic[choice] 
    except Exception as e:
        print(f"Error {e}, {choice} not supported")
        pass

    if x == 1:
        return 15

    f1 = values[0] + pow(x, values[1]) + values[2] * x

    f2 = pow(values[3] - min(values[4], (values[5]*x) / (x+values[6]) ),x)

    if choice == "construction":
        eq = math.ceil(f1 * f2 - values[7])
    else:
        eq = math.floor(f1 * f2 - values[7])

    return eq

def plot_xp(choice, label, size=(0, 101, 10), log=True):
    xpoints = []
    ypoints = []
    for x in range(1,size[1]):
        res = xp_formula(x, choice)
        xpoints.append(x)
        ypoints.append(res)

    plt.xticks(range(*size))

    plt.plot(xpoints,ypoints, label=label)
    plt.legend(loc='best')
    plt.xlabel("LVL")
    plt.ylabel("XP")
    if log:
        plt.semilogy()
    plt.grid(True, linewidth=0.5, linestyle='--')
    
plt.subplot(211)
plot_xp("class", "class", (0, 501, 25))
count=0
plt.subplot(212)
for i in xp_dic:
    if count != 0:
        plot_xp(i, label=i, log=True, size = (0, 51, 5))
    count += 1

plt.show()


# for i in range(15):
#     print(
#         f"LVL {i+1}: ",
#         xp_formula(
#             i+1,
#             "construction"
#         )
#     )

# print(
#     xp_formula(43, "alchemy")
# )