from sys import stdin
from collections import deque

#topology sort + dp
stdin = open('./input.txt', 'r')

def topology_sort():
    dp = [0] * (n+1)
    queue = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            dp[i] = time[i]
            queue.append(i)

    while queue:
        idx = queue.popleft()
        for i in edges[idx]:
            indegree[i] -= 1
            dp[i] = max(dp[i], dp[idx] + time[i])
            if indegree[i] == 0:
                queue.append(i)
    return dp[target]


t = int(stdin.readline())

for _ in range(t):
    n, k = map(int, stdin.readline().split())
    
    #진입 차수
    indegree = [0] * (n+1)
    #건설 시간
    time = [0] + list(map(int, stdin.readline().split()))
    #간선 
    edges = [[] for _ in range(n+1)]

    for _ in range(k):
        a, b = map(int, stdin.readline().split())
        edges[a].append(b)
        indegree[b] += 1
    target = int(stdin.readline())
    # print(time, edges)
    print(topology_sort())