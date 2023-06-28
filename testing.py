# this file serves to try and slowly build a very rudimentary slicer (firstly attempting to use the reeb graph and finding a formula using 
# max, min and saddle points to then write onto gcode)

import numpy as np
from stl import mesh
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

meshModel = mesh.Mesh.from_file('UReCA-Summer-Project/stls/40mmcube.stl')




