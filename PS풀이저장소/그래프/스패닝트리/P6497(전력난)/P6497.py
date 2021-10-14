from sys import stdin
from collections import deque

stdin = open('./input.txt', 'r')

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(a, b, parent):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

def cal_cost(m, edges, total_cost):

    #필요한 최소 비용
    required_cost = 0

    #부모테이블
    parent = [i for i in range(m)] 

    #비용 작은 순으로 정렬
    edges.sort()

    for edge in edges:
        cost, x, y = edge
        if find_parent(parent, x) != find_parent(parent, y):
            required_cost += cost
            union_parent(x, y, parent)
    return (total_cost - required_cost)

while(True):
    m, n = map(int, stdin.readline().split())
    if m == 0 and n == 0:
        break
    edges = []
    #모든 불을 켜는데 드는 비용
    total_cost = 0
    for _ in range(n):
        a, b, cost = map(int, stdin.readline().split())
        edges.append((cost, a, b))
        edges.append((cost, b, a))
        total_cost += cost
    print(cal_cost(m, edges, total_cost))
