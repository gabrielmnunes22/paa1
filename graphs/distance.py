from collections import deque

def distance(graph, s):
    dist = {}
    visited = {}
                                    
    for i in graph.keys():  # initializing visited nodes dict
        visited[i] = False
        dist[i] = -1        # infinite distance
    
    d = deque([s])
    dist[s] = 0
    visited[s] = True

    while len(d) > 0:
        key = d.popleft()
        
        for i in graph[key]:
            if not (visited[i]):
                visited[i] = True
                d.append(i) 
                dist[i] = dist[key] + 1
    return dist


G1 = {
    'A': ['B', 'E'],
    'B': ['E', 'F'],
    'C': ['D'],
    'D': [],
    'E': ['C', 'F'],
    'F': ['D', 'G'],
    'G': []
}

dist = {}
dist = distance(G1, 'A')

for key, value in dist.items():
    print(f"{key}: {value}")