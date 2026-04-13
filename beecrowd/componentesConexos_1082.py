def printGraph(graph):
    for key, value in graph.items():
        print(f"{key}: {value}")


def setGraphEdge(graph, v1, v2):
    graph[v1].append(v2)
    graph[v2].append(v1)

def printComponent(Nodes):
    Nodes.sort()
    for node in Nodes:
        print(f"{node},", end = "")
    print()


def bfs_iterativo(graph, visited, s):
    queue = []
    queue.append(s)
    visited[s] = True

    printNodes = []

    while(len(queue) > 0):
        key = queue.pop(0)
        printNodes.append(key)

        for i in graph[key]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

    return printNodes
   



N = int(input())           # qtd de casos de teste

for i in range(N):
    graph = {}      # lista de adjacências
    letter = 'a'    # nó base para o problema
    V, E = map(int, input().split())    # qtd de vértices e arestas do grafo
    
    for j in range(V):    
        key = chr(ord(letter) + j)   # inserindo as chaves do dicionário              
        graph[key] = [] 

    for k in range(E):
        v1, v2 = input().split()
        setGraphEdge(graph, v1, v2)
    
    visited = {}            # lista de nós visitados
    for node in graph:      # começo com nenhum nó visitado
        visited[node] = graph[node]
        visited[node] = False

    #printGraph(graph)
    #printGraph(visited)

    components = 0      # número de componentes conexos
    print(f"Case #{i + 1}:")
    while(False in visited.values()):
        printNodes = []                 # armezo os nós do componente conexo
        if visited[letter] == False:
            printNodes = bfs_iterativo(graph, visited, letter)
            printComponent(printNodes)
            components += 1
        letter = chr(ord(letter) + 1)
        
    
    print(f"{components} connected components")
    print()






