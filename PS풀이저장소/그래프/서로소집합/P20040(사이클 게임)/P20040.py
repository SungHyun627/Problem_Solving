from sys import stdin

stdin = open('./input.txt', 'r')

#n: 점의 수, m: 진행된 차례 수
n, m = map(int, stdin.readline().split())

parent = [i for i in range(n+1)]

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

for i in range(1, m+1):
    a, b = map(int, stdin.readline().split())
    if find_parent(parent, a) == find_parent(parent, b):
        print(i)
        break
    else:
        union_parent(parent, a, b)
    
    if i == m:
        print(0)