import networkx as nx
import matplotlib.pyplot as plt
from utils.uninformed_utils import dfs, ucs
from utils.informed_utils import astar
from utils.math_utils import euclidean_heuristic, euclidean

# --- Graph Data ---
edges = [
    ("La Toca", "Perico's"), ("La Toca", "The Barn"), ("La Toca", "Green Mall"),
    ("Perico's", "711"), ("Perico's", "Green Mall"), ("711", "Green Mall"),
    ("Green Mall", "Jollibee"), ("The Barn", "Green Mall"), ("The Barn", "Jollibee"),
    ("711", "Starbucks"), ("Starbucks", "Gang Gang Chicken"), ("Starbucks", "Agno"),
    ("Agno", "K-Mart"), ("Agno", "24 Chicken"), ("Agno", "Bloemen"),
    ("Bloemen", "McDonald's"), ("McDonald's", "KFC"), ("McDonald's", "Uncle John's"),
    ("24 Chicken", "Uncle John's"), ("Uncle John's", "Tapa King"),
    ("Gang Gang Chicken", "Tapa King"), ("Gang Gang Chicken", "K-Mart"),
    ("Tapa King", "Jollibee"), ("KFC", "Bonchon"), ("KFC", "Tokyo Tokyo"),
    ("Bonchon", "Mang Inasal"), ("Mang Inasal", "Tokyo Tokyo"),
    ("Tokyo Tokyo", "Burger King"), ("Burger King", "Chowking"),
    ("Chowking", "24 Chicken"), ("24 Chicken", "K-Mart"),
]

positions = {
    "Bonchon": (0, 0), "KFC": (1, 0), "McDonald's": (2, 0), "Bloemen": (3, 0),
    "Agno": (4, 0), "Starbucks": (5, 0), "711": (6, 0), "Perico's": (7, 0), "La Toca": (8, 0),
    "The Barn": (8, -1), "Green Mall": (7, -1), "Jollibee": (7, -2), "Mang Inasal": (-1, -2),
    "Tokyo Tokyo": (0, -2), "Burger King": (1, -2), "Chowking": (2, -2), "24 Chicken": (3, -2),
    "K-Mart": (4, -1), "Gang Gang Chicken": (5, -1), "Uncle John's": (3, -3), "Tapa King": (5, -2)
}

# --- Apply scaling to match original behavior ---
scale_factor = 50
scaled_positions = {node: (x * scale_factor, y * scale_factor) for node, (x, y) in positions.items()}

# --- Create weighted graph using scaled positions ---
G = nx.Graph()
for u, v in edges:
    if u in scaled_positions and v in scaled_positions:
        dist = euclidean(scaled_positions[u], scaled_positions[v])
        G.add_edge(u, v, weight=dist)
    else:
        print(f"⚠️ Skipping edge {u}-{v} due to missing position.")

# --- User Interface ---
print("Available algorithms:")
print("1. Depth-First Search (DFS)")
print("2. Uniform Cost Search (UCS)")
print("3. A* Search")

algo_choice = input("Enter the number of the algorithm to use (1-3): ").strip()
start = input("Enter start node: ").strip()
goal = input("Enter goal node: ").strip()

if start not in G or goal not in G:
    print("Invalid start or goal node.")
    print("Available nodes:", list(G.nodes))
    exit()

# --- Run selected algorithm ---
path, cost = None, None
if algo_choice == "1":
    path = dfs(G, start, goal)
    cost = sum(G[path[i]][path[i + 1]]['weight'] for i in range(len(path) - 1)) if path else None
elif algo_choice == "2":
    path, raw_cost = ucs(G, start, goal)
    cost = sum(G[path[i]][path[i + 1]]['weight'] for i in range(len(path) - 1)) if path else None
elif algo_choice == "3":
    heuristic = euclidean_heuristic(scaled_positions)
    path, cost = astar(G, start, goal, heuristic)
else:
    print("Invalid algorithm choice.")
    exit()

# --- Display result ---
if path:
    print(f"\nPath found: {' -> '.join(path)}")
    print(f"Total cost: {round(cost, 2)}")

    # Visualization
    edge_colors = []
    for u, v in G.edges():
        if path and u in path and v in path:
            i1 = path.index(u)
            i2 = path.index(v)
            if abs(i1 - i2) == 1:
                edge_colors.append('red')
            else:
                edge_colors.append('gray')
        else:
            edge_colors.append('gray')

    node_colors = []
    for node in G.nodes():
        if node == start:
            node_colors.append('green')
        elif node == goal:
            node_colors.append('blue')
        elif path and node in path:
            node_colors.append('red')
        else:
            node_colors.append('lightblue')

    plt.figure(figsize=(14, 8))
    nx.draw(G, pos=scaled_positions, with_labels=True, node_color=node_colors,
            edge_color=edge_colors, node_size=1500, font_size=10)

    edge_labels = {(u, v): f"{int(d['weight'])}m" for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos=scaled_positions, edge_labels=edge_labels, font_size=9)

    plt.title(f"{['DFS', 'UCS', 'A*'][int(algo_choice)-1]} Path: {start} → {goal}")
    plt.axis("equal")
    plt.show()
else:
    print("No path found.")
