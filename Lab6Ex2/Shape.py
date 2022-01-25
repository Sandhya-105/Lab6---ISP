# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 15:35:24 2021

@author: SANDHYA
"""

class Shape:
    def __init__(self, strokeWidth, strokeColor, fillColor):
        self.__strokeWidth = strokeWidth
        self.__strokeColor = strokeColor
        self.__fillColor = fillColor
    
    def getstrokeWidth(self):
        return self.__strokeWidth
    
    def getstrokeColor(self):
        return self.__strokeColor
    
    def getfillColor(self):
        return self.__fillColor
    
    def setstrokeWidth(self, strokeWidth):
        self.__strokeWidth = strokeWidth
        
    def setstrokeColor(self, strokeColor):
        self.__strokeColor = strokeColor
        
    def setfillColor(self, fillColor):
        self.__fillColor = fillColor
    
    