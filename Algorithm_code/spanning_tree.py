from sys import stdin
stdin = open('./input.txt', 'r')

# 신장트리(스패닝 트리) : 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프
# 크루스칼 알고리즘 : 최소비용 신장트리 (그리디)
# 시간 복잡도 : O(ElogE)

"""
1. 간선 데이터비용 오름차순 정렬
2. 간선 하나씩 확인하여 사이클 발생 유무 확인
    - 사이클 미 발생시 union
    - 사이클 발생 시 트리에서 제외
3. 2번 과정 반복
"""

# n : 노드 수, m : 간선 수
n, m = map(int, stdin.readline().rstrip().split())
# 간선의 정보(비용, 두개의 노드)를 저장할 리스트
edges = []
# 각 노드의 root node를 저장할 table
parent = [0] * (n+1)

# 총 비용
result = 0

#초기화
for i in range(1, n+1):
    parent[i] = i

#간선 정보 입력
for _ in range(m):
    a, b, cost = map(int, stdin.readline().rstrip().split())
    edges.append((cost, a, b))

# 비용 오름차순으로 정렬
edges.sort() 

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    x = find_parent(parent, a) 
    y = find_parent(parent, b)
    if x > y:
        parent[x] = y 
    else:
        parent[y] = x

for edge in edges:
    cost, x, y = edge
    if find_parent(parent, x) == find_parent(parent, y):
        continue
    union(parent, x, y)
    result += cost

print(result)