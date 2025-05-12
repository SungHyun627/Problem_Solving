from sys import setrecursionlimit
setrecursionlimit(10**6)
n = int(input())

graph = [[] for _ in range(n+1)]
checked = [False] *(n+1)
d = [0] * (n+1)

for _ in range(n - 1):
    f, t = map(int, input().split())
    graph[f].append(t)
    checked[t] = True

a, b = map(int, input().split())

root = checked[1:].index(False) + 1


### 높이 게산
def dfs(x, depth):
    d[x] = depth
    for node in graph[x]:
        dfs(node, depth+1)

dfs(root, 0)

## 높이 맞추기
while d[a] != d[b]:
    if d[a] > d[b]:
        for i in range(1, n+1):
            if a in graph[i]:
                a = i
                break
    else:
        for i in range(1, n+1):
            if b in graph[i]:
                b = i
                break

## 공통 조상 찾기
while a != b:
    for i in range(1, n+1):
        if a in graph[i]:
            a = i
            break
    for i in range(1, n+1):
        if b in graph[i]:
            b = i
            break

print(a)
        
