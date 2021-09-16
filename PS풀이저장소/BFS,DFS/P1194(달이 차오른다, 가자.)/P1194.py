from sys import stdin
from collections import deque

##풀이 방법##
#BFS, a~f열쇠의 유무를 6개의 bitmask로 표시
#set 자료구조 활용하여 중복되는 경로 방지

stdin = open('./input.txt', 'r')
n, m = map(int, stdin.readline().rstrip().split())
graph = [list(stdin.readline().rstrip()) for _  in range(n)]
key_type = ['a', 'b', 'c', 'd', 'e', 'f']
lock_type = ['A', 'B', 'C', 'D', 'E', 'F']

for i in range(n):
    for j in range(m):
        if graph[i][j] == '0':
            startx, starty = i, j
            break

def isin(nx, ny):
    if nx >= 0 and nx < n and ny >=0 and ny < m:
        return True
    else:
        return False

def bfs():
    queue = deque()
    keys = 0
    count  = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    state = set()

    queue.append((startx, starty, keys, count))
    state.add((startx, starty, keys))

    while queue:
        # print(queue)
        x, y, keys, count = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (not isin(nx, ny)) or (graph[nx][ny] == '#'): 
                continue

            if graph[nx][ny] == '1':
                print(count + 1)
                # print(state)
                return

            elif graph[nx][ny] in key_type:
                idx = key_type.index(graph[nx][ny])
                nkeys = (keys | (1 << idx))
                if (nx, ny, nkeys) not in state:
                    state.add((nx, ny, nkeys))
                    queue.append((nx, ny, nkeys, count + 1))
                else:
                    continue

            elif graph[nx][ny] in lock_type:
                idx = lock_type.index(graph[nx][ny])
                if (keys & (1 << idx)):
                    if (nx, ny, keys) not in state:
                        state.add((nx, ny, keys))
                        queue.append((nx, ny, keys, count + 1))
                    else:
                        continue
                else:
                    continue
            else:
                if (nx, ny, keys) not in state:
                    state.add((nx, ny, keys))
                    queue.append((nx, ny, keys, count + 1))
                else:
                    continue
    print(-1)
bfs()
