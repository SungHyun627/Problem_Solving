#P17352 여러분의 다리가 되어 드리겠습니다!
from sys import stdin
stdin = open('./input.txt', 'r')
n = int(stdin.readline())

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

parent = [i for i in range(n+1)]

while True:
    t = stdin.readline()
    if not t:
        break
    a, b = map(int, t.split())
    union_parent(parent, a, b)

for i in range(1, n+1):
    find_parent(parent, i)

print(*set(parent[1:]))
