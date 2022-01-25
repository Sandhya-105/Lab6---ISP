# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 11:21:03 2021

@author: SANDHYA
"""

from Shape import Shape
class Polyline(Shape):
    def __init__(self, points):
        self.__points = points
        self.__numPoints = len(points)
    
    def get_points(self):
        return self.__points
    
    def get_numPoints(self):
        return self.__numPoints

    def set_points(self, points):
        self.__points = points
    
    def set_numPoints(self):
        self.__numPoints = len(self.__points)
    
    
    
    
    
    