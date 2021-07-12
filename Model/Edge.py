class Edge:
    def __init__(self,origin, destinatation, weight):
        self.origin = origin
        self.destinatation = destinatation
        self.weight = weight

    def getOrigin(self):
        return self.origin

    def setOrigin(self, origin):
        self.origin = origin

    def getDestinatation(self):
        return self.destinatation

    def setDestinatation(self, destinatation):
        self.destinatation = destinatation

    def getWeight(self):
        return self.weight

    def setWeight(self, weight):
        self.weight = weight