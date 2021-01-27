from sys import stdin
from sys import setrecursionlimit

setrecursionlimit(10**6)

stdin = open('./input.txt', 'r')

# 특정 원소가 속한 집합(루트 노드) 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 집합 합치기
def union(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

# 집합 개수, 연산 개수 입력 받기
n, m = map(int, stdin.readline().split())

# 부모 테이블 생성 및 초기화
parent = [i for i in range(n+1)]

# 각각의 union 연산 실행
for _ in range(m):
    a, b, c = map(int, stdin.readline().split())

    # 연산자가 0일 때
    if a == 0:
        # 합집합 연산
        union(parent, b, c)
    else:
        print('yes') if find_parent(parent, b) == find_parent(parent, c) else print('no')