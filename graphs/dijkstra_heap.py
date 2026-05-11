import heapq

def dijkstra_heap(graph, start):
    dist = {node: float('inf') for node in graph.keys()}
    visitado = {node: False for node in graph.keys()}
    previous = {node: None for node in graph.keys()}

    dist[start] = 0

    fila = [(0, start)]
    while fila:
        peso, node = heapq.heappop(fila)

        if visitado[node]:
            continue

        visitado[node] = True

        for vizinho, peso in graph[node]:
            nova_dist = dist[node] + peso
            if nova_dist < dist[vizinho]:
                dist[vizinho] = nova_dist
                previous[vizinho] = node
                heapq.heappush(fila, (nova_dist, vizinho)) 

    return dist, previous

def print_dict(graph):
    for key, value in graph.items():
        print(f"{key} : {value}")

G1 = {
    'S': [('A', 1), ('B', 3)],
    'A': [('S', 1), ('D', 5), ('C', 4)],
    'B': [('S', 3), ('D', 4), ('C', 1)],
    'C': [('A', 4), ('B', 1), ('E', 6)],
    'D': [('A', 5), ('B', 4), ('E', 2)],
    'E': [('D', 2), ('C', 6)],
    'F': []
}

dist, previous = dijkstra_heap(G1, 'S')
print_dict(dist)
print()
print_dict(previous)