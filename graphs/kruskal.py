vertices = ['A', 'B', 'C', 'D']

edges = [
    ('C', 'D', 10),
    ('A', 'C', 3),
    ('A', 'B', 1),
    ('B', 'C', 2)
]

def find(parent, x):
    while parent[x] != x:
        x = parent[x]
    return x

def union(parent, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x == root_y:
        return False

    parent[root_y] = root_x
    return True

def kruskal(vertices, edges):
    parent = {v : v for v in vertices}
    selected_edges = []
    total_weight = 0

    sorted_edges = sorted(edges, key=lambda edge : edge[2]) 

    for u, v, weight in sorted_edges:
        if union(parent, u, v):
            selected_edges.append((u, v, weight))
            total_weight += weight

    return selected_edges, total_weight


# parent = {'P': 'Q', 'Q': 'R', 'R': 'R'}

# print(find(parent, 'P'))  # R
# print(find(parent, 'Q'))  # R
# print(find(parent, 'R'))  # R

# parent = {'A': 'A', 'B': 'A', 'C': 'C', 'D': 'C'}

# print(union(parent, 'B', 'D'))  # True: merges two groups
# print(find(parent, 'A') == find(parent, 'D'))  # True
# print(union(parent, 'A', 'C'))  # False: already connected

mst, total = kruskal(vertices, edges)
print(mst)
print(total)