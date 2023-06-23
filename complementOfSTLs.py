# This program attempts to use a compare volumes of two STL files and return their complemet using the volume of a mesh representation formula
# by Cha Sheng and Tsuhan Cheng -> "http://chenlab.ece.cornell.edu/Publication/Cha/icip01_Cha.pdf"
# The program also uses a Mesh library to import stl files and turn them into mesh to obtain data points in the design and use those to try and
# estimate volumes
import numpy as np
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot

# function for calculating volume - 
def calculateVolume(mesh):
    meshPoints = np.array(mesh.points)
    volume = 0

    for point in meshPoints:
        x1 = point[0]
        y1 = point[1]
        z1 = point[2]
        x2 = point[3]
        y2 = point[4]
        z2 = point[5]
        x3 = point[6]
        y3 = point[7]
        z3 = point[8]
        volume += ((-x3 * y2 * z1) + (x2 * y3 * z1) + (x3 * y1 * z2) - (x1 * y3 * z2) - (x2 * y1 * z3) + (x1 * y2 * z3)) / 6
    
    return volume


# import the two meshes
modelOne = mesh.Mesh.from_file('UReCA-Summer-Project/stls/40mmcube.stl')
modelTwo = mesh.Mesh.from_file('UReCA-Summer-Project/stls/20mm_calibraton_cube.stl')

volModelOne = calculateVolume(modelOne)
volModelTwo = calculateVolume(modelTwo) 
    
if(volModelOne == volModelTwo):
    print(0)
elif(volModelOne > volModelTwo):
    print("Model One's volume is bigger than Model Two's volume by %d/n", (volModelOne - volModelTwo))
else:
    print("Model Two's volume is bigger than Model One's volume by %d/n", (volModelTwo - volModelOne))

