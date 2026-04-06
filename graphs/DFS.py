# objetivo: percorrer todos os nós possíveis a partir de um nó origem
def dfs_recursivo(graph, visited, s):
    visited[s] = True                 # marco nó da chamada da função como visitado
    print(s)
    
    for i in graph[s]:
        if v[i] == False:
            dfs_recursivo(graph, visited, i)


def dfs_iterativo(graph, visited, s):
    stack = []
    stack.append(s)
    visited[s] = True

    while(len(stack) > 0):
        key = stack.pop()
        print(key)
        
        for i in graph[key]:
            if visited[i] == False:
                visited[i] = True
                stack.append(i)
            

G1 = {
    'A': ['B', 'E'],
    'B': ['E', 'F'],
    'C': ['D'],
    'D': [],
    'E': ['C', 'F'],
    'F': ['D', 'G'],
    'G': []
}

# Dicionário de nós já visitados
v = {}
for key in G1.keys():       # Começo: nenhum nó visitado
    v[key] = False


#dfs_recursivo(G1, v, 'A')
dfs_iterativo(G1, v, 'A')
