from math import *
import CATlib

F_0 = 2.18*pow(10,-3) #erg/cm^2 from the BATSE Catalogue

def MDP_from_catalogue(CATALOG):
    output = []
    for k in CATALOG:
        kput = k.output_MDP()
        if kput: output.append(kput)
    return output