import numpy as np
import math 


def complementFunc(sphereOne, sphereTwo, radius):
    radiusSphereOne = math.sqrt((sphereOne[0] - radius[0]) ** 2 + (sphereOne[1] - radius[1]) ** 2 + (sphereOne[2] - radius[2]) ** 2)
    radiusSphereTwo = math.sqrt((sphereTwo[0] - radius[0]) ** 2 + (sphereTwo[1] - radius[1]) ** 2 + (sphereTwo[2] - radius[2]) ** 2)
    
    volSphereOne = (4/3) * math.pi * (radiusSphereOne ** 3)
    volSphereTwo = (4/3) * math.pi * (radiusSphereTwo ** 3)

    if(volSphereOne == volSphereTwo):
        return 0
    elif(volSphereOne > volSphereTwo ):
        return volSphereOne - volSphereTwo
    else:
        return volSphereTwo - volSphereOne


sphereOne = [1, 2, 3]
sphereTwo = [2, 3, 4]
radius = [0, 0, 0]

result = complementFunc(sphereOne, sphereTwo, radius)
print(result)





