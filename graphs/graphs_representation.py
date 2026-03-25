# GRAPH = {V, E}
# G1 = {{A, B, C, D, E, F}, {{A, B}, {B, D}, {B, E}, {D, E}, {E, F}}


# Dictionary Adjacency List

G1 = {
    'A': ['B'],
    'B': ['A', 'D', 'E'],
    'C': [],
    'D': ['B', 'E'],
    'E': ['B', 'D', 'E'],
    'F': ['E'],
}

# Adjacency matrix (V x V)

G2 = [
#    A  B  C  D  E  F
    [0, 1, 0, 0, 0, 0], # A
    [1, 0, 0, 1, 1, 0], # B
    [0, 0, 0, 0, 0, 0], # C
    [0, 1, 0, 0, 1, 0], # D
    [0, 1, 0, 1, 0, 1], # E
    [0, 0, 0, 0, 1, 0], # F
]

# adding 'NewVertex' as a key of an Adjacency list 
def add_vertex(graph, NewVertex):
    graph[NewVertex] = []

# remove 'Vertex' as a key of an Adjacency list 
def remove_vertex(graph, Vertex):
    if Vertex in graph:
        for v in graph[Vertex]:
            graph[v].remove(Vertex)
        del graph[Vertex]
    
# adding 'AdjVertex' to the list of Vertices connected to 'Vertex' 
def add_edge(graph, Vertex, AdjVertex):
    if AdjVertex in graph and AdjVertex in graph:
        graph[Vertex].append(AdjVertex)
        graph[AdjVertex].append(Vertex)

# removing 'AdjVertex' to the list of Vertices connected to 'Vertex'
def remove_edge(graph, Vertex, AdjVertex):
    if Vertex in graph and AdjVertex in graph[Vertex]:
        graph[Vertex].remove(AdjVertex)
        graph[AdjVertex].remove(Vertex)

# returning the sum of graph degrees (handshaking lemma: 2|E|)
def sum_degrees(graph):
    total = 0
    for v in graph:
        total += len(graph[v])
    return total


# teste das funções

add_vertex(G1, 'G')
print("criando nodo G: ")
print(f"G: {G1['G']}")

print("adicionado aresta entre os nodos G e A")
add_edge(G1, 'G', 'A')
print(f"G: {G1['G']}")
print(f"A: {G1['A']}")
print(f"soma dos graus dos vertices de G1: {sum_degrees(G1)}")

print("removendo nodo G")
remove_vertex(G1, 'G')
print(f"A: {G1['A']}")

print(f"soma dos graus dos vertices de G1: {sum_degrees(G1)}")







    
    

