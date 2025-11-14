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


import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

# LOG: 부모 테이블의 최대 깊이(2^LOG > n)
LOG = 17  # 예: n <= 100000이면 2^17 = 131072 > 100000

n = int(input())                # 노드 수
graph = [[] for _ in range(n+1)]  # 1-indexed 인접 리스트

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# parent[k][v] = v에서 2^k 만큼 위로 올라간 노드 (없으면 0)
parent = [[0] * (n+1) for _ in range(LOG)]
depth = [0] * (n+1)
visited = [False] * (n+1)

def dfs(x, d):
    visited[x] = True
    depth[x] = d
    for nx in graph[x]:
        if not visited[nx]:
            parent[0][nx] = x  # nx의 바로 위 부모 저장 (2^0 = 1)
            dfs(nx, d+1)

# 루트가 1일 때
dfs(1, 0)

# Binary Lifting 테이블 생성
for k in range(1, LOG):
    for v in range(1, n+1):
        parent[k][v] = parent[k-1][ parent[k-1][v] ]

def lca(a, b):
    # 1) depth 맞추기: 항상 a가 더 깊게 만든다
    if depth[a] < depth[b]:
        a, b = b, a

    diff = depth[a] - depth[b]
    # diff를 이진수로 분해하여 a를 한 번에 올린다
    for k in range(LOG):
        if diff & (1 << k):
            a = parent[k][a]

    # 2) 이미 같으면 LCA 찾음
    if a == b:
        return a

    # 3) 가장 높은 2^k부터 내려오며 서로 다른 부모를 찾아 함께 올린다
    for k in reversed(range(LOG)):
        if parent[k][a] != parent[k][b]:
            a = parent[k][a]
            b = parent[k][b]

    # 이제 a와 b는 서로 다른 노드이지만 바로 부모는 같다
    return parent[0][a]