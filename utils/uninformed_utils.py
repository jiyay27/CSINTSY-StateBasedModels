# bfs_utils.py for breadth-first search (BFS) algorithm

import heapq

def ucs(graph, start, goal):
    frontier = [(0, start)]  # (total_cost, node)
    came_from = {start: None}
    cost_so_far = {start: 0}
    visited = set()

    nodes_visited = 0
    nodes_expanded = 0

    while frontier:
        current_cost, current_node = heapq.heappop(frontier)

        if current_node in visited:
            continue

        visited.add(current_node)
        nodes_visited += 1

        if current_node == goal:
            path = reconstruct_path(came_from, start, goal)
            print(f"UCS - Nodes Visited: {nodes_visited}, Nodes Expanded: {nodes_expanded}")
            return path, current_cost

        for neighbor in graph.neighbors(current_node):
            edge_weight = graph[current_node][neighbor].get('weight', 1)
            new_cost = current_cost + edge_weight

            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                came_from[neighbor] = current_node
                heapq.heappush(frontier, (new_cost, neighbor))
                nodes_expanded += 1

    print(f"UCS - Nodes Visited: {nodes_visited}, Nodes Expanded: {nodes_expanded}")
    return None, float('inf')


def reconstruct_path(came_from, start, goal):
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path