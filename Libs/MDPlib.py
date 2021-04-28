from math import *
import CATlib

F_0 = 2.18*pow(10,-3) #erg/cm^2 from the BATSE Catalogue

class GRB:
    def __init__(self, name = "" ,fluence = -1, T90 = 100, flux = 1):
        self.name = name
        #self.fluence3 = fluence3 #BATSE Fluence for Energy 100-300KeV
        #self.fluence4 = fluence4 #BATSE Fluence for Energy > 300KeV
        self.fluence  = fluence
        self.T90 = T90
        self.flux = flux
        print("I've been added...", self.name)
    def calculate_MDP(self, detector):
        #We will use EL as Energy Level, being 3 or 4 depending if you want to calculate in the 100-300keV or >300keV energy ranges
        MDP_w = 0
        S = 0.9*self.fluence*self.flux/F_0
        for k in detector.DEFINITION_MODFACTOR.keys():
            u100 = detector.DEFINITION_MODFACTOR[k]
            B = self.T90*detector.DEFINITION_BGRATE[k]
            MDP = 4.29*sqrt(S+B)/(u100*S)
            MDP_w += MDP/7
        return MDP_w
    def output_MDP(self, detector):
        MDP = self.calculate_MDP(detector)
        if MDP <= 100: #Cut case
            print ("GRB", self.name,"MDP", MDP)

def MDP_from_catalogue(CATALOG):
    for k in CATALOG:
        k.output_MDP()