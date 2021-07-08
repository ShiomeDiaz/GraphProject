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
            if dato== vertice.getData():
                return vertice
        return m
