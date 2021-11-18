# 최소 공통 조상(LCA)알고리즘
# 1. 모든 노드에 대하 깊이(depth) 계산
# 2. 최소 공통 조상을 찾을 두 노드 확인
# 2-1. 두 노드의 깊이가 동일하도록 거슬러 올라간다.
# 2-2. 이후 부모가 같아질 때까지 반복적으로 두 노드의 부모 방향으로 거슬러 올라간다.
# 3. 모든 LCA(a, b) 연산에 대하여 2번의 과정 반복

# 매 쿼리마다 거슬러 올라가기 때문에 O(n) => m개의 쿼리는 O(mn)

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

# 개선된 알고리즘, 세그먼트 트리를 이용해서 시간복잡도 개선 => O(mlogn)
LOG = 21
parent = [[0]*LOG for _ in range(n+1)]
# c와 d는 동일

def dfs(x, depth):
    c[x] = True
    d[x] = depth
    for y in graph[x]:
        if c[y]:
            continue
        parent[y][0] = x
        dfs(y, depth+1)

# 전체 부모 관계를 설정하는 함수
def set_parent():
    # 1이 루트노드
    dfs(1, 0)
    for i in range(1, LOG):
        for j in range(1, n+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]

# A와 B의 최소 공통 조상을 찾는 함수
def LCA(a, b):
    # b가 더 깊도록 설정
    if d[a] > d[b]:
        a, b  = b, a
    # 깊이가 동일하도록
    for i in range(LOG -1, -1, -1):
        if d[b]- d[a] >= (1 << i):
            b = parent[b][i]
    # 부모가 같아지도록
    if a == b:
        return a
    for i in range(LOG -1, -1, -1):
        # 조상을 향해 거슬러 올라가기
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    
    # 부모가 찾고자 하는 조상
    return parent[a][0]

set_parent()
m = int(stdin.readlien())

for i in range(m):
    a, b = map(int, stdin.readline().split())
    print(LCA(a,b))