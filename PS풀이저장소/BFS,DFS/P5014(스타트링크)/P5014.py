#P5014 스타트링크
from sys import stdin
from collections import deque

stdin = open('./input.txt', 'r')

f, s, g, u, d = map(int, stdin.readline().split())
visited = [False] * (f+1)
dh = [u, -d]

def bfs():
    if s == g:
        return 0
    queue = deque()
    queue.append((s, 0))
    visited[s] = True

    while queue:
        # print(queue)
        h, count = queue.popleft()
        for i in range(2):
            nh = h + dh[i]
            if nh <= 0 or nh > f:
                continue
            if visited[nh]:
                continue
            
            if nh == g:
                return count + 1
            queue.append((nh, count + 1))
            visited[nh] = True
    return "use the stairs"

print(bfs())