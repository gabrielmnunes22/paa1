# Gabriel Nunes - 08/05/2026

import heapq

def dijkstra(graph, start, destination):

    # Inicialização
    visitado = {v: [False, False] for v in graph.keys()}
    dist = {v: [float('inf'), float('inf')] for v in graph.keys()}     # dist[0] - distância par e dist[1] - distância ímpar
    previous = {v: [None, float('inf')] for v in graph.keys()}

    dist[start] = [0, float('inf')]  # Origem começa com distância zero

    paridade = 0
    fila = [(0, start, paridade)]

    while fila:  # enquanto fila não for vazia
        #print(fila)
        #print_dict(dist)
        #print()
        
        dist_no, node, paridade = heapq.heappop(fila)  # extrai nodo com menor distância na fila

        if visitado[node][paridade]:
            continue  

        visitado[node][paridade] = True
        

        #print(f"no atual: {node}")
    
        for vizinho, peso in graph[node]:    # para cada vizinho v de u
            nova_dist = dist[node][paridade] + peso     # distância até u mais peso da aresta u-v
            nova_paridade = 1 - paridade

            if nova_dist < dist[vizinho][nova_paridade]:       # se distância menor que a atual
                previous[vizinho] = node, paridade
                dist[vizinho][nova_paridade] = nova_dist                
                heapq.heappush(fila, (nova_dist, vizinho, nova_paridade))  # coloca v na fila com sua distância atual da origem
        
    return dist, previous


def print_dict(dict):
    for key, value in dict.items():
        print(f"{key} : {value}")
        
C, V = map(int, input().split())

graph = {}
for i in range(C):
    graph[i + 1] = []

for i in range(V):
    C1, C2, G = map(int, input().split())
    graph[C1].append((C2, G))
    graph[C2].append((C1, G))

#print_dict(graph)

dist, previous = dijkstra(graph, 1, C)
#print(dist[C])
#print_dict(previous)

if dist[C][0] == float('inf'):
    print("-1")
else:
    print(dist[C][0])