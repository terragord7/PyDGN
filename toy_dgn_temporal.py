import torch
from torch import embedding_renorm_, nn
from torch_geometric.nn import SAGEConv
from torch_geometric.nn import global_add_pool, global_mean_pool
from torch_geometric_temporal.nn.recurrent import DCRNN


class ToyDynamicDGN(nn.Module):
    """
    Simple Dynamic Deep Graph Network that can be used to test the library
    """

    def __init__(self, dim_node_features, dim_edge_features, dim_target, predictor_class, config):
        """
        Initializes the model.
        :param dim_node_features: arbitrary object holding node feature information
        :param dim_edge_features: arbitrary object holding edge feature information
        :param dim_target: arbitrary object holding target information
        :param predictor_class: the class of the predictor that will classify node/graph embeddings produced by this DGN
        :param config: the configuration dictionary to extract further hyper-parameters
        """

        super().__init__()

        dim_embedding = 32
        filter_size = 1

        self.model = DCRNN(dim_node_features, dim_embedding, filter_size)

        # self.predictor is a LinearNodePredictor
        self.predictor = predictor_class(dim_node_features=dim_embedding,
                                         dim_edge_features=dim_edge_features,
                                         dim_target=dim_target, config=config)

    def forward(self, snapshot, prev_state=None):
        # snapshot.x: Tensor of size (num_nodes_t x node_ft_size)
        # snapshot.edge_index: Adj of size (num_nodes_t x num_nodes_t)
        x, edge_index = snapshot.x, snapshot.edge_index
        h_old = 0. if prev_state is None else prev_state

        h = self.model(x, edge_index) + h_old
        h = torch.relu(h)

        # Node predictors assume the embedding is in field "x"
        snapshot.x = h
        out, _ = self.predictor(snapshot)

        return out, h
