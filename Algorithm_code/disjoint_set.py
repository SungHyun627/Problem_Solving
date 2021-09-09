from sys import stdin

# 서로소 자료구조
# O(V + MlogV)
# 사이클 판별에 사용(무향 그래프에서 사용)
"""
1. find_parent, union 함수 작성
2. 부모테이블 생성 및 초기화
3. 
"""
# n: 노드의 개수, m : edge의 개수
stdin = open('./input.txt', 'r')

n, m = map(int, stdin.readline().rstrip().split())

parent = [0] * (n+1)

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

# parent table 초기화
for i in range(1, n+1):
    parent[i] = i

# 각각의 간선에 대해 find, union 연산
cycle = False

for _ in range(m):
    x, y = map(int, stdin.readline().rstrip().split())
    if find_parent(parent, x) == find_parent(parent, y):
        cycle = True
        break
    else:
        union(parent, x, y)

print("cycle 발생") if cycle else print("cycle 없음")

