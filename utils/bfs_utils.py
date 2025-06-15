# bfs_utils.py for breadth-first search (BFS) algorithm

from collections import deque

def bfs(graph, start, goal):
    visited = set()
    queue = deque([[start]])  # queue of paths, not just nodes

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path  # path found!

        if node not in visited:
            visited.add(node)
            for neighbor in graph.neighbors(node):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None  # no path found
