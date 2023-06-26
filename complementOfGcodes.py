# This code serves to take in a gcode, extract the functions according to what shape they move in, and keep track of the object's volume as the 
# extruder moves 
import sys
from pygcode import Line

filename1 = sys.argv[1]
filename2 = sys.argv[2]

commands = []

with open(filename1, 'r') as f1:
    for lineInFile in f1.readLines():
        line = Line(lineInFile)    #this decodes the gcode line
        


with open(filename2, 'r') as f2:
    contentOfGcode2 = f2.read()

