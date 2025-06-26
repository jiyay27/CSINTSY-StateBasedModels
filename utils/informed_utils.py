# astar_utils.py for A* search algorithm

import heapq

def astar(graph, start, goal, heuristic):
    open_set = []
    heapq.heappush(open_set, (0, [start]))  # (f_score, path)

    g_scores = {start: 0}
    visited = set()

    while open_set:
        f_score, path = heapq.heappop(open_set)
        current = path[-1]

        if current == goal:
            final_g = g_scores[current]
            final_h = heuristic(current, goal)
            final_f = final_g + final_h
            print(f"\nA* reached goal: {current}")
            print(f"g(n): {round(final_g, 2)}, h(n): {round(final_h, 2)}, f(n): {round(final_f, 2)}")
            return path, final_f

        if current in visited:
            continue

        visited.add(current)
        g = g_scores[current]
        h = heuristic(current, goal)
        f = g + h
        print(f"Visited: {current} | g(n): {round(g,2)} | h(n): {round(h,2)} | f(n): {round(f,2)}")


        for neighbor in graph.neighbors(current):
            edge_weight = graph[current][neighbor]['weight']
            tentative_g = g_scores[current] + edge_weight

            if neighbor not in g_scores or tentative_g < g_scores[neighbor]:
                g_scores[neighbor] = tentative_g
                h = heuristic(neighbor, goal)
                f = tentative_g + h
                heapq.heappush(open_set, (f, path + [neighbor]))
                print(f"Exploring {neighbor} via {current} | g: {round(tentative_g,2)} h: {round(h,2)} f: {round(f,2)}")

    return None, float('inf')  # no path found
