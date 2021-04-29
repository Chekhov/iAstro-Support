from . import CATlib
from . import MDPlib

class DetectorModel:
    def __init__(self, name = "", ERange = [100,1000], ERes = 100):
        self.name = name
        self.data = {}
        self.Q100 = {} # User adds Energy as keys and Modulation Factor for 100% polarized beams
        self.doubleEfficiency = 0
        self.eventEfficiency = 0
        self.ERange = ERange
        self.ERes = ERes
        # TODO save model in json file
    def updateERes(self, ERes):
        self.ERes = ERes
        return 0
    def addGeoFile(self, filename):
        self.geometry = filename
    def addModel(self, modelName, data):
        #TODO add a new model and its data to the DetectorModel
        return 0
    def calculateFOM(self):
        FOM = {}
        #return cubic function FOM(Energy)
        if bool(self.Q100):
            for k in energy:
                FOM[energy] = self.doubleEfficiency*spec_Q100
            self.FOM = FOM
        return FOM
    def calculateMDP(self):
        MDP = {}
        if True: #TODO condition to calculate MDP where we have data AND no MDP has been calculated... or can be recalculated again
            self.MDP = MDP
        return MDP
    def calculateManyGRB(self, cat):
        #TODO how many GRBs per year are visible in function of detector MDP 
        return MDPlib.MDP_from_catalogue(cat) #returns an array of MDPs calculated for each GRB
    def calculateSens(self):
        SENS = {}
        if True: #TODO condition for sensitivity
            self.SENS = SENS
        return SENS
    def calculateEffArea(self, fromfile):
        nEffArea = 0
        # Calculate the Effective Area by reading a .sim file and 
        #self.EffArea[energy] = nEffArea
        f = open(tra_file)
        content = f.readlines()
        A_start = 0
        Start_Events = 0
        for line in content:
            nk = line.split()
            if line.find('SimulationStartAreaFarField') != -1 :
                A_start = float(nk[1])
                i += 1	
            elif line.find('TS') != -1 :
                # Start Events
                Start_Events = int(nk[1])
                i += 1
            else:
                continue
        
        print("Reconstruct  the  data  with Revan if you haven't already.")
        print("In  Mimrec  accept  all  events.")
        print("Take note of the total events on your terminal output.")
        End_Events = int(input("Please Insert the Total Number of Detected Events:"))
        nEffArea = A_start*End_Events/Start_Events
        print("The Calculated Effective Area from the File Was:", nEffArea)
        return nEffArea
    def grabModel(self, modelName):
        #return model data
        return 0
    def calculateMultiplicity(self, tra_file):
        f = open(tra_file)
        content = f.readlines()

        SQ = []
        i = 0

        for line in content:
            if line.find('SQ') != -1 :
                nk = line.split()
                # print(nk)
                SQ.append(int(nk[1]))
                i += 1	
            elif line.find('ET PH') != -1 :
                # print ("Hey we exist!")
                SQ.append(1)
                i += 1
            else:
                continue 

        multiplicity = [SQ.count(1), SQ.count(2), SQ.count(3), sum(i > 3 for i in SQ)]
        print("Multiplicity Parser")
        print("All:", i)
        print("SQ1:", multiplicity[0],"|", round(multiplicity[0]*100/i,5) , "%" )
        print("SQ2:", multiplicity[1],"|", round(multiplicity[1]*100/i,5), "%")
        print("SQ3:", multiplicity[2],"|", round(multiplicity[2]*100/i,5), "%")
        print("SQ+:", multiplicity[3],"|", round(multiplicity[3]*100/i,5), "%")
        self.eventEfficiency = multiplicity[0]
        self.doubleEfficiency = multiplicity[1]
        return multiplicity