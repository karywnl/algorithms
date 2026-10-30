import heapq


graph = {
    'A': [('B', 2), ('C', 6)],
    'B': [('A', 2), ('C', 3), ('D', 5)],
    'C': [('A', 6), ('B', 3), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}


def prims(graph, start):
    """Return (selected_edges, total_weight) for the starting component.

    Neighbours are (vertex, weight) pairs. Heap ties compare vertex labels,
    so labels should be mutually comparable, such as all strings or all ints.
    """
    seen = {start}
    heap = []
    total_weight = 0
    selected_edges = []

    for destination, weight in graph[start]:
        heapq.heappush(heap, (weight, start, destination))

    while heap:
        weight, source, destination = heapq.heappop(heap)

        if destination in seen:
            continue

        seen.add(destination)
        selected_edges.append((source, destination, weight))
        total_weight += weight

        for neighbour, edge_weight in graph[destination]:
            if neighbour not in seen:
                heapq.heappush(heap, (edge_weight, destination, neighbour))

    return selected_edges, total_weight


if __name__ == '__main__':
    mst, total = prims(graph, 'A')
    print(mst)
    print(total)
