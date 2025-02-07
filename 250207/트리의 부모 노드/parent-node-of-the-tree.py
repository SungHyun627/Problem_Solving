n = int(input())

parent = [-1] * (n+1)
parent[1] = 0
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def find_parent(t):
    for node in graph[t]:
        if parent[node] != -1:
            continue
        parent[node] = t
        find_parent(node)

find_parent(1)
print(*parent[2:], sep="\n")
