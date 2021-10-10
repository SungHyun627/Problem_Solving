from sys import stdin
from collections import deque

stdin = open('./input.txt', 'r')

#보드의 크기
n = int(stdin.readline())

#board
board = [[0] * n for _ in range(n)]

#사과의 개수
apple_num = int(stdin.readline())

for _ in range(apple_num):
    x, y = map(int, stdin.readline().split())
    board[x-1][y-1] = 1

#방향전환 횟수
change_dir_num = int(stdin.readline())
change_dir = dict()

for _ in range(change_dir_num):
    time, dir = stdin.readline().split()
    change_dir[int(time)] = dir

#방향
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs():
    count = 0
    dir = 0
    queue1 = deque()
    queue2 = deque()
    visited = [[False] * n for _ in range(n)]
    queue1.append((0, 0))
    visited[0][0] = True

    while queue1:
        x, y = queue1.popleft()
        queue2.append((x, y))

        if count in change_dir:
            if change_dir[count] == 'L':
                dir = (dir - 1) % 4
            else:
                dir = (dir + 1) % 4
        nx = x + dx[dir]
        ny = y + dy[dir]
        
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            return count + 1
        if visited[nx][ny]:
            return count + 1
        
        if board[nx][ny] == 1:
            board[nx][ny] = 0
            queue1.append((nx, ny))
            visited[nx][ny] = True
        else:
            x, y = queue2.popleft()
            visited[x][y] = False
            queue1.append((nx, ny))
            visited[nx][ny] = True
        count += 1
        # print(board)
print(bfs())