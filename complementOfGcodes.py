# This code serves to take in a gcode, extract the functions according to what shape they move in, and keep track of the object's volume as the 
# extruder moves 
import sys

gcode1 = sys.argv[1]
# filename2 = sys.argv[2]

g0123mov = []

commands = []

with open(gcode1, 'r') as code:
    command = code.readline()
    if(command.split()[0] == "G1" or command.split()[0] == "G2" or command.split()[0] == "G3"):
        
        
    print(*command, sep = '\n')


# with open(filename2, 'r') as f2:
#     contentOfGcode2 = f2.read()

