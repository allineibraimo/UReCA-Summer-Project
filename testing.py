# this file serves to try and slowly build a very rudimentary slicer (firstly attempting to use the reeb graph and finding a formula using 
# max, min and saddle points to then write onto gcode)

import numpy as np
from stl import mesh
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import voxelmap as vxm
import trimesh


# # Load the STL file
# mesh = trimesh.load('stls/Simple_Flower_Vase.stl')

# # Define the voxel grid resolution and voxalise mesh
# voxel_object = mesh.voxelized(pitch=0.01)

# # transform texture info to color info
# only_colors = mesh.visual.to_color().vertex_colors
# only_colors = np.asarray(only_colors)
# mesh.visual = mesh.visual.to_color()

# # extract mesh vertices
# vertices = mesh.vertices

# # ProximityQuery bulti-in function to get the closest voxel point centers to each vertex
# _, vert_idx = trimesh.proximity.ProximityQuery(mesh).vertex(voxel_object.points)

# # initialize an array of zeros of size X, Y, Z, 4 to contain the colours for ecah voxelized mesh in the grid
# cube_color = np.zeros([voxel_object.shape[0], voxel_object.shape[1], voxel_object.shape[2], 4])

# for idx, vert in enumerate(vert_idx):
#     vox_verts = voxel_object.points_to_indices(vertices[vert])
#     curr_color = only_colors[vert]
#     curr_color[3] = 255
#     cube_color[vox_verts[0], vox_verts[1], vox_verts[2], :] = curr_color

# voxelized_mesh = voxel_object.as_boxes(colors=cube_color)

# s = trimesh.Scene()
# s.add_geometry(voxelized_mesh)
# s.add_geometry(mesh)
# s.show()

def voxelize(mesh):
    meshPoints = np.array(mesh.points)
    # volume = 0
    cubes = vxm.Model()

    # using the same algorithm as the comparing stls 
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
        num_voxels =  ((-x3 * y2 * z1) + (x2 * y3 * z1) + (x3 * y1 * z2) - (x1 * y3 * z2) - (x2 * y1 * z3) + (x1 * y2 * z3)) / 6

        cubes.XYZ = point
        cubes.RGB = [ hex(np.random.randint(0.5e7,1.5e7))[2:] for i in range(num_voxels) ]   # define random colors for the 10 voxels
        cubes.sparsity = 0.1

        cubes.load(coords=True)

    return cubes


# load model (stl in this case)
testModel = modelOne = mesh.Mesh.from_file('stls/Simple_Flower_Vase.stl')

finalVoxel = voxelize(testModel)
finalVoxel.draw(coloring='automatic',geometry='voxels',len_voxel=0.5, background_color='#ffffff',window_size=[416, 416])



    





















