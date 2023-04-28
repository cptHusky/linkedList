def dijkstra(graph: dict, start: str) -> dict:
    distances = {node: float('inf') for node in graph}
    if distances[start]:
        distances[start] = 0
    else:
        raise KeyError
    visited = set()

    while len(visited) != len(graph):
        current_node = None
        min_distance = float('inf')

        for node in graph:
            if distances[node] < min_distance and node not in visited:
                current_node = node
                min_distance = distances[node]

        for neighbor, weight in graph[current_node].items():
            if neighbor not in visited:
                distance = min_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance

        visited.add(current_node)
    return distances
