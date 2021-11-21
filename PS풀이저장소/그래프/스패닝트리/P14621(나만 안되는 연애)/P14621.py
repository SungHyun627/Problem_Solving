#P14621 나만 안되는 연애
from sys import stdin

stdin = open('./input.txt', 'r')

n, m = map(int, stdin.readline().split())
school_type = [0] + list(stdin.readline().split())
result = 0

# 부모테이블
parent = [i for i in range(n+1)]

edges = []

for _ in range(m):
    a, b, cost = map(int, stdin.readline().split())
    if school_type[a] != school_type[b]:
        edges.append((cost, a, b))
edges.sort()

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

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

for i in range(1, n+1):
    find_parent(parent, i)

print(result) if parent.count(1) == n else print(-1)