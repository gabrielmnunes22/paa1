def dijkstra(graph, start):
    #inicialização
    dist = {node: float('inf') for node in graph.keys()}
    previous = {node: None for node in graph.keys()}
    visited = {node: False for node in graph.keys()}


    dist[start] = 0
    
    arestas = []
    for node in graph.keys():
        for vizinho, peso in graph[node]:
            arestas.append((node, vizinho, peso))
    
    nodos_visitados = 0
    while nodos_visitados < len(graph):
        #encontrando o vizinho com menor distância(peso)
        #sempre começa pelo nó start
        menor_dist = float('inf')
        u = None
        for node in graph.keys():
            if not visited[node] and dist[node] < menor_dist:
                menor_dist = dist[node]
                u = node
        
        #se não há nó não-visitado, termina loop
        if u == None:
            break
        
        visited[u] = True
        nodos_visitados += 1

        for (origem, destino, peso) in arestas:
            if origem == u and not visited[destino]:
                if dist[origem] + peso < dist[destino]:
                    dist[destino] = dist[origem] + peso
                    previous[destino] = origem

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

#print_dict(G1)
dist, previous = dijkstra(G1, 'S')
print_dict(dist)
print()
print_dict(previous)
