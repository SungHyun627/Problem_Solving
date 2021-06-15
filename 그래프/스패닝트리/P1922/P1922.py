from sys import stdin

stdin = open('input.txt', 'r')
n = int(stdin.readline().rstrip())
m = int(stdin.readline().rstrip())

# 크루스칼 알고리즘 구현

edges = []
for _ in range(m):
    a, b, cost = map(int, stdin.readline().rstrip().split())
    edges.append((cost, a, b))
# 비용이 적은 순으로 sort
edges.sort()

# parent table 초기화
parent = [i for i in range(n+1)]

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

# 최종 비용
result = 0

# 그래프가 생성되지 않는 간선을 비용이 적print(find_parent(parent, a), find_parent(parent, a))은 순서대로 추가
for edge in edges:
    cost, a, b = edge
    # 
    if find_parent(parent, a) == find_parent(parent, b):
        continue
    union_parent(parent, a, b)
    result += cost

print(result)