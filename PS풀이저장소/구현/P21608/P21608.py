#P21608 상어 초등학교
from sys import stdin

stdin = open('./input.txt', 'r')

n = int(stdin.readline())
a = [[] for _ in range(n*n+1)]
board = [[0]*n for _ in range(n)]
seq = []
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

for i in range(1, n*n + 1):
  x = list(map(int, stdin.readline().split()))
  idx = x[0]
  a[idx].extend(x[1:])
  seq.append(idx)

def calculate_result():
  global n
  result = 0
  for x in range(n):
    for y in range(n):
      score = 0
      for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
          continue
        if board[nx][ny] in a[board[x][y]]:
          score += 1
      if score == 0:
        continue
      result += (10 ** (score-1))
  return result

def place_student():
  global n
  for s in seq:
    possible_case = []
    for x in range(n):
      for y in range(n):
        p, q = 0, 0
        if board[x][y]:
          continue
        for k in range(4):
          nx = x + dx[k]
          ny = y + dy[k]
          if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
          if board[nx][ny] == 0:
            q += 1
          if board[nx][ny] in a[s]:
            p += 1
        possible_case.append((p, q, x, y))
    possible_case.sort(key = lambda x: (-x[0], -x[1], x[2], x[3]))
    rx, ry = possible_case[0][2], possible_case[0][3]
    board[rx][ry] = s

place_student()
print(calculate_result())