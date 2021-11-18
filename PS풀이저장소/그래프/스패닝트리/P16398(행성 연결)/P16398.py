# P16398 행성 연결
from sys import stdin
from collections import deque

stdin = open('./input.txt', 'r')

# n : 행성의 수
n = int(stdin.readline())

#부모 테이블
parent = [i for i in range(n+1)]

# 행성 사이를 있는 edge들의 집합
edges = []
#최소 비용
result = 0

for i in range(1, n+1):
    a = list(map(int, stdin.readline().split()))
    for j in range(i, n):
        edges.append((a[j], i, j+1))

# 비용 오름차순으로 정렬
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
    cost, x, y  = edge
    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        result += cost
print(result)