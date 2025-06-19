# CSINTSY S13 - State Based Models
# Created by: Donato, John Joseph
            # Javier, Audrin Matthew
            # Ching, Nicolas Miguel 
            # Ocampo, Kurt Christian

# Initial Commit: 2023-10-16
# Uninformed Search : BFS
# Informed Search : A*

# For visualization and graph representation
import networkx as nx
import matplotlib.pyplot as plt
from utils.math_utils import euclidean, euclidean_heuristic
from utils.uninformed_utils import dfs, ucs
from utils.informed_utils import astar

# Define the positions of each eatery in a 2D space (x, y) coordinates.
positions = {
    "Bonchon": (0, 0),
    "KFC": (1, 0),
    "McDonald's": (2, 0),
    "Bloemen": (3, 0),
    "Agno": (4, 0),
    "Starbucks": (5, 0),
    "711": (6, 0),
    "Perico's": (7, 0),
    "La Toca": (8, 0),
    "The Barn": (8, -1),
    "Green Mall": (7, -1),
    "Jollibee": (7, -2),
    
    "Mang Inasal": (-1, -2),
    "Tokyo Tokyo": (0, -2),
    "Burger King": (1, -2),
    "Chowking": (2, -2),
    "24 Chicken": (3, -2),
    "K-Mart": (4, -1),
    "Gang Gang Chicken": (5, -1),
    "Uncle John's": (3, -3),
    "Tapa King": (5, -2)
}

# Rescale positions for better visuals
scale_factor = 50
scaled_positions = {node: (x * scale_factor, y * scale_factor) for node, (x, y) in positions.items()}

# Define edges between nodes ( eatery -> eatery )
edges = [
    ("La Toca", "Perico's"),
    ("La Toca", "The Barn"),
    ("La Toca", "Green Mall"),
    ("Perico's", "711"),
    ("Perico's", "Green Mall"),
    ("711", "Green Mall"),
    ("Green Mall", "Jollibee"),
    ("The Barn", "Green Mall"),
    ("The Barn", "Jollibee"),
    ("711", "Starbucks"),
    ("Starbucks", "Gang Gang Chicken"),
    ("Starbucks", "Agno"),
    ("Agno", "K-Mart"),
    ("Agno", "24 Chicken"),
    ("Agno", "Bloemen"),
    ("Bloemen", "McDonald's"),
    ("McDonald's", "KFC"),
    ("McDonald's", "Uncle John's"),
    ("24 Chicken", "Uncle John's"),
    ("Uncle John's", "Tapa King"),
    ("Gang Gang Chicken", "Tapa King"),
    ("Gang Gang Chicken", "K-Mart"),
    ("Tapa King", "Jollibee"),
    ("KFC", "Bonchon"),
    ("KFC", "Tokyo Tokyo"),
    ("Bonchon", "Mang Inasal"),
    ("Mang Inasal", "Tokyo Tokyo"),
    ("Tokyo Tokyo", "Burger King"),
    ("Burger King", "Chowking"),
    ("Chowking", "24 Chicken"),
    ("24 Chicken", "K-Mart"),
]

heuristics = {}

def initialize_graph():
    G = nx.Graph()
    G.add_nodes_from(scaled_positions.keys())

    for n1, n2 in edges:
        distance = euclidean(scaled_positions[n1], scaled_positions[n2])
        G.add_edge(n1, n2, weight=distance)
    
    return G

def draw_graph(graph, path, positions, cost=None):
    edge_colors = []
    for edge in graph.edges():
        if edge in list(zip(path, path[1:])) or tuple(reversed(edge)) in list(zip(path, path[1:])):
            edge_colors.append('red')
        else:
            edge_colors.append('gray')

    plt.figure(figsize=(12, 10))
    nx.draw(graph, positions, with_labels=True, node_color='lightblue', node_size=1500,
            edge_color=edge_colors, width=2, font_size=12)
    
    edge_distances = {
        (u, v): f"{int(d['weight'])}m" for u, v, d in graph.edges(data=True)
    }

    nx.draw_networkx_edge_labels(
        graph, positions,
        edge_labels=edge_distances,
        font_size=9,
        font_color='black'
    )

    return plt

def display_dfs_path(graph, start, goal):
    dfs_path = dfs(graph, start, goal)
    print("DFS Path", dfs_path)
    
    return dfs_path, "DFS Search"

def display_ucs_path(graph, start, goal):
    ucs_path, cost = ucs(graph, start, goal)
    print("UCS Path", ucs_path)
    print("Total Cost ", cost)
    
    return ucs_path, cost, "UCS Search"

def main():
    # Eatery List
    # McDonald's, Bloemen, Agno, Starbucks, 711, Perico's, La Toca
    # Tapa King, 24 Chicken, Mang Inasal, KFC, Bonchon, K-Mart
    # Jollibee, Chowking, Burger King, Tokyo Tokyo, Green Mall
    # Uncle John's, Gang Gang Chicken

    G = initialize_graph()
    
    start = "24 Chicken"
    goal = "Green Mall"

    #dfs_path, name = display_dfs_path(G, start, goal)

    ucs_path, cost, name = display_ucs_path(G, start, goal)

    pos = scaled_positions

    #draw_graph(G, dfs_path, pos)

    draw_graph(G, ucs_path, pos, cost=cost)

    plt.axis("equal")
    plt.show()

if __name__ == "__main__":
    main()