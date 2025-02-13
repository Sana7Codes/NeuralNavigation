import networkx as nx
import matplotlib.pyplot as plt


class NeuralNetworkModel:
    """Simulates adaptive neural pathways inspired by neuroplasticity"""

    def __init__(self):
        self.network = nx.Graph()  # Nodes: neurons, Edges: synapses with weights
        self.base_strength = 0.5   # Initial synaptic connection strength

    def add_neuron(self, neuron):
        if not isinstance(neuron, str):
            raise ValueError("Neuron ID must be a string")
        if neuron not in self.network:
            self.network.add_node(neuron, activation=0)

    def add_connection(self, neuron1, neuron2, weight=None):
        """Safely adds a synaptic connection between two neurons"""
        if neuron1 not in self.network or neuron2 not in self.network:
            raise ValueError("Both neurons must exist before connecting.")
        weight = weight if weight is not None else self.base_strength
        self.network.add_edge(neuron1, neuron2, weight=weight)

    def strengthen_connection(self, neuron1, neuron2):
        """Hebbian learning: 'Neurons that fire together wire together'"""
        if self.network.has_edge(neuron1, neuron2):
            current_weight = self.network[neuron1][neuron2]['weight']
            new_weight = min(1.0, current_weight +
                             (1 - current_weight) * 0.2)  # Cap at 1.0
            self.network[neuron1][neuron2]['weight'] = new_weight

    def decay_connections(self, decay_rate=0.05):
        """Simulate natural synaptic weakening"""
        for u, v, d in self.network.edges(data=True):
            d['weight'] = max(0, d['weight'] - decay_rate)

    def find_decision_path(self, input_neuron, output_neuron):
        """Adaptive pathfinding with neuro-inspired weights"""
        try:
            path = nx.dijkstra_path(
                self.network, input_neuron, output_neuron, weight='weight')
            # Strengthen used pathways (neuroplasticity simulation)
            for i in range(len(path)-1):
                self.strengthen_connection(path[i], path[i+1])
            return path
        except nx.NetworkXNoPath:
            return None

    def visualize_network(self):
        """Brain-inspired visualization"""
        pos = nx.spring_layout(self.network)
        edge_weights = [max(0.5, self.network[u][v]['weight'] * 3)
                        for u, v in self.network.edges()]  # Adjusted scaling

        plt.figure(figsize=(10, 8))
        nx.draw(self.network, pos, with_labels=True, node_size=800,
                node_color='skyblue', edge_color='gray',
                width=edge_weights)
        plt.title("Neuroplastic Network Simulation (Neuro-Canva Framework)")
        plt.show()


# --------------------------
# Neuro-Canva Decision Simulation
# --------------------------

# Initialize cognitive network
decision_model = NeuralNetworkModel()

# Create neural nodes for decision process
neurons = ["Sensory Input", "Attention", "Memory Recall",
           "Risk Assessment", "Decision Output"]
for n in neurons:
    decision_model.add_neuron(n)

# Form initial pathways (weak connections)
decision_model.add_connection("Sensory Input", "Attention", weight=0.3)
decision_model.add_connection("Attention", "Memory Recall", weight=0.4)
decision_model.add_connection("Memory Recall", "Risk Assessment", weight=0.3)
decision_model.add_connection("Risk Assessment", "Decision Output", weight=0.5)

# Simulate decision-making process
print("First decision path:")
path1 = decision_model.find_decision_path("Sensory Input", "Decision Output")
print(f"Path: {path1}")

print("\nStrengthened path after repetition:")
path2 = decision_model.find_decision_path("Sensory Input", "Decision Output")
print(f"Path: {path2}")

# Visualize neuroplastic changes
decision_model.visualize_network()
