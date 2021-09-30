from sys import stdin

stdin = open('./input.txt', 'r')

n = int(stdin.readline())

#행성들의 위치
planet_pos = []

#행성들 사이의 거리
edges = []

for i in range(1, n+1):
    planet_pos.append(tuple(map(int, stdin.readline().split())) + (i,))

#부모 테이블
parent = [i for i in range(n+1)]

#x좌표로 오름차순 정렬 후, x좌표 상 바로 옆에 있는 행성간의 거리를 edges에 저장
planet_pos.sort(key = lambda x: x[0])
for i in range(n-1):
    edges.append((min(abs(planet_pos[i][0] - planet_pos[i+1][0]), abs(planet_pos[i][1] - planet_pos[i+1][1]), abs(planet_pos[i][2] - planet_pos[i+1][2])), planet_pos[i][3], planet_pos[i+1][3]))

#y좌표로 오름차순 정렬 후, y좌표 상 바로 옆에 있는 행성간의 거리를 edges에 저장
planet_pos.sort(key = lambda x: x[1])
for i in range(n-1):
    edges.append((min(abs(planet_pos[i][0] - planet_pos[i+1][0]), abs(planet_pos[i][1] - planet_pos[i+1][1]), abs(planet_pos[i][2] - planet_pos[i+1][2])), planet_pos[i][3], planet_pos[i+1][3]))

#z좌표로 오름차순 정렬 후, z좌표 상 바로 옆에 있는 행성간의 거리를 edges에 저장
planet_pos.sort(key = lambda x: x[2])
for i in range(n-1):
    edges.append((min(abs(planet_pos[i][0] - planet_pos[i+1][0]), abs(planet_pos[i][1] - planet_pos[i+1][1]), abs(planet_pos[i][2] - planet_pos[i+1][2])), planet_pos[i][3], planet_pos[i+1][3]))


#비용이 적은 순으로 정렬
edges.sort()

# print(edges)

#부모 노드를 찾는 함수
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

#부모를 합치는 함수
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

min_cost = 0

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        min_cost += cost
print(min_cost)