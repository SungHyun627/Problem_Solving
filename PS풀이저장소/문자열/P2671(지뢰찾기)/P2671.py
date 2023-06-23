#P2671 지뢰찾기
from sys import stdin

stdin = open('./input.txt', 'r')

dx, dy = [0, 0, -1, 1, -1, -1, 1, 1], [-1, 1, 0, 0, -1, 1, -1, 1]

n = int(stdin.readline())
a = [list(stdin.readline().rstrip()) for _ in range(n)]
b = [list(stdin.readline().rstrip()) for _ in range(n)]
isFail = False
result = [['.'] * n for _ in range(n)]
bombs = []

for i in range(n):
  for j in range(n):
    t = 0
    if b[i][j] == '.':
      if a[i][j] == '*':
        bombs.append((i, j))
      continue
    if a[i][j] == '*':
      bombs.append((i, j))
      isFail = True
      continue
    else:
      for k in range(8):
        nx = i + dx[k]
        ny = j + dy[k]
        if nx >= n or ny >= n or nx < 0 or ny < 0:
          continue
        if a[nx][ny] == '*':
          t += 1
      result[i][j] = str(t)

if isFail:
  for bomb in bombs:
    x, y = bomb
    result[x][y] = '*'
for i in range(n):
  print(''.join(result[i]))