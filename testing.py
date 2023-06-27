import numpy as np
from stl import mesh
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt


modelOne = mesh.Mesh.from_file('stls/Simple_Flower_Vase.stl')

# # meshPoints = np.array(modelOne.mesh)

# figure = plt.figure()
# axes = mplot3d.Axes3D(figure)

# axes.add_collection3d(mplot3d.art3d.Poly3DCollection(modelOne.vectors))

# # Auto scale to the mesh size
# scale = modelOne.points.flatten()
# axes.auto_scale_xyz(scale, scale, scale)

# # Show the plot to the screen
# plt.show()

# Extract vertex coordinates from the mesh
vertices = modelOne.vectors.reshape(-1, 3)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the mesh vertices
ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], c='b', s=1)

# Set axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set plot limits
ax.set_xlim(np.min(vertices[:, 0]), np.max(vertices[:, 0]))
ax.set_ylim(np.min(vertices[:, 1]), np.max(vertices[:, 1]))
ax.set_zlim(np.min(vertices[:, 2]), np.max(vertices[:, 2]))

# Show the plot
plt.show()







