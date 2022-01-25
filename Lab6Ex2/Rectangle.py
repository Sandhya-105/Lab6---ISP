# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 13:35:54 2021

@author: SANDHYA
"""
from Point import Point
from Shape import Shape
class Rectangle(Shape):
    def __init__(self, topleftpoint, width, height):
        self.__width = width
        self.__height = height
        self.__topleftpoint = topleftpoint
        
    def gettopleftpoint(self):
        return self.__topleftpoint
    
    def calcbottomleftpoint(self):
        x =self.__topleftpoint.getX()
        y = self.__topleftpoint.getY() - self.__height
        bbpoint = Point(x,y)
        return bbpoint
    
    def getwidth(self):
        return self.__width
    
    def getheight(self):
        return self.__height
    
    def settopleftpoint(self,topleftpoint):
        self.__topleftpoint = topleftpoint
        
    def setwidth(self, width):
        self.__width = width
        
    def setheight(self,height):
        self.__height = height
        
    def area(self):
        area = self.__width * self.__height
        return float(area)
    
    def perimeter(self):
        perimeter = 2*(self.__width + self.__height)
        return float(perimeter)
    
    def contains(self, point):
        if(point.getX() > self.__topleftpoint.getX() and point.getX() < self.__topleftpoint.getX() + self.__width and point.getY() > self.__topleftpoint.getY() and point.getY() < self.__topleftpoint.getY()+ self.__height):
           return True
        else:
           return False
    
    def centroid(self):
        w = self.__width/2
        h = self.__height/2
        x = self.__topleftpoint.getX() + w
        y = self.__topleftpoint.getY() + h
        return Point(x,y)
    
    def toString(self):
       rectstr = "topleftpoint = " + self.__topleftpoint.toString() + " width = " + str(self.__width) + " height = " + str(self.__height)
       return rectstr
        