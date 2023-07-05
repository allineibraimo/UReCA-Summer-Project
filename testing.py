# this file serves to try and slowly build a very rudimentary slicer (firstly attempting to use the reeb graph and finding a formula using 
# max, min and saddle points to then write onto gcode)

import numpy as np
from stl import mesh
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

meshModel = mesh.Mesh.from_file('stls/Simple_Flower_Vase.stl')
fig = plt.figure()
ax = plt.axes(projection='3d')

points = meshModel.points
# points = points.flatten()

#get points in each axis
x_axis = meshModel.x
y_axis = meshModel.y
z_axis = meshModel.z

#for all z points that are the same, create a pixelated area 
z_points = z_axis.flatten()










