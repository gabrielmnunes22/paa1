from collections import deque

def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(f"{element}", end = " ")
        print()

def bfs(matrix, i, j, N, M):
    queue = deque([(i, j)])
    matrix[i][j] = '#'              # marco posição [i][j] da matriz como visitada

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while len(queue) > 0:
        row, col = queue.popleft()
        
        for x, y in directions:
            novoI = x + row 
            novoJ = y + col

            if 0 <= novoI < N and 0 <= novoJ < M:
                if matrix[novoI][novoJ] == '.':
                    queue.append((novoI, novoJ))
                    matrix[novoI][novoJ] = '#'
    

def compConexos(matrix, N, M):
    numComponentes = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == '.':
                bfs(matrix, i, j, N, M)
                numComponentes += 1
    return numComponentes


N, M  = map(int, input().split())

# expression for item in iterable
matrix = [list(input()) for i in range(N)]

#print()
#print_matrix(matrix)

numeroCompConexos = compConexos(matrix, N, M)
print(f"{numeroCompConexos}")
