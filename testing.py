import numpy as np
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot


modelOne = mesh.Mesh.from_file('stls/40mmcube.stl')

# meshPoints = np.array(modelOne.mesh)

figure = pyplot.figure()
axes = mplot3d.Axes3D(figure)

axes.add_collection3d(mplot3d.art3d.Poly3DCollection(modelOne.vectors))

vectors = np.array(modelOne.vectors)
print(vectors)

# Auto scale to the mesh size
scale = modelOne.points.flatten()
axes.auto_scale_xyz(scale, scale, scale)

# Show the plot to the screen
pyplot.show()