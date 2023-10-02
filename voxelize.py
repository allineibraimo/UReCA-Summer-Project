from stl import mesh
import stltovoxel
import numpy as np

# modelOne = mesh.Mesh.from_file('C:/Users/allin/OneDrive/Documents/GitHub/UReCA-Summer-Project/stls/40mmcube.stl')
stltovoxel.convert_file('stls/40mmcube.stl', 'voxels/test2.xyz', 50)

