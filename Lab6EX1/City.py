# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 15:56:39 2022

@author: SANDHYA
"""

class City():
    def __init__(self, name, location, area, population, population_density, GDP, income_per_month):
        self.__name = name
        self.__location = location
        self.__area = area
        self.__population = population
        self.__population_density = population_density
        self.__GDP = GDP
        self.__income_per_month = income_per_month
        
    def getName(self):
        return self.__name 
    
    def getLocation(self):
        return self.__location
    
    def getArea(self):
        return self.__area    

    def getPopulation(self):
        return self.__population
    
    def getPopulation_density(self):
        return self.__population_density
    
    def getGDP(self):
        return self.__GDP
    
    def getIncome_per_month(self):
        return self.__income_per_month
 
    def setName(self, name):
        self.__name = name
        
    def setLocation(self, location):
        self.__location = location
    
    def setArea(self, area):
        self.__area = area
    
    def setPopulation(self, population):
        self.__population = population
    
    def setPopulation_density(self, population_density):
        self.__population_density = population_density
    
    def setGDP(self, GDP):
        self.__GDP = GDP
    
    def setIncome_per_month(self, income_per_month):
        self.__income_per_month = income_per_month
    

    
    
        