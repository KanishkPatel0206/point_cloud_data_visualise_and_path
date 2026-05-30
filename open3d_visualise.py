import open3d as o3d

# File path loading.
file_path = r"D:\01_Projects\point_cloud_data_visualise_and_path\patchwork_chair_ply_0\Patchwork chair.ply"

#loadning the point cloud data
pcd = o3d.io.read_point_cloud(file_path)

#check if the loaded successfully
if not pcd.has_points():
    print("Failed to load point cloud data.")
else:
    print("Point cloud data loaded successfully.")
    print(pcd)
#visualise the point cloud data
o3d.visualization.draw_geometries([pcd], window_name="Point Cloud Visualization", width=800, height=600)