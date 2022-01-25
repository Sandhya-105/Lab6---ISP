# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 17:51:38 2022

@author: SANDHYA
"""

import json
from Point import Point
from Rectangle import Rectangle
from Polyline import Polyline
import matplotlib.pyplot as plt


polylines = []
c_lines = []
 # --------------------------------------------------------minimum bounding box function --------------------------------------
def minBoundingBox(polylines):
    xArray = []
    yArray = []
    for line in polylines:
        for coords in line:
          xArray.append(coords[0])
          yArray.append(coords[1])
    topleftpt = Point(min(xArray)- 50, max(yArray)+ 50)
    width = (max(xArray) -min(xArray)) + 100
    height = (max(yArray) - min(yArray)) + 100
    bbox = Rectangle(topleftpt, width, height)
    return bbox

# -------------------------------------------------------- opening and reading the data -----------------------------------------
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
        
bounding_box = minBoundingBox(polylines)

# ---------------------------------------------------scaling the data ---------------------------------------------
scale = 900/max(bounding_box.getheight(), bounding_box.getwidth())

for lines in c_lines:
    temp = []
    for coords in lines.get_points():
        lng = coords.getX() * scale
        lat = coords.getY() * scale
        coords.setPosition(lng, lat)
        temp.append(coords)
    lines.set_points(temp)

bounding_box_lng = bounding_box.centroid().getX() * scale
bounding_box_lat = bounding_box.centroid().getY() * scale

# -------------------------------------------------translating the data ---------------------------------------------
xTranslation = 500 - bounding_box_lng
yTranslation = 500 - bounding_box_lat

for lines in c_lines:
    temp = []
    for coords in lines.get_points():
        lng_trans = coords.getX() + xTranslation
        lat_trans = coords.getY() + yTranslation
        coords.setPosition(lng_trans, lat_trans)
        temp.append(coords)
    lines.set_points(temp)

# ---------------------------------------------------plotting the data -----------------------------------------------    
for lines in c_lines:
    xArray = []
    yArray = []
    for coords in lines.get_points():
        xArray.append(coords.getX())
        yArray.append(coords.getY())
    
    plt.plot(xArray, yArray, c = lines.getstrokeColor())
    