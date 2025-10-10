"""
Training loop for GNS model.
"""
import torch
import wandb
from models.gns import GNS
from torch_geometric.data import DataLoader
import h5py
import numpy as np
from tools.preprocess.graph_builder import build_graph

def load_dataset(hdf5_path):
    with h5py.File(hdf5_path, "r") as f:
        positions = f["positions"][:]
    # Build graphs for each timestep
    graphs = [build_graph(pos) for pos in positions]
    return graphs

def train(hdf5_path, epochs=10, batch_size=32, lr=1e-3):
    graphs = load_dataset(hdf5_path)
    loader = DataLoader(graphs, batch_size=batch_size, shuffle=True)
    model = GNS(node_dim=3, edge_dim=0, hidden_dim=64)
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    wandb.init(project="gns-training")

    for epoch in range(epochs):
        total_loss = 0
        for batch in loader:
            optimizer.zero_grad()
            pred = model(batch.x, batch.edge_index, None)
            # Dummy target: next position (for demo)
            target = batch.x
            loss = torch.nn.functional.mse_loss(pred, target)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        wandb.log({"epoch": epoch, "loss": total_loss / len(loader)})
        print(f"Epoch {epoch}: Loss {total_loss / len(loader):.4f}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python train_gns.py <dataset.h5>")
        exit(1)
    hdf5_path = sys.argv[1]
    train(hdf5_path)
