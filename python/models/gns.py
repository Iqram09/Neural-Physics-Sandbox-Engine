"""
Graph Network Simulator (GNS) model implementation.
"""
import torch
import torch.nn as nn
from torch_geometric.nn import MessagePassing

class GNS(MessagePassing):
    def __init__(self, node_dim, edge_dim, hidden_dim):
        super().__init__(aggr='add')
        self.node_mlp = nn.Sequential(
            nn.Linear(node_dim + hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim)
        )
        self.edge_mlp = nn.Sequential(
            nn.Linear(2 * node_dim + edge_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim)
        )
        self.out_mlp = nn.Sequential(
            nn.Linear(hidden_dim, node_dim)
        )

    def forward(self, x, edge_index, edge_attr):
        # x: [num_nodes, node_dim]
        # edge_index: [2, num_edges]
        # edge_attr: [num_edges, edge_dim]
        h = self.propagate(edge_index, x=x, edge_attr=edge_attr)
        out = self.out_mlp(h)
        return out

    def message(self, x_i, x_j, edge_attr):
        # x_i: target node features
        # x_j: source node features
        # edge_attr: edge features
        edge_input = torch.cat([x_i, x_j, edge_attr], dim=-1)
        edge_out = self.edge_mlp(edge_input)
        return edge_out

    def update(self, aggr_out, x):
        # aggr_out: aggregated messages for each node
        node_input = torch.cat([x, aggr_out], dim=-1)
        node_out = self.node_mlp(node_input)
        return node_out
