from sys import stdin
import heapq
INF = int(1e6)

stdin = open('./input.txt', 'r')

# n : 지역 수, m : 수색 범위, r : 길의 개수
n, m, r= map(int, stdin.readline().split())

# 한 지역에서 다른 지역까지의 최단거리
graph = [[INF] * (n+1) for _ in range(n + 1)]
# 해당 지역에 있는 아이템 개수
item = [0] + list(map(int, stdin.readline().split()))

# A->A로 가는 최단거리는 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if i==j:
            graph[i][j] = 0
            
# 지역 간 거리 입력
for _ in range(r):
    a, b, c = map(int, stdin.readline().split())
    graph[a][b] = c
    graph[b][a] = c

# 플로이드 와샬 알고리즘
for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

# 최대 item 개수
max_result = 0
# 각 지역별 아이템의 개수를 계산하여 최대 아이템 개수 갱신
for i in range(1, n+1):
    result = 0
    for j in range(1, n+1):
        if graph[i][j] <= m:
            result += item[j]
    max_result = max(max_result, result)
print(max_result)