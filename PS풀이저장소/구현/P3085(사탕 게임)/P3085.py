#P3085 사탕 게임
from sys import stdin 

stdin = open('./input.txt', 'r')
n = int(stdin.readline())
board = [list(stdin.readline().rstrip()) for _ in range(n)]
result = 0
cases = []

def calculate_candy():
  max_eating_candy = 0
  for i in range(n):
    temp1, prev_char = 1, board[i][0]
    for j in range(1, n):
      if prev_char == board[i][j]:
        temp1 += 1
      else:
        prev_char = board[i][j]
        max_eating_candy = max(max_eating_candy, temp1)
        temp1 = 1
    max_eating_candy = max(max_eating_candy, temp1)
  for j in range(n):
    temp2, prev_char = 1, board[0][j]
    for i in range(1, n):
      if prev_char == board[i][j]:
        temp2 += 1
      else:
        prev_char = board[i][j]
        max_eating_candy = max(max_eating_candy, temp2)
        temp2 = 1
    max_eating_candy = max(max_eating_candy, temp2)
  return max_eating_candy

for i in range(n):
  for j in range(n):
    cases.append((i, j))

for case in cases:
  x, y = case
  if y + 1 < n:
    board[x][y], board[x][y+1] = board[x][y+1], board[x][y]
    result = max(result, calculate_candy())
    board[x][y], board[x][y+1] = board[x][y+1], board[x][y]
  if x + 1 < n:
    board[x][y], board[x+1][y] = board[x+1][y], board[x][y]
    result = max(result, calculate_candy())
    board[x][y], board[x+1][y] = board[x+1][y], board[x][y]
print(result)