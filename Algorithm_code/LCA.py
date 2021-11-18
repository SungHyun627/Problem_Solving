# 최소 공통 조상(LCA)알고리즘
# 1. 모든 노드에 대하 깊이(depth) 계산
# 2. 최소 공통 조상을 찾을 두 노드 확인
# 2-1. 두 노드의 깊이가 동일하도록 거슬러 올라간다.
# 2-2. 이후 부모가 같아질 때까지 반복적으로 두 노드의 부모 방향으로 거슬러 올라간다.
# 3. 모든 LCA(a, b) 연산에 대하여 2번의 과정 반복

# 매 쿼리마다 거슬러 올라가기 때문에 O(logn) => m개의 쿼리는 O(mlogn)

from sys import stdin, setrecursionlimit

n = int(stdin.readline())
# 재귀 한도 설정
setrecursionlimit(10 ** 6)

# 부모 노드의 정보
parent = [0] * (n+1)
# 각 노드 까지의 깊이
d = [0] * (n+1)
# 각 노드의 깊이가 계산되었는 지 여부
c = [0] * (n+1)
# 그래프
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 루트 노드부터 시작하여 깊이(depth)를 구하는 함수
def dfs(x, depth):
    c[x] = True
    d[x] = depth
    for y in graph[x]:
        # 이미 계산이 되었다면
        if c[y]:
            continue
        parent[y] = x
        dfs(y, depth + 1)

# A와 B의 최소 공통 조상을 찾는 ㅎ마수
def LCA(a, b):
    # 깊이가 동일하도록
    while d[a] != dp[b]:
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]
    # 노드가 같아 지도록
    while a !=b:
        a = parent[a]
        b = parent[b]
    return a

# 루트 노드는 1번
dfs(1, 0)

# m개의 pair
for i in range(m):
    a, b = map(int, stdin.readline().split())
    print(LCA(a,b))

