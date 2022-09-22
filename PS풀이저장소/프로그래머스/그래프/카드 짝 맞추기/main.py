from collections import deque
from itertools import permutations

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

def out_of_boundary(x, y):
  return x < 0 or y < 0 or x >= 4 or y >= 4

def bfs(start, dest, n_board):
  visited = [[-1] * 4 for _ in range(4)]
  q = deque([])
  q.append(start)
  visited[start[0]][start[1]] = 0
  while q:
    x, y = q.popleft()
    for k in range(4):
        jump = 0
        while True:
          nx = x + dx[k] * (jump+1)
          ny = y + dy[k] * (jump+1)
          if out_of_boundary(nx, ny):
            break
          jump += 1
          if n_board[nx][ny]:
            break
        for t in (1, jump):
          nx = x + dx[k] * t
          ny = y + dy[k] * t
          if out_of_boundary(nx, ny):
              continue
          if visited[nx][ny] == -1:
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))
  return visited[dest[0]][dest[1]]
        

def solution(board, r, c):    
    answer = int(1e9)
    card_pos = [[] for _ in range(7)]
    card_type = []
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                card_pos[board[i][j]].append((i, j))
    for i in range(7):
        if card_pos[i]: card_type.append(i)
    #카드 수            
    n = len(card_type)
    
    for p in permutations(card_type):
        new_board = [[0] * 4 for _ in range(4)]
        curx, cury = r, c
        for i in range(4):
            for j in range(4):
                new_board[i][j] = board[i][j]
        
        #dp
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = bfs((r, c), card_pos[p[0]][0], new_board) + bfs(card_pos[p[0]][0], card_pos[p[0]][1], new_board)
        dp[0][1] = bfs((r, c), card_pos[p[0]][1], new_board) + bfs(card_pos[p[0]][1], card_pos[p[0]][0], new_board)
        new_board[card_pos[p[0]][0][0]][card_pos[p[0]][0][1]] = 0
        new_board[card_pos[p[0]][1][0]][card_pos[p[0]][1][1]] = 0
        
        for i in range(1, n):
          dp[i][0] = min(dp[i-1][0] + bfs(card_pos[p[i-1]][1], card_pos[p[i]][0], new_board), dp[i-1][1] + bfs(card_pos[p[i-1]][0], card_pos[p[i]][0], new_board)) + bfs(card_pos[p[i]][0], card_pos[p[i]][1], new_board)
          dp[i][1] = min(dp[i-1][0] + bfs(card_pos[p[i-1]][1], card_pos[p[i]][1], new_board), dp[i-1][1] + bfs(card_pos[p[i-1]][0], card_pos[p[i]][1], new_board)) + bfs(card_pos[p[i]][1], card_pos[p[i]][0], new_board)
          new_board[card_pos[p[i]][0][0]][card_pos[p[i]][0][1]] = 0
          new_board[card_pos[p[i]][1][0]][card_pos[p[i]][1][1]] = 0
        answer = min(answer, *dp[n-1])
    return answer + 2 * n