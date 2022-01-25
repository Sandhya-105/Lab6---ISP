# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 14:25:33 2022

@author: SANDHYA
"""

import csv
from City import City
from Point import Point
from Rectangle import Rectangle
import matplotlib.pyplot as plt

cities = []
# ///////////////////////////////////////////////  Functions //////////////////////////////////////////////////////////
# creating minimum bounding box
def minBoundingBox(cities):
    xArray = []
    yArray = []
    for city in cities:
        xArray.append(city.getLocation().getX())
        yArray.append(city.getLocation().getY())
    topleftpt = Point(min(xArray)-50, max(yArray)+50)
    width = (max(xArray) -min(xArray)) + 100
    height = (max(yArray) - min(yArray)) + 100
    bbox = Rectangle(topleftpt, width, height)
    return bbox

# creating the plotting surface
fig, ax = plt.subplots()
ax.set_aspect("equal")

# open the CSV file
with open("cities.csv", mode = 'r') as file:
    # read the CSV file
    csvFile = csv.reader(file)
    next(csvFile, None)
    # display the contents of the CSV file
    for line in csvFile:
        name, coords, area, population, pop_density, gdp, income = line
        lat_lng = coords.split()
        location = Point(lat_lng[1], lat_lng[0])
        location.setfillColor("red")
        city = City(name, location, area, population, pop_density, gdp, income)
        cities.append(city)

bounding_box = minBoundingBox(cities) # bounding box for cities

#///////////////////////////////////////////////////Scaling the data ///////////////////////////////////////////
scale = 900/max(bounding_box.getheight(), bounding_box.getwidth())

for city in cities:
    lng = city.getLocation().getX() * scale
    lat = city.getLocation().getY() * scale
    coords = city.getLocation()
    coords.setPosition(lng, lat)
    city.setLocation(coords)

bounding_box_lng = bounding_box.centroid().getX() * scale
bounding_box_lat = bounding_box.centroid().getY() * scale

#///////////////////////////////////////////////translating the data ///////////////////////////////////////////
xTranslation = 500 - bounding_box_lng
yTranslation = 500 - bounding_box_lat

for city in cities:
    x_translated = city.getLocation().getX() + xTranslation
    y_translated = city.getLocation().getY() + yTranslation
    coords = city.getLocation()
    coords.setPosition(x_translated, y_translated)
    city.setLocation(coords)
    
#/////////////////////////////////////////////////plotting and labelling the data ///////////////////////////////////////
for city in cities:
    plt.scatter(city.getLocation().getX(), city.getLocation().getY(), c = city.getLocation().getfillColor())
    plt.text(city.getLocation().getX(), city.getLocation().getY(), city.getName())
    


