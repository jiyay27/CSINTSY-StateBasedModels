# bfs_utils.py for breadth-first search (BFS) algorithm

from collections import deque
import heapq

def dfs(graph, start, goal):
    return None

def ucs(graph, start, goal):
    visited = set()
    queue = [(0, [start])]  # (total_cost, path)

    while queue:
        cost, path = heapq.heappop(queue)
        node = path[-1]

        if node == goal:
            return path, int(cost)

        if node not in visited:
            visited.add(node)
            for neighbor in graph.neighbors(node):
                if neighbor not in visited:
                    edge_weight = graph[node][neighbor]['weight']
                    total_cost = cost + edge_weight
                    heapq.heappush(queue, (total_cost, path + [neighbor]))

    return None, float('inf')