from utils.lavafunc import LavaFunc
from utils.plot import Ploting
from matplotlib import pyplot as plt
import re
import numpy as np


"""
Requirement lvl for     
T1 CLASS - 9
T2 CLASS - 29
T3 CLASS - 69   
T4 CLASS - 192
"""

def parse_bonuses():
    count = True
    bonuses = []
    characters = []
    with open("scripting/family.txt") as f:
        for line in f:
            
            if not count:
                if re.search('"(.*)"', line):
                    bonus = re.search('"(.*)"', line).group(1).split('"')[0]
                    bonus = bonus.split(" ")
                    bonuses.append(bonus)
            
            if count:
                result = re.search('"(.*)"', line)
                characters = result.group(1).split(" ")
                count = False

    try:
        for item in range(len(characters)):
            bonus_name = bonuses[item][0]
            if bonus_name != "NO_FAMILY_BONUS" and bonus_name != characters[item] and bonus_name != "FILLER" :
                bonus_name = bonus_name     \
                    .replace("{", " ")      \
                    .replace("_", " ")      \
                    .replace("#@", "x ")    \
                    .replace("|", " ")
                    
                a = float(bonuses[item][1])
                b = float(bonuses[item][2])
                func = bonuses[item][3]
                
                yield characters[item], bonus_name, a, b, func
    except IndexError:
        pass

plot = Ploting()

bonuses_per_character = parse_bonuses() 
count = 0

for i in bonuses_per_character:
    character , bonus_name, a, b, func = i 

    # T1 CLASS OFFSET
    offset = 9
    dashes=(2, 1)

    # T2 CLASS OFFSET
    if (count+2) % 3:
        offset = 20 + offset
        dashes=()
        
    count += 1

    xpoints = []
    ypoints = []
    for x in range(offset,200):
        res = LavaFunc(a, b, x-offset)
        res.convert_to_func(func)
        xpoints.append(x)
        ypoints.append(res.result)

    plt.plot(xpoints,ypoints, label=f"({character}) : {bonus_name}", dashes=dashes)

plot.set_conf(
    x = (0,201,5),
    y = (0,50,2)
)

plt.show()

