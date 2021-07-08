class Arista:
    def __init__(self, source, destinatation, weight):
        self.source = source
        self.destinatation = destinatation
        self.weight = weight

    def getSource(self):
        return self.source

    def setSource(self, source):
        self.source = source

    def getDestinatation(self):
        return self.destinatation

    def setDestinatation(self, destinatation):
        self.destinatation = destinatation

    def getWeight(self):
        return self.weight

    def setWeight(self, weight):
        self.weight = weight