n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


for _ in range(m):
    s, e = map(int, input().split())
    print(graph[s-1][e-1])