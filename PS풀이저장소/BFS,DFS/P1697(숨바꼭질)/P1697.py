from sys import stdin
from collections import deque

stdin = open('./input.txt', 'r')

n, k = map(int, stdin.readline().split())

queue = deque()
time = 0
queue.append((n, time))

def bfs():
    visited = [False] * 200001
    visited[n] = True
    if n == k:
        return 0
    while queue:
        x, t = queue.popleft()
        nx_list = [2 * x, x + 1, x -1]

        for nx in nx_list:
            if nx < 0 or nx >= 200000:
                continue
            if not visited[nx]:
                if nx == k:
                    return(t + 1)
                    break
                else:
                    queue.append((nx, t+1))
                    visited[nx] = True
print(bfs())