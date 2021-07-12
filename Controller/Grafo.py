from Model.Apex import Apex
from Model.Edge import Edge
from collections import deque
from copy import copy


class Graph:

    def __init__(self):
        self.apexList = []
        self.edgeList = []
        self.visitedList = []
        self.blockedList = []

    def getApexList(self):
        return self.apexList

    def getEdgeList(self):
        return self.edgeList

    def getVisitedList(self):
        return self.visitedList

    def joinApex(self, date):
        if self.checkApex(date) is None:
            self.apexList.append(Apex(date))

    def checkApex(self, date):
        for apex in self.apexList:
            if date == apex.getDate():
                return apex
        return None

    def joinEdge(self, origin, destination, weight):
        if self.checkEdge(origin, destination) is None:
            if self.checkApex(origin) is not None and self.checkApex(destination) is not None:
                self.edgeList.append(Edge(origin, destination, weight))
                self.checkApex(origin).getAdjacentList().append(destination)

    def checkEdge(self, origin, destination):
        for edge in self.edgeList:
            if edge.getOrigin() == origin and edge.getDestination() == destination:
                return edge
        return None

    def profundity(self, position, visitedList):
        if self.checkEdge(position):
            if not visitedList:
                visitedList.append(position)
            for adjacent in self.checkEdge(position).getAdjacentList():
                if not adjacent not in visitedList:
                    visitedList.append(adjacent)
                    visitedList = self.profundity(adjacent, visitedList)
            return visitedList
        else:
            print('The apex marked to start the route doesnt exist')

    def amplitude(self, data):
        visitedA = []
        tail = deque()
        apex = self.checkApex(data)

        if apex is not None:
            tail.append(apex)
            visitedA.append(data)

            while (tail):
                element = tail.popleft()
                for adjacent in element.getAdjacentList():
                    if adjacent not in visitedA:
                        apex = self.checkApex(adjacent)
                        tail.append(apex)
                        visitedA.append(adjacent)

            return visitedA

    def printApex(self):
        for apex in self.apexList:
            print(apex.getData())

    def printEdge(self):
        for edge in self.edgeList:
            print('Origin: {0}, Destination: {1}, Weight: {2}'.format(edge.getOrigin(), edge.getDestination(),
                                                                      edge.getWeight()))

    def printAdjacentList(self):
        for apex in self.apexList:
            print('Adjacent List of ', apex.getData(), ':', apex.getAdjacentList())

    def getWell(self):
        nWell = 0
        for apex in self.apexList:
            if len(apex.getAdjacentList()) == 0:
                print('The apex: ', apex.getData(), 'is a well')
                nWell += 1
        print('The wells number of graph is: ', nWell)

        return nWell

    def getSource(self):
        nSource = 0
        door = False

        for apex in self.apexList:
            for edge in self.edgeList:
                if edge.getDestination() == apex.getData():
                    door = True
                if door != True:
                    break

            if door == False:
                print('The apex: ', apex.getData(), 'is the source')
                nSource += 1
        print('The sources number of graph is: ', nSource)

        return nSource

    def connectedStrong(self):
        nWells = self.getWell()
        nSource = self.getSource()

        if nSource > 0 and nWells > 0:
            print('The graph is weakly connected')
            return True

        return False

    def order(self, copyEdge):
        for i in range(len(copyEdge)):
            for j in range(len(copyEdge)):
                if copyEdge[i].getWeight() < copyEdge[j].getWeight():
                    temp = copyEdge[i]
                    copyEdge[i] = copyEdge[j]
                    copyEdge[j] = temp

    def Kruscal(self):
        copyEdge = copy(self.getEdgeList())
        kruscalEdge = []
        ensembleList = []

        self.order(copyEdge)
        for minor in copyEdge:
            self.ensembleOperationsKruscal(minor, ensembleList, kruscalEdge)
        print('-------------Kruscal-------------')
        for data in kruscalEdge:
            print('Origin: {0}, Destination: {1}, Weight: {3}'.format(data.getOrigin(), data.getDestiantion(),
                                                                      data.getWeight()))

        return kruscalEdge

    def ensembleOperationsKruscal(self, minor, ensembleList, kruscalList):

        located1 = -1
        located2 = -1

        if not ensembleList:
            ensembleList.append({minor.getOrigin(), minor.getDestination()})
            kruscalList.append(minor)

        else:
            for i in range(len(ensembleList)):
                if (minor.getOrigin() in ensembleList) and (minor.getDestination() in ensembleList):
                    return

            for i in range(len(ensembleList)):
                if minor.getOrigin() in ensembleList[i]:
                    located1 = i
                if minor.getDestination() in ensembleList:
                    located2 = i

            if located1 != -1 and located2 != -1:
                if located1 != located2:
                    ensembleList[located1].update(ensembleList[located2])
                    ensembleList[located2].clear()
                    kruscalList.append(minor)

            if located1 != -1 and located2 == -1:
                ensembleList[located1].add(minor.getOrigin())
                ensembleList[located1].add(minor.getDestination())
                kruscalList.append(minor)

            if located1 == -1 and located2 != -1:
                ensembleList[located2].add(minor.getOrigin())
                ensembleList[located2].add(minor.getDestination())
                kruscalList.append(minor)

            if located1 == -1 and located2 == -1:
                ensembleList.append({minor.getOrigin(), minor.getDestination()})
                kruscalList.append(minor)

    def Boruvka(self):

        copyApex = copy(self.getApexList())
        copyEdge = copy(self.getEdgeList())

        boruvkaEdges = []
        ensembleList = []
        door = True
        quantity = 0

        while (quantity > 1 or door):
            for apex in copyApex:
                self.ensembleOperationsBoruvka(apex, ensembleList, boruvkaEdges, copyEdge)
                door = False
                quantity = self.ensemblesQuantities(ensembleList)

        for data in boruvkaEdges:
            print('Origin: {0}, Destination: {1}, Weight: {2}'.format(data.getOrigin(), data.getDestiantion(),
                                                                      data.getWeight()))

        return boruvkaEdges

    def ensembleOperationsBoruvka(self, apex, ensembleList, boruvkaEdge, copyEdge):

        located1 = -1
        located2 = -1
        minor = self.searchMinor(apex, copyEdge)

        if not minor == None:
            if not ensembleList:
                ensembleList.append({minor.getOrigin(), minor.getDestination()})
                boruvkaEdge.append(minor)
        else:
            for i in range(len(ensembleList)):
                if (minor.getOrigin() in ensembleList) and (minor.getDestination() in ensembleList):
                    return False

            for i in range(len(ensembleList)):
                if minor.getOrigin() in ensembleList[i]:
                    located1 = i
                if minor.getDestination() in ensembleList:
                    located2 = i

            if located1 != -1 and located2 != -1:
                if located1 != located2:
                    ensembleList[located1].update(ensembleList[located2])
                    ensembleList[located2].clear()
                    boruvkaEdge.append(minor)

            if located1 != -1 and located2 == -1:
                ensembleList[located1].update(minor.getOrigin())
                ensembleList[located1].update(minor.getDestination())
                boruvkaEdge.append(minor)

            if located1 == -1 and located2 != -1:
                ensembleList[located2].update(minor.getOrigin())
                ensembleList[located2].update(minor.getDestination())
                boruvkaEdge.append(minor)

            if located1 == -1 and located2 == -1:
                ensembleList.append({minor.getOrigin(), minor.getDestination()})
                boruvkaEdge.append(minor)

    def ensemblesQuantities(self, ensembleList):

        quantity = 0

        for ensemble in ensembleList:

            if len(ensemble) > 0:
                quantity += 1

        return quantity

    def searchMinor(self, apex, copyEdge):
        temp = []

        for adjancent in apex.getAdjacentList():
            for edge in copyEdge:
                if edge.getOrigin() == apex.getData() and edge.getDestination() == adjancent:
                    temp.append(edge)

        if temp:
            self.order(temp)
            apex.getAdjacentList().remove(temp[0].getDestination())
            return temp[0]

        return None

    def prim(self):
        copyEdge = copy(self.getEdgeList())
        ensemble = []
        primEdge = []
        tempEdge = []
        self.order(copyEdge)
        self.directed(copyEdge)
        minor = copyEdge[0]
        ensemble.append(minor.getOrigin())
        finish = False

        while finish == False:
            for apex in ensemble:
                self.algorithmPrim(copyEdge, ensemble, primEdge, tempEdge, apex)
            if len(self.apexList) == len(ensemble):
                finish = True

        print(ensemble)
        for edge in primEdge:
            print('Origin: {0}, Destination: {1} - Weight: {2}'.format(edge.getOrigin(), edge.getDestination(),
                                                                       edge.getWeight()))

        return primEdge

    def algorithmPrim(self, copyEdge, ensemble, primEdge, tempEdge, apex):
        cycle = False
        self.joinTemp(copyEdge, tempEdge, apex)
        candidate = self.candidatePrim(tempEdge, copyEdge, primEdge)

        if candidate != None:
            if candidate.getOrigin() in ensemble and candidate.getDestination() in ensemble:
                cycle = True
            if cycle == False:
                primEdge.append(candidate)
                if not candidate.getOrigin() in ensemble:
                    ensemble.append(candidate.getOrigin())
                if not candidate.getDestination() in ensemble:
                    ensemble.append(candidate.getDestination())

    def joinTemp(self, copyEdge, tempEdge, apex):
        for edge in copyEdge:
            if edge.getOrigin() == apex or edge.getDestination() == apex:
                if self.checkApexTemp(apex, tempEdge):
                    tempEdge.append(edge)

    def checkApexTemp(self, edge, tempEdge):
        for element in tempEdge:
            if element.getOrigin() == edge.getOrigin() and element.getDestination() == edge.getDestination():
                return False
        return True

    def checkPrim(self, candidate, primEdge):
        for edge in primEdge:
            if edge.getOrigin() == candidate.getOrigin() and edge.getDestination() == candidate.getDestination():
                return False
            if edge.getOrigin() == candidate.getDestination() and edge.getDestination() == candidate.getOrigin():
                return False
        return True

    def candidatePrim(self, tempEdge, copyEdge, primEdge):
        minor = copyEdge[len(copyEdge) - 1]
        for i in range(len(tempEdge)):
            if tempEdge[i].getWeight() < minor.getWeight():
                if self.checkApexTemp(tempEdge[i], primEdge):
                    minor = tempEdge[i]
        tempEdge.pop(tempEdge.index(minor))

        return minor

    def directed(self, copyEdge):
        for element in copyEdge:
            for i in range(len(copyEdge)):
                if element.getOrigin() == copyEdge[i].getDestination() and element.getDestination() == copyEdge[
                    i].getOrigin():
                    copyEdge.pop(i)
                    break

    def notDirected(self, copyEdge):
        directed = False
        for element in copyEdge:
            for i in range(len(copyEdge)):
                if element.getOrigin() == copyEdge[i].getDestination() and element.getDestination() == copyEdge[
                    i].getOrigin():
                    directed = True
            if directed == False:
                copyEdge.append(Edge(element.getDestination(), element.getOrigin(), element.getWeight()))

    def dijkstra(self, origin, apexAux):

        marcs = [] #la lista de los que ya se visitaron
        roads=[]#la lista final
        # se inicia con valores de infinito
        for v in self.apexList:
            roads.append(float("inf"))
            marcs.append(False)
            apexAux.append(None)
            if v.getData() is origin:
                roads[self.apexList.index(v)]=0
                apexAux[self.apexList.index(v)]=v.getData()
        while not self.allMarcs(marcs):
            aux=self.notMarcMinor(roads,marcs)# obtenemos el menor no marcado
            if aux is None:
                break
            index=self.apexList.index(aux)#indice del menor
            marcs[index]=True#marca como visitado
            currentValue=roads[index]
            for vAdja in aux.getAdjacentList():
                newIndex=self.apexList.index(self.checkApex(vadja))
                edge=self.checkEdge(vAdja,aux.getData())
                if roads[newIndex]>currentValue+edge.getWeihgt():
                    roads[newIndex] = currentValue + edge.getWeihgt()
                    apexAux[newIndex]=self.apexList[index].getData
        return roads

    def notMarcMinor(self,roads,marcs):
        minorApex=None
        auxRoads=sorted(roads)
        copyRoads=copy(roads)
        flag=True
        counter=0
        while flag:
            minor=auxRoads[counter]
            if marcs[copyRoads.index(menor)]==False:
                minorApex=self.apexList[copyRoads.index(minor)]
                flag=False
            else:
                copyRoads[copyRoads.index(minor)]="x"
                counter=counter+1
            return minorApex
    def allMarc(self,marcs):
        for j in marcs:
            if j is False:
                return False
        return True
    def chargeInicialRed(self,rute):
        with open(rute) as contents:
            acmeNetwork=json.load(contens)
        for apex in acmeNetwork["cuevas"]:
            self.ingressApex(apex)
        for edge in acmeNetwork["caminos"]:
            self.ingressEdge(edge[0],edge[1],edge[2])
        self.notDirected(self.edgeList)

#//parte de anexos extras//
    def changeDirection(self,origin,destinatation):
        for edge in self.edgeList:
            copyOrigin=str(edge.getOrigin())
            copyDestinatation=str(edge.getDestinatation())
            if origin==copyOrigin and destinatation==copyDestinatation:
                temp=edge.getOrigin()
                edge.setOrigin(edge.getDestinatation())
                edge.setDestinatation(temp)

    def blockEdge(self,origin,destinatation):
        for edge in self.edgeList:
            copyOrigin = str(edge.getOrigin())
            copyDestinatation = str(edge.getDestinatation())
            if origin == copyOrigin and destinatation == copyDestinatation:
                self.blockedList.append(edge)
                index = self.edgeList.index(edge)
                self.blockedList.pop(index)

    def unblockEdge(self,origin,destinatation):
        for edge in self.blockedList:
            copyOrigin = str(edge.getOrigin())
            copyDestinatation = str(edge.getDestinatation())
            if origin == copyOrigin and destinatation == copyDestinatation:
                self.edgeList.append(edge)
                index = self.blockedList.index(edge)
                self.blockedList.pop(index)

    def gradeApex(self,apex):
        gradeApex=0
        enterApex=self.checkApex(apex)
        copyEdges=copy(self.edgeList)
        for apex in self.edgeList:
            if apex==enterApex:
                gradeApex=len(apex.getAdjacentList())
        self.edgeList=copyEdges
        return gradeApex







