class Apex:
    def __init__(self, data):
        self.data = data
        self.adjacentList = []

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def getAdjacentList(self):
        return self.adjacentList

    def setAdjacentList(self, adjacentList):
        self.adjacentList = adjacentList