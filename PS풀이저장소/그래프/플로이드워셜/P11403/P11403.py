from sys import stdin

stdin = open('./input.txt', 'r')

#정점의 개수
n = int(stdin.readline())

#경로가 없을 때 비용 INF
INF = int(1e9)

#그래프의 인접행렬
graph = [list(map(int, stdin.readline().rstrip().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            graph[i][j] = INF

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0 and graph[i][j] != INF:
            graph[i][j] = 1
        else:
            graph[i][j] = 0

for i in range(n):
    print(*graph[i], sep=' ')