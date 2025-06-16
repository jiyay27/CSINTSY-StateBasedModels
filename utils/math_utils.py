import math

def euclidean(a, b):
    return math.dist(a, b)

def euclidean_heuristic(positions):
    def heuristic(n1, n2):
        x1, y1 = positions[n1]
        x2, y2 = positions[n2]
        return math.hypot(x2 - x1, y2 - y1)
    return heuristic