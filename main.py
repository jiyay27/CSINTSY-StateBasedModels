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
from utils.bfs_utils import bfs

graph = {
    "Henry Sy Hall": ["Velasco", "St. La Salle Hall"],
    "Velasco": ["Henry Sy Hall", "Agno", "St. Miguel Hall"],
    "Agno": ["Velasco", "Green Mall", "St. Miguel Hall"],
    "Green Mall": ["Agno", "Jollibee", "McDonalds"],
    "Jollibee": ["Green Mall"],
    "McDonalds": ["Green Mall"],
    # Add more nodes (at least 20 eateries and nearby buildings)
    }

# Heuristic values for each node (for A* search)
heuristics = {
        "Henry Sy Hall": 6,
        "Velasco": 5,
        "Agno": 4,
        "Green Mall": 2,
        "McDonalds": 1,
        "Jollibee": 0
    }

def main():
    # Visualization graph
    G = nx.Graph()
    G.add_edge("Henry Sy Hall", "Velasco", weight=3)
    G.add_edge("Velasco", "Agno", weight=2)
    G.add_edge("Agno", "Green Mall", weight=1)
    G.add_edge("Green Mall", "Jollibee", weight=3)
    G.add_edge("Green Mall", "McDonalds", weight=3)

    

    bfs_path = bfs(G, "Velasco", "Agno")
    print("BFS Path", bfs_path)

    pos = nx.spring_layout(G, seed=42)

    # Define edge colors: red for path, gray for others
    edge_colors = []
    for edge in G.edges():
        if edge in list(zip(bfs_path, bfs_path[1:])) or tuple(reversed(edge)) in list(zip(bfs_path, bfs_path[1:])):
            edge_colors.append('red')  # highlight the BFS path
        else:
            edge_colors.append('gray')

    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500,
            edge_color=edge_colors, width=2, font_size=12)

    plt.title("BFS Path from A to G (in red)")
    plt.show()


if __name__ == "__main__":
    main()