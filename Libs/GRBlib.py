from math import *

#Library defines GRBs

# TODO Implement detectors and data... not today

DEFINITION_MODFACTOR = {
    25.8  : 0.4729,
    45.6  : 0.4219, #Our data
    60.0  : 0.41, #Alexey's Temp Data
    72.5  : 0.36,
    84.3  : 0.30,
    95.7  : 0.28,
    107.5 : 0.35,
} # Angle Theta : Modulation Factor for 100% Pol
DEFINITION_BGRATE = {
    25.8  : 6.4, #Alexey's Data for now
    45.6  : 6.1,
    60.0  : 5.8,
    72.5  : 5.6,
    84.3  : 5.5,
    95.7  : 5.5,
    107.5 : 5.8,
} # Angle Theta : Background Rate

F_0 = 2.18*pow(10,-3) #erg/cm^2
class GRB:
    def __init__(self, name = "" ,fluence = -1, T90 = 100, flux = 1):
        self.name = name
        #self.fluence3 = fluence3 #BATSE Fluence for Energy 100-300KeV
        #self.fluence4 = fluence4 #BATSE Fluence for Energy > 300KeV
        self.fluence  = fluence
        self.T90 = T90
        self.flux = flux
        print("I've been added...", self.name)
    def calculate_MDP(self):
        #We will use EL as Energy Level, being 3 or 4 depending if you want to calculate in the 100-300keV or >300keV energy ranges
        MDP_w = 0
        S = 0.9*self.fluence*self.flux/F_0
        for k in DEFINITION_MODFACTOR.keys():
            u100 = DEFINITION_MODFACTOR[k]
            B = self.T90*DEFINITION_BGRATE[k]
            MDP = 4.29*sqrt(S+B)/(u100*S)
            MDP_w += MDP/7
        return MDP_w
    def output_MDP(self):
        MDP = self.calculate_MDP()
        if MDP <= 100: #Cut case
            print ("GRB", self.name,"MDP", MDP)
            return MDP