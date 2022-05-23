#P15683 감시
#카메라 위치, 종류, 상태 고려하여 사각지대 최소 크기 구하기
from sys import stdin
from itertools import product
stdin = open('./input.txt')
n, m = map(int, stdin.readline().split())

#방향 벡터(인덱스 0: 북, 1: 동, 2: 남, 3: 서)
#4(1), 2(2), 4(2), 4(3), 1(4)
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

graph = [list(map(int, stdin.readline().split())) for _ in range(n)]

def calculate_not_monitor(board, case, pos, num):
  # print(case, pos)
  can_monitor = 0
  for i in range(num):
    x, y = pos[i]
    for j in case[i]:
      nx, ny = x, y
      while True:
        nx += dx[j]
        ny += dy[j]
        # 범위를 벗어날 때
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
          break
        # 해당 부분이 벽일 때
        if board[nx][ny] == 6:
          break
        if not board[nx][ny]:
          board[nx][ny] = '#'
  
  for i in range(n):
    can_monitor += board[i].count('#')
  # for i in range(n):
  #   print(board[i])
  return n*m - can_monitor



  return 1

def solve():
  camera_pos = []
  camera_cases = []
  camera_num = 0
  wall_num = 0
  result = n * m
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 6:
        wall_num += 1
        continue
      if not graph[i][j]:
        continue
      elif graph[i][j] == 1:
        camera_cases.append([[0], [1], [2], [3]])
      elif graph[i][j] == 2:
        camera_cases.append([(0, 2), (1, 3)])
      elif graph[i][j] == 3:
        camera_cases.append([(0, 1), (1, 2), (2, 3), (3, 0)])
      elif graph[i][j] == 4:
        camera_cases.append([(0, 1, 2), (1, 2, 3), (2, 3, 0), (3, 0, 1)])
      else:
        camera_cases.append([(0, 1, 2, 3)])
      camera_pos.append((i, j))
      camera_num += 1

  for case in list(product(*camera_cases)):
    board = [[0] * m for _ in range(n)]
    for i in range(n):
      for j in range(m):
        board[i][j] = graph[i][j]
    result = min(calculate_not_monitor(board, case, camera_pos, camera_num), result)

  return result - wall_num - camera_num
      
  
print(solve())