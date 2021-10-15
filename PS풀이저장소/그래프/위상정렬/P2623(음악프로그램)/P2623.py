from sys import stdin
from collections import deque

stdin = open('./input.txt', 'r')
n, m = map(int, stdin.readline().split())

edges = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for _ in range(m):
    arr = list(map(int, stdin.readline().split()))
    if not arr[0]:
        continue
    for i in range(1, arr[0]):
        if arr[i+1] not in edges[arr[i]]:
            edges[arr[i]].append(arr[i+1])
            indegree[arr[i+1]] += 1

# print(edges, indegree)

def make_sequence():
    result = []
    queue = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            queue.append(i)
            result.append(i)
    
    while queue:
        idx = queue.popleft()
        for i in edges[idx]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)
                result.append(i)
    # print(indegree)
    if len(result) != n:
        return 0
    else:
        return '\n'.join(map(str, result))

print(make_sequence())