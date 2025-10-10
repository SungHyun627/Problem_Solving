inputs = [[3, 4, 2, 3, 3, 1, 5], [2, 2, 1, 1, 2, 2, 2], [3, 3, 1, 2, 3, 3, 4]]
from sys import setrecursionlimit

board = -1
ans = ''
sx, sy = -1, -1
ex, ey = -1, -1
bn, bm = -1, -1

setrecursionlimit(10**6)

# d, l, r, u
dx, dy = [1, 0, 0, -1], [0, -1, 1, 0]
dir = ['d', 'l', 'r', 'u']

def dfs(cx, cy, remain, path):
  global bn, bm, ans
  if ans != '':
    return
  if remain == 0:
    if cx != ex or cy != ey:
      return
    ans = path
    return

  dist = abs(cx-ex) + abs(cy-ey)  
  if dist > remain:
    return
  if (dist-remain) % 2 != 0:
    return

  for i in range(4):
    nx = cx + dx[i]
    ny = cy + dy[i]

    if nx < 0 or ny < 0 or nx >= bn or ny >= bm:
      continue

    dfs(nx, ny, remain-1, path + dir[i])
    if ans != '':
      return


def solution(n, m, x, y, r, c, k):
  global board, ans, sx, sy, ex, ey, bn, bm
  ans = ''
  bn, bm = n, m
  board = [['.'] * m for _ in range(n)]
  sx, sy, ex, ey = x-1, y-1, r-1, c-1
  board[sx][sy] = 'S'
  board[ex][ey] = 'E'

  dfs(sx, sy, k, '')
  return ans if ans != '' else "impossible"


for input in inputs:
  print(solution(*input))