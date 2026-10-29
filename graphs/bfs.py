from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

def bfs(graph, start):
    seen = set()
    order = []

    seen.add(start)
    queue = deque([start])

    while queue:
        current_element = queue.popleft()
        order.append(current_element)
        for v in graph[current_element]:
            if v not in seen:
                seen.add(v)
                queue.append(v)

    return order


print(bfs(graph, "A"))