from sys import stdin
INF = int(1e10)

stdin = open('./input.txt', 'r')

# n : 도시 수
n = int(stdin.readline())
# m : 버스 수
m = int(stdin.readline())

# 특정 도시에서 다른 도시로 가는 비용
graph = [[INF] * (n+1) for _ in range(n+1)]
# A->A로 가는 비용은 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if i==j:
            graph[i][j] = 0
# 비용 입력
for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    graph[a][b] = min(graph[a][b], c)

# 플로이드 와샬 알고리즘 수행
for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

# 만약 INF라면 0으로 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            graph[i][j] = 0
# 출력
for i in range(1, n+1):
    print(*graph[i][1:])