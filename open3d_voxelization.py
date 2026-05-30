import open3d as o3d

# File path
file_path = r"D:\01_Projects\IITH_LiDAR_ground_dataset_labelled_raw\IITH_LiDAR_ground_dataset_labelled_raw\patchwork_chair_ply_0\Patchwork chair.ply"

# Load point cloud
pcd = o3d.io.read_point_cloud(file_path)

# Optional: downsample (makes it faster)
pcd = pcd.voxel_down_sample(voxel_size=0.5)

# Create voxel grid
voxel_size = 0.5  # 🔥 change this to control cube size
voxel_grid = o3d.geometry.VoxelGrid.create_from_point_cloud(pcd, voxel_size=voxel_size)

# Print info
print("Voxel size:", voxel_size)
print("Number of voxels:", len(voxel_grid.get_voxels()))

# Visualize
o3d.visualization.draw_geometries([voxel_grid],
                                  window_name="Voxel Grid",
                                  width=800,
                                  height=600)