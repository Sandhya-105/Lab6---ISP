# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 14:25:33 2022

@author: SANDHYA
"""

import csv
from City import City
from Point import Point
cities = []

# open the CSV file
with open("cities.csv", mode = 'r') as file:
    # read the CSV file
    csvFile = csv.reader(file)
    next(csvFile, None)

    # display the contents of the CSV file
    for line in csvFile:
        
        name, coords, area, population, pop_density, gdp, income = line
        print(name, coords, area, population, pop_density, gdp, income)
        lat_lng = coords.split()
        location = Point(lat_lng[1], lat_lng[0])
        city = City(name, location, area, population, pop_density, gdp, income)
        cities.append(city)
    print("\n")

for city in cities:
    print("name:", city.getName())
    print("coords:", city.getLocation().toString())
    print("area:", city.getArea())
    print("population:", city.getPopulation())
    print("population_density:", city.getPopulation_density())
    print("GDP:", city.getGDP())
    print("income_per_month:", city.getIncome_per_month())
    print("\n")
