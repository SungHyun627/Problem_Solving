from sys import stdin
from collections import deque

##BFS로 풀이
##백트래킹 + DFS도 생각해볼 필요 있음

stdin = open('./input.txt', 'r')
n, m = map(int, stdin.readline().rstrip().split())
graph = [list(stdin.readline().rstrip()) for _ in range(n)]
cost_set = set()
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def have_alphabet(k, x):
    if (k & (1 << x)):
        return True
    else:
        return False

def BFS():
    bitmask = 0
    count = 1
    queue = deque()
    bitmask = (bitmask | (1 << (ord(graph[0][0]) - ord('A'))))
    queue.append((0, 0, bitmask, count))
    cost_set.add((0, 0, bitmask, count))

    while queue:
        # print(queue)
        x, y, mask, count = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or ny >= m or nx < 0 or ny < 0:
                continue
            if have_alphabet(mask, ord(graph[nx][ny]) - ord('A')):
                continue
            else:
                new_mask = (mask | (1 << (ord(graph[nx][ny]) - ord('A'))))
                if (nx, ny, new_mask, count+1) not in cost_set:                    
                    cost_set.add((nx, ny, new_mask, count+1))
                    queue.append((nx, ny, new_mask, count+1))
    print(count)
BFS()