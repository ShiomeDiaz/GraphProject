import pygame
from Model.Arista import Arista
from Model.Vertice import Vertice
from collections import deque
from copy import copy
import json

class Grafo:
    def __init__(self):
        self.verticesList=[]
        self.edgesList=[]
        self.visitedList=[]
        self.blockList=[]
    def getVerticesList(self):
        return self.verticesList
    def getEdgesList(self):
        return self.edgesList
    def getVisitedList (self):
        return self.visitedList
    def VerticeIngress (self, data):
        if self.checkVertice(data) is None:
            self.verticesList.append(vertice(data))
    def checkVertice(self,data):
        for vertice in self.verticesList:
            if data== vertice.getData():
                return vertice
        return None
    def enterEdge(self,source,destinatation,weight):
        if self.checkEdge(source,destinatation) is None:
            if self.checkVertice(source) is not None and self.checkVertice(destinatation) is not None:
                self.edgesList.append(edge(source,destinatation,weight))
                self.checkVertice(source).getAdjacentList().append(destinatation)
    def checkEdge(self,source,destinatation):
        for edge in self.edgesList:
            if edge.getSource()==source and edge.getDestinatation()== destinatation:
                return edge
        return None
    def deph (self,position,guest_list ):
        if self.checkVertice(position):
            if not guest_list:
                guest_list.append(position)
            for adjacent in self.checkVertice(position).getAdjacentList():
                if adyacente not in guest_list:
                    guest_list.append(adjacent)
                    guest_list=self.deph(adjacent,guest_list)
            return guest_list
        else:
            return"""El
        vertice
        señalado
        para
        iniciar
        el
        recorrido
        no
        existe"""


        """"def profundidad(self, dato):
            if dato in self.listaVisitados:
                return
            else:
                vertice = self.verificarVertice(dato)
                if vertice is not None:
                    self.listaVisitados.append(vertice.getDato())
                    for dato in vertice.getListaAdyacentes():
                        self.profundidad(dato)
        """
    def amplitude(self,data):
        visitedA=[]
        tail=aboutWhat()
        vertice=self.checkVertice(data)
        if vertice is not None:
            tail.append(vertice)
            visitedA.append(data)
        while cola:
            element=tail.popleft()
            for adjacent in element.getAdjacent():
                if adjacent not in visitedA
                    vertice=self.checkVertice(adjacent)
                    tail.append(vertice)
                    visitedA.append(adjacent)
        return visitedA
    def impressVerice(self):
        for vertice in self.verticesList:
            print(vertice.getData())
    def impressEdge(self):
        for edge in self.edgesList:
            print ('Origen: {0} -- Destino: {1} -- Peso: {2}'.format(arista.getSource(),arista.getDestinatation(),arista.getWeight()))
    def impressAdjacentList(self):
        for vertice in self.edgesList:
            print ('Lista de adyacentes de ', vertice.getData(), ': ', vertice.getAdjacentList())
    def separator(self):
        print()
        print('-------------------------------------')
        print()
    def getWells(self):
        numberWells=0
        for vertice in self.verticesList:
            if len(vertice.getAdjacentList())==0:
                print('el vertice: ',vertice.getData(),'es un pozo')
                numberWells+=1
            print ('la cantidad de pozos del grafo es:',numberWells)
            return numberWells
    def getSources(self):
        numberSources=0
        flag=False
        for vertice in self.verticesList:
            for edge in self.edgesList:
                if edge.getDestinatation()==vertice.getData():
                    flag=True
                if flag!=False:
                    break
            if bandera==False:
                print('el vertice: ', vertice.getData(),'es una fuente')
                numberSources+=1
        print('la cantidad de fuentes en el grafo es: ',numberSources)
        return numberSources
    def strongConnected(self):
        numberWells=self.getWells()
        numberSources=self.getSources()
        if numberWells>0 and numberSources>0:
            print ('el grafo es debilmente conexo')
            return True




