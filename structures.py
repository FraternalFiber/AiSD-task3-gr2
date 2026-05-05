import numpy as np

class GraphMatrix:
    """Reprezentacja grafu za pomocą macierzy incydencji"""
    def __init__(self, num_vertices):
        self.v = num_vertices
        self.edges_list = []  # Lista krawędzi (u, v)
        self.matrix = None

    def add_edge(self, u, v):
        self.edges_list.append((u, v))

    def build_matrix(self):
        # Macierz: wiersze = wierzchołki, kolumny = krawędzie
        self.matrix = np.zeros((self.v, len(self.edges_list)), dtype=int)
        for i, (u, v) in enumerate(self.edges_list):
            self.matrix[u-1][i] = -1 # Wyjście
            self.matrix[v-1][i] = 1  # Wejście

    def get_out_neighbors(self, u_idx):
        neighbors = []
        if self.matrix is None: self.build_matrix()
        for e_idx in range(len(self.edges_list)):
            if self.matrix[u_idx][e_idx] == -1:
                for v_idx in range(self.v):
                    if self.matrix[v_idx][e_idx] == 1:
                        neighbors.append(v_idx)
                        break
        return neighbors

    def get_in_degree(self, v_idx):
        if self.matrix is None: self.build_matrix()
        return np.count_nonzero(self.matrix[v_idx] == 1)

class GraphPredecessors:
    """Reprezentacja grafu za pomocą listy poprzedników"""
    def __init__(self, num_vertices):
        self.v = num_vertices
        self.predecessors = {i: [] for i in range(num_vertices)}
        self.out_edges = {i: [] for i in range(num_vertices)}

    def add_edge(self, u, v):
        self.predecessors[v-1].append(u-1)
        self.out_edges[u-1].append(v-1)

    def get_out_neighbors(self, u_idx):
        return self.out_edges[u_idx]

    def get_in_degree(self, v_idx):
        return len(self.predecessors[v_idx])