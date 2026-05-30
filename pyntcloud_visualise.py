from pyntcloud import PyntCloud
import pyvista as pv

file_path = r"D:\01_Projects\IITH_LiDAR_ground_dataset_labelled_raw\IITH_LiDAR_ground_dataset_labelled_raw\patchwork_chair_ply_0\Patchwork chair.ply"

# Load using PyntCloud
cloud = PyntCloud.from_file(file_path)

# Convert to numpy
points = cloud.points[['x', 'y', 'z']].values

# Create PyVista object
pc = pv.PolyData(points)

# Plot
plotter = pv.Plotter()
plotter.add_points(pc, render_points_as_spheres=True, point_size=2)
plotter.show()