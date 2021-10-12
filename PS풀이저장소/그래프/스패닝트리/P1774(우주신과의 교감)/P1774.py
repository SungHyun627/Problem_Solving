from sys import stdin

stdin = open('./input.txt', 'r')
n, m = map(int, stdin.readline().split())

positions = [0]
for _ in range(n):
    a, b = map(int, stdin.readline().split())
    positions.append((a, b))

#부모 테이블
parent = [i for i in range(n+1)]

#두 지점의 좌표, 비용
edges = []
for i in range(1, n+1):
    for j in range(i+1, n+1):
        cost = ((positions[i][0] - positions[j][0]) ** 2 + (positions[i][1] - positions[j][1]) ** 2) ** 0.5
        edges.append((cost, i, j))
#비용 오름차순으로 정렬
edges.sort()
# print(edges)

#총 비용
total_cost = 0

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

#이미 연결된 간선들에 대한 비용
for _ in range(m):
    x, y = map(int, stdin.readline().split())
    union_parent(parent, x, y)

for cost, a, b in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        total_cost += cost
        union_parent(parent, a, b)

print('{0:.2f}'.format(total_cost))