#P11265 끝나지 않는 파티
#PyPy로 통과
from sys import stdin

stdin = open('./input.txt', 'r')
n, m = map(int, stdin.readline().split())
INF = int(1e10)
graph = [[INF]*(n+1)]

for i in range(1, n+1):
    graph.append([0] + list(map(int, stdin.readline().split())))

for i in range(1, n+1):
    graph[i][i] = INF

# 플로이드 와샬
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][k]+graph[k][j], graph[i][j])

for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    print("Stay here") if graph[a][b] > c else print("Enjoy other party")