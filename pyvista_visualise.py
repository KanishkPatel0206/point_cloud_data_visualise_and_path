import pyvista as pv

file_path = r"D:\01_Projects\point_cloud_data_visualise_and_path\patchwork_chair_ply_0\Patchwork chair.ply"

mesh = pv.read(file_path)

plotter = pv.Plotter()
plotter.add_mesh(mesh, color='white', point_size=5, render_points_as_spheres=True)
plotter.show(title="Point Cloud Visualization", window_size=(800, 600))