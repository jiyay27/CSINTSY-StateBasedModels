# astar_utils.py for A* search algorithm

import heapq

def astar(graph, start, goal, heuristic):
    open_set = [(0, start)]  # (f_score, node)
    came_from = {start: None}
    g_scores = {start: 0}
    visited = set()

    nodes_visited = 0
    nodes_expanded = 0

    while open_set:
        f_score, current = heapq.heappop(open_set)

        if current in visited:
            continue

        visited.add(current)
        nodes_visited += 1

        if current == goal:
            final_g = g_scores[current]
            final_h = heuristic(current, goal)
            final_f = final_g + final_h
            path = reconstruct_path(came_from, start, goal)
            print(f"\nA* reached goal: {current}")
            print(f"g(n): {round(final_g, 2)}, h(n): {round(final_h, 2)}, f(n): {round(final_f, 2)}")
            print(f"A* - Nodes Visited: {nodes_visited}, Nodes Expanded: {nodes_expanded}")
            return path, final_f

        for neighbor in graph.neighbors(current):
            edge_weight = graph[current][neighbor].get('weight', 1)
            tentative_g = g_scores[current] + edge_weight

            if neighbor not in g_scores or tentative_g < g_scores[neighbor]:
                g_scores[neighbor] = tentative_g
                came_from[neighbor] = current
                h = heuristic(neighbor, goal)
                f = tentative_g + h
                heapq.heappush(open_set, (f, neighbor))
                nodes_expanded += 1

    print(f"A* - Nodes Visited: {nodes_visited}, Nodes Expanded: {nodes_expanded}")
    return None, float('inf')

def reconstruct_path(came_from, start, goal):
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path