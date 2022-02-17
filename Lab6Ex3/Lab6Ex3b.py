# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 17:33:29 2022

@author: SANDHYA
"""

import csv
import json
from City import City
from Point import Point
from Rectangle import Rectangle
from Polyline import Polyline
import matplotlib.pyplot as plt


cities = []
polylines = []
c_lines = []
#Minimum Bounding Box for the cities as well as the coastline ///////////////////////////////////////////////////////////

def minBoundingBox(data, F_type):
    xArray = []
    yArray = []
    if( F_type == "polylines"):
      for line in data:
        for coords in line:
            xArray.append(coords[0])
            yArray.append(coords[1])
            
    elif( F_type == "cities"):
        for city in data:
            xArray.append(city.getLocation().getX())
            yArray.append(city.getLocation().getY())
        
    topleftpt = Point(min(xArray), min(yArray))
    width = (max(xArray) -min(xArray))
    height = (max(yArray) - min(yArray))
    bbox = Rectangle(topleftpt, width, height)
    return bbox

# creating the plotting surface
fig, ax = plt.subplots()
ax.set_aspect("equal")

# open the CSV and JSON file ///////////////////////////////////////////////////////////////////////////////////////
with open("cities.csv", mode = 'r') as file:
    # read the CSV file
    csvFile = csv.reader(file)
    next(csvFile, None) # to skip the header of the CSV file
    for line in csvFile:
        
        name, coords, area, population, pop_density, gdp, income = line
        lat_lng = coords.split()
        location = Point(lat_lng[1], lat_lng[0])
        location.setfillColor("red")
        city = City(name, location, area, population, pop_density, gdp, income)
        cities.append(city)

with open("europe.geojson", mode = 'r') as file:
    gjFile = json.load(file)
    for entry in gjFile['features']:
        polyline = entry['geometry']['coordinates']
        polylines.append(polyline)
        points = []
        for coords in polyline:
            point = Point(coords[0], coords[1])
            points.append(point)
        coastline = Polyline(points)
        coastline.setstrokeColor("Blue")
        c_lines.append(coastline)

bounding_box_lines = minBoundingBox(polylines, "polylines")
bounding_box_cities = minBoundingBox(cities, "cities")

# Scaling the cities and coastline ////////////////////////////////////////////////////////////////////////////////////////

scale = 900/max(bounding_box_lines.getheight(), bounding_box_lines.getwidth())

bounding_box_lng = bounding_box_lines.centroid().getX() * scale
bounding_box_lat = bounding_box_lines.centroid().getY() * scale

for city in cities:
    lng = city.getLocation().getX() * scale
    lat = city.getLocation().getY() * scale
    coords = city.getLocation()
    coords.setPosition(lng, lat)
    city.setLocation(coords)
    
for lines in c_lines:
    temp = []
    for coords in lines.get_points():
        lng = coords.getX() * scale
        lat = coords.getY() * scale
        coords.setPosition(lng, lat)
        temp.append(coords)
    lines.set_points(temp)
    
#Translating the coordinates of cities and coastlines /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

xTranslation = 500 - bounding_box_lng
yTranslation = 500 - bounding_box_lat

for city in cities:
    x_translated = city.getLocation().getX() + xTranslation
    y_translated = city.getLocation().getY() + yTranslation
    coords = city.getLocation()
    coords.setPosition(x_translated, y_translated)
    city.setLocation(coords)
    
for lines in c_lines:
    temp = []
    for coords in lines.get_points():
        lng_trans = coords.getX() + xTranslation
        lat_trans = coords.getY() + yTranslation
        coords.setPosition(lng_trans, lat_trans)
        temp.append(coords)
    lines.set_points(temp)

#Plotting both cities and coastlines with city name ///////////////////////////////////////////////////////////////////////////////////////////////////////

for city in cities:
    plt.scatter(city.getLocation().getX(), city.getLocation().getY(), c = city.getLocation().getfillColor())
    plt.text(city.getLocation().getX(), city.getLocation().getY(), city.getName(), c = "Black", size = 10)
      
for lines in c_lines:
    xArray = []
    yArray = []
    for coords in lines.get_points():
        xArray.append(coords.getX())
        yArray.append(coords.getY())
    plt.plot(xArray, yArray, c = lines.getstrokeColor())

plt.xticks(range(0,1100,200))
plt.yticks(range(0,1100,200))


