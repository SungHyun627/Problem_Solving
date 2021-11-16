#P11725 트리의 부모 찾기
from sys import stdin
from collections import deque

stdin = open('./input.txt', 'r')

n = int(stdin.readline())
parent = [0] * (n+1)
parent[1] = 1
nodes = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, stdin.readline().split())
    nodes[a].append(b)
    nodes[b].append(a)

queue = deque()
queue.append(1)

while queue:
    x = queue.popleft()
    for node in nodes[x]:
        if parent[node] == 0:
            parent[node] = x
            queue.append(node)
print(*parent[2:], sep='\n')

