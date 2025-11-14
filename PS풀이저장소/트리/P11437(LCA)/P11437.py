## P11437. LCA
from sys import stdin, setrecursionlimit
stdin = open('./input.txt', 'r')
setrecursionlimit(10**7)

n = int(stdin.readline())               
graph = [[] for _ in range(n+1)] 
LOG = 17  

for _ in range(n-1):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [[0] * (n+1) for _ in range(LOG)]
depth = [0] * (n+1)
visited = [False] * (n+1)

def dfs(x, d):
    visited[x] = True
    depth[x] = d
    for nx in graph[x]:
        if not visited[nx]:
            parent[0][nx] = x 
            dfs(nx, d+1)

dfs(1, 0)

for k in range(1, LOG):
    for v in range(1, n+1):
        parent[k][v] = parent[k-1][ parent[k-1][v] ]

def lca(a, b):
  
    if depth[a] < depth[b]:
        a, b = b, a

    diff = depth[a] - depth[b]
  
    for k in range(LOG):
        if diff & (1 << k):
            a = parent[k][a]

  
    if a == b:
        return a

  
    for k in reversed(range(LOG)):
        if parent[k][a] != parent[k][b]:
            a = parent[k][a]
            b = parent[k][b]

  
    return parent[0][a]

m = int(stdin.readline())
for _ in range(m):
  print(lca(*map(int, stdin.readline().split())))