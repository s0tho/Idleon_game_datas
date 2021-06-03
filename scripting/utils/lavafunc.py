from inspect import getmembers, isfunction
import math

class LavaFunc:
    def __init__(self, a, b=None, lvl=1):
        self.result = 0
        self.a = a 
        self.b = b
        self.lvl = lvl


    def add(self):
        if self.b:
            self.result = (
                (
                    (self.a+self.b)/self.b + 0.5 * (self.lvl - 1)
                )
                / (self.a/self.b)
            ) * self.lvl * self.a
        else:
            self.result = self.lvl * self.a


    def decay(self):
        self.result = (self.lvl * self.a) / (self.lvl + self.b)


    def interval_add(self):
        self.result = self.a + math.floor(
            self.lvl/self.b
        )


    def big_base(self):
        self.result = self.a + self.b * self.lvl


    def decay_multi(self):
        self.result = 1 + ( self.lvl * self.a ) / (self.lvl + self.b)


    def rounding(self, r=3):
        return round(
            self.result, 
            r
        )

    def convert_to_func(self, func):
        functions = [
            "add",
            "bigBase",
            "decay",
            "decayMulti",
            "intervalAdd"
        ]
        
        attributes = [
            attribute for attribute in dir(LavaFunc) 
            if callable(getattr(LavaFunc, attribute)) 
                and attribute.startswith('__') is False 
                and attribute != "convert_to_func" 
                and attribute != "rounding"
            ]
        for index, string in enumerate(functions):
            if func == string:
                eval("self." + attributes[index] + "()")
