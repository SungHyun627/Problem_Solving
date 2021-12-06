#P1976 여행 가자
from sys import stdin
stdin = open('./input.txt', 'r')

n = int(stdin.readline())
m = int(stdin.readline())

parent = [i for i in range(n+1)]
edges = []

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

for i in range(1, n+1):
    a = list(map(int, stdin.readline().split()))
    for j in range(i, n):
        if a[j]:
            edges.append((i, j+1))

#번호가 작은 도시부터 union_parent하기 위해 sort
edges.sort()

for edge in edges:
    a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)

# parent 다시 한번 계산
for i in range(1, n+1):
    find_parent(parent, i)


route = list(map(int, stdin.readline().split()))
root_city = parent[min(route)]
is_possible = True

for i in range(m):
    if parent[route[i]] != root_city:
        is_possible = False
        break
print('YES') if is_possible else print('NO')