"""
Converts particle positions to graph data for GNN training.
"""
import numpy as np
import h5py
import torch
from torch_geometric.data import Data
from scipy.spatial import cKDTree

def build_graph(positions, radius=0.1):
    # positions: [num_particles, 3]
    tree = cKDTree(positions)
    edge_index = []
    for i, pos in enumerate(positions):
        neighbors = tree.query_ball_point(pos, r=radius)
        for j in neighbors:
            if i != j:
                edge_index.append([i, j])
    edge_index = torch.tensor(edge_index, dtype=torch.long).t().contiguous()
    x = torch.tensor(positions, dtype=torch.float)
    data = Data(x=x, edge_index=edge_index)
    return data

def load_positions_from_hdf5(hdf5_path, dataset_name="positions"):
    with h5py.File(hdf5_path, "r") as f:
        positions = f[dataset_name][:]
    return positions

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python graph_builder.py <hdf5_file>")
        exit(1)
    hdf5_file = sys.argv[1]
    positions = load_positions_from_hdf5(hdf5_file)
    graph = build_graph(positions)
    print(graph)
