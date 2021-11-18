# P11437 LCA
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)

stdin = open('./input.txt', 'r')

# 정점의 수
n = int(stdin.readline())

# 그래프
graph = [[] for _ in range(n+1)]

#부모 테이블 
parent = [[0] * 21 for _ in range(n+1)]
# 각 노드의 깊이
depth = [0] * (n+1)

# 깊이가 계산되었는지 확인하는 리스트
check = [0] * (n+1)

def dfs(x, d):
    check[x] = True
    depth[x] = d
    for y in graph[x]:
        if check[y]:
            continue
        parent[y][0] = x
        dfs(y, d+1)

def set_parent():
    dfs(1, 0)
    for i in range(1, 21):
        for j in range(1, n+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]


def LCA(a, b):
    # b가 더 깊도록 설정
    if depth[a] > depth[b]:
        a, b  = b, a
    # 깊이가 동일하도록
    for i in range(21-1, -1, -1):
        if depth[b]- depth[a] >= (1 << i):
            b = parent[b][i]
    # 부모가 같아지도록
    if a == b:
        return a
    for i in range(21-1, -1, -1):
        # 조상을 향해 거슬러 올라가기
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    
    # 부모가 찾고자 하는 조상
    return parent[a][0]

for _ in range(n-1):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

set_parent()
m = int(stdin.readline())

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    print(LCA(a, b))