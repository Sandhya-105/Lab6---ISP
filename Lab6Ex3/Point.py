# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 11:53:04 2021

@author: SANDHYA
"""
import math
from Shape import Shape
class Point(Shape):
    def __init__(self, X, Y):
        self.__X = float(X)
        self.__Y = float(Y)
        
    def getX(self):
        return self.__X
    def getY(self):
        return self.__Y
    
    def setX(self, X):
        self.__X = X
    def setY(self, Y):
        self.__Y = Y
        
    def setPosition(self,X,Y):
        self.__X = X
        self.__Y = Y
        
    def distance(self, X, Y):
        xpt = (self.__X - X) ** 2
        ypt = (self.__Y - Y) ** 2
        dist = math.sqrt(xpt + ypt)
        return dist
    
    def toString(self):
        ptstr = "Point ("+ str(self.__X) + "," + str(self.__Y) + ")"
        return ptstr


        

        
        