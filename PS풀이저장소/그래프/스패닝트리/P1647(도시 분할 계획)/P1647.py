from sys import stdin

stdin = open('./input.txt', 'r')

#n: 집의 개수, m: 길의 개수

n, m = map(int, stdin.readline().split())

#두 도시를 잇는 길의 비용
cost_edges = []
#부모 테이블
parent = [0] * (n+1)

#부모 테이블 초기화
for i in range(1, n+1):
    parent[i] = i

for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    cost_edges.append((c, a, b))

#비용을 오름차순으로 정렬
cost_edges.sort()

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


#총 비용에 사용된 cost list
used_cost = []
#사용된 비용
result = 0

#총 비용 구하는 과정
for cost_edge in cost_edges:
    cost, a, b = cost_edge
    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        result += cost
        used_cost.append(cost)

used_cost.sort()
print(result - used_cost[-1])