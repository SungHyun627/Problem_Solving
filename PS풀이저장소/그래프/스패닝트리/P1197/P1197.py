from sys import stdin
from sys import setrecursionlimit

setrecursionlimit(10**6)

stdin = open('./input.txt', 'r')

# v : 정점 개수, e : 간선 개수
v, e = map(int, stdin.readline().split())

# 각 node의 parent node를 찾는 함수
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    if x > y:
        parent[x] = y
    else:
        parent[y] = x

# 부모 테이블
parent = [i for i in range(v+1)]
# 간선 테이블
edge = []
# MST의 가중치
result = 0

# 간선 비용 입력
for _ in range(e):
    a, b, c = map(int, stdin.readline().split())
    # 비용을 기준으로 오름차순 하기위해 비용, 두 정점 순으로 리스트에 저장
    edge.append((c, a, b))

# 오름차순 정렬
edge.sort()

for i in edge:
    cost, node1, node2= i
    if find_parent(parent, node1) == find_parent(parent, node2):
        continue
    union(parent, node1, node2)
    result += cost

print(result)