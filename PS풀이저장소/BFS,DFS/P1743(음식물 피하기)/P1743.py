#P1743 음식물 피하기
from sys import stdin
from collections import deque
stdin = open('./input.txt', 'r')

# 세로, 가로, 음식물 쓰레기 수
n, m, k = map(int, stdin.readline().split())
# 통로
board = [[0] * m for _ in range(n)]
# 가장 큰 쓰레기
biggest_trash_size = 0
# 방향리스트
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for _ in range(k):
  r, c = map(int, stdin.readline().split())
  board[r-1][c-1] = 1

for i in range(n):
  for j in range(m):
    if board[i][j]:
      queue = deque()
      board[i][j] = 0
      temp_size = 1
      queue.append((i, j))

      while queue:
        x, y = queue.popleft()
        for t in range(4):
          nx = x + dx[t]
          ny = y + dy[t]

          if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue

          if board[nx][ny]:
            board[nx][ny] = 0
            temp_size += 1
            queue.append((nx, ny))
        
        biggest_trash_size = max(biggest_trash_size, temp_size)

print(biggest_trash_size)
