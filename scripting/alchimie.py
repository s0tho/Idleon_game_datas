from matplotlib import pyplot as plt
import numpy as np

DECANT = 0.02
VIAL = 0.01
STAMP = 0.01
BLEACH = 1.5
NOT_BLEACH = 1 
LIQUIDS = ["Water", "Nitrogen"]

def get_p2w(p2w_lvl):
    if not isinstance(p2w_lvl, np.ndarray):
        if p2w_lvl > 100:
            p2w_lvl = 100
    return (400 * (p2w_lvl/(100+p2w_lvl)))/100

def get_decant(decant_lvl):
    return DECANT*decant_lvl

def get_vial(vial_lvl):
    if vial_lvl > 10:
        print("\nVial LVL can't be higher than 10, it will be considered lvl 10.")
        vial_lvl = 10
    return VIAL*vial_lvl

def get_stamp(stamp_lvl):
    return STAMP*stamp_lvl

def get_charlvl(chars_lvl):
    if chars_lvl:
        result = 0
        for lvl in chars_lvl:
            result += pow(lvl * 2 + 4,0.65)/100
        return result
    return 0


def isBleach(value):
    if value:
        return BLEACH
    return NOT_BLEACH

def calc_liquidh(    
        p2w_lvl = 0,
        decant_lvl = 0,
        vial_lvl = 0,
        stamp_lvl = 0,
        chars_lvl = [0,0,0],
        bleach=False
    ):

    waterh_f1 = 1 + get_decant(decant_lvl) + get_p2w(p2w_lvl) + get_vial(vial_lvl)
    waterh_f2 = 1 + get_stamp(stamp_lvl) + get_charlvl(chars_lvl)
    bleach = isBleach(bleach)

    waterh = bleach * waterh_f1 * waterh_f2

    return round(waterh,4)

def compare_sources(data,char_lvl,bleach,enum=[1]):
    for i, level in enumerate(enum):
        result = {}
        for i in range(len(LIQUIDS)):
            initial = calc_liquidh(
                    p2w_lvl = data["p2w"][i],
                    decant_lvl = data["decant"][i],
                    vial_lvl = data["vial"],
                    stamp_lvl = data["stamp"],
                    chars_lvl = char_lvl[i],
                    bleach=bleach[i]
                )
            for type in data:
                if isinstance(data[type], list):
                    data[type][i] += level
                else:
                    data[type] += level

                liquidh = calc_liquidh(
                    p2w_lvl = data["p2w"][i],
                    decant_lvl = data["decant"][i],
                    vial_lvl = data["vial"],
                    stamp_lvl = data["stamp"],
                    chars_lvl = char_lvl[i],
                    bleach=bleach[i]
                )

                if isinstance(data[type], list):
                    data[type][i] -= level
                else:
                    data[type] -= level

                result[type] = liquidh

            res = {key: val for key, val in sorted(result.items(), key = lambda ele: ele[1], reverse = True)}

            print("====== " + LIQUIDS[i].upper() + " ======")
            print()
            print('{:>15} {:>8.4f} /h'.format("INITIAL:", initial))
            print()
            for i in res:
                print('{:>15} {:>8.4f} /h {:>7}%'.format(
                    i.upper() + f" +{level} lvl:", 
                    res[i], 
                    "+" + str(round(((res[i]/initial)*100)-100,2))))
            print()

def compare_p2w(p2w_lvl_a, p2w_lvl_b):
    return round(
        (get_p2w(p2w_lvl_b) - get_p2w(p2w_lvl_a))*100
        ,4)

def plot_p2w():
    z = np.linspace(0,100,100)

    plt.subplot(1, 2, 1)
    plt.plot( get_p2w(z)*100 )
    # plt.semilogy()
    plt.xlabel("p2w level")
    plt.ylabel("Regen %")
    plt.grid(True, linewidth=0.5, linestyle='--')

    plt.subplot(1, 2, 2)
    plt.plot( get_p2w(z)*100 - get_p2w(z-1)*100 )
    plt.xlabel("p2w level")
    plt.ylabel("Regen % Gain by lvl")
    plt.grid(True, linewidth=0.5, linestyle='--')

    plt.show()

# ACCOUNT WIDE
vial_lvl = 5
stamp_lvl = 29
#LIQUIDS
char_lvl = [
    [39,35,37],
    []
]
water_p2w = 61
nitrogen_p2w = 25
water_decant = 7
nitrogen_decant = 11
bleach = [True, True]


data = {
    "p2w": [water_p2w, nitrogen_p2w],
    "decant" : [water_decant, nitrogen_decant],
    "vial" : vial_lvl,
    "stamp" : stamp_lvl,
}

enum=[20]

compare_sources(data, char_lvl, bleach, enum)

# print(
#     "Gain: " 
#     + str(compare_p2w(80, 100))
#     + "%"
# )

# plot_p2w()
