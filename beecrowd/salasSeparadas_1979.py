# Gabriel Machado Nunes

def printGraph(graph):
    for key, value in graph.items():
        print(f"{key} : {value}")

def bipartite(g):
    cor = {}  # vetor de cores (True e False)
    visited = {}  
    for i in g.keys():  # para todo nodo i em g
        visited[i] = False  
    for x in g.keys():  
        if not (visited[x]):  
            l = [x]  # inicia a busca em x
            cor[x] = True  # atribui cor 1 a x
            visited[x] = True  
            while len(l) > 0:  
                i = l.pop(0)  
                for j in g[i]:  
                    if (
                        visited[j] and cor[i] == cor[j]
                    ):  # se vizinho já colorido com cor oposta
                        return False  # achou ciclo impar
                    elif not (visited[j]):  # se vizinho ainda não colorido
                        l.append(j)  # adiciona a lista
                        visited[j] = True  # registra como visitado
                        cor[j] = not (cor[i])  # atribui cor inversa ao nodo atual
    return True  # se nao ha ciclo impar, o grafo e bipartido



from collections import deque

n = int(input())                   # número de aluno que vão fazer a prova
while n != 0:

    graph = {i : [] for i in range(1, n+1)}
    for _ in range(n):
        id = int(input())       # identificador aluno
        vizinhos = [int(x) for x in input().split()]  
        graph[id] = vizinhos 
        for vizinho in vizinhos:
            graph[vizinho].append(id)
        # preenche o grafo 

    isBipartite = bipartite(graph)

    if isBipartite:
        print("SIM")
    else:
        print("NAO")
    

    n = int(input())




