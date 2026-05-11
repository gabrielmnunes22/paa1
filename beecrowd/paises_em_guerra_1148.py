import heapq

def dijkstra_heap(graph, start):
    dist = {node: float('inf') for node in graph.keys()}
    visitado = {node: False for node in graph.keys()}
    parent = {node: None for node in graph.keys()}
    
    dist[start] = 0

    fila = [(0, start)]
    while fila:
        #print(fila)
        #print_dict(dist)
        #print()
        peso, node = heapq.heappop(fila)

        if visitado[node]:
            continue

        visitado[node] = True

        #print(f"node: {node}")
        # .items() retorna pares (chave, valor)
        for vizinho, peso in graph[node].items():
    
            nova_dist = dist[node] + peso

            if nova_dist < dist[vizinho]:
                dist[vizinho] = nova_dist
                parent[vizinho] = node
                heapq.heappush(fila, (nova_dist, vizinho)) 

    return dist

def print_dict(graph):
    for key, value in graph.items():
        print(f"{key} : {value}")

while True:

    N, E = map(int, input().split())

    if N == 0 and E == 0:
        break

    graph = {}

    for i in range(N):
        graph[i + 1] = {}

    for _ in range(E):
        X, Y, H = map(int, input().split())
        if X in graph[Y]:
            graph[X][Y] = 0
            graph[Y][X] = 0
        else:    
            graph[X][Y] = H

    #print_dict(graph)
                    
    K = int(input())
    for _ in range(K):
        O, D = map(int, input().split())

        dist = dijkstra_heap(graph, O)

        if dist[D] == float('inf'):
            print("Nao e possivel entregar a carta")
        else:
            print(dist[D])
    print()