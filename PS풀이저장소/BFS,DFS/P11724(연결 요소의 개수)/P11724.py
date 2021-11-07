#P11724 연결 요소의 개수
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)

stdin = open('./input.txt', 'r')

n, m = map(int, stdin.readline().split())
edges = [[]  for _ in range(n+1)]
visited = [False] * (n+1)
result = 0

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    if a > b:
        a, b = b, a
    edges[a].append(b)
    edges[b].append(a)

def dfs(node):
    visited[node] = True
    if not edges[node]:
        return

    for i in edges[node]:
        if not visited[i]:
            dfs(i)

for k in range(1, n+1):
    if not visited[k]:
        dfs(k)
        result += 1

print(result)