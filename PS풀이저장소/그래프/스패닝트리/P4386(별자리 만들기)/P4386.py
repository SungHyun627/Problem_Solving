from sys import stdin

stdin = open('./input.txt', 'r')

n = int(stdin.readline())

#별들의 위치
star_pos = []

#별들 사이의 거리
distances = []

for _ in range(n):
    star_pos.append(tuple(map(float, stdin.readline().split())))

#부모 테이블
parent = [i for i in range(n+1)]

for i in range(n):
    for j in range(i+1, n):
        dist = ((star_pos[i][0] - star_pos[j][0]) ** 2 + (star_pos[i][1] - star_pos[j][1]) ** 2) ** 0.5
        distances.append((dist, i, j))

#거리가 짧은 순으로 정렬
distances.sort()

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

min_dist = 0

for distance in distances:
    dist, a, b = distance
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        min_dist += dist
print(f'{min_dist:.2f}')