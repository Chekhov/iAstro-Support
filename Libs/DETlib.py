

class DetectorModel:
    def __init__(self, name = ""):
        self.name = name
        self.data = {}
    def addGeoFile(self, filename):
        self.geometry = filename
    def addModel(self, modelName, data):
        #add a new model and its data to the DetectorModel
        return 0
    def grabModel(self, modelName):
        #return model data
        return 0