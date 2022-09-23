from collections import deque

def solution(board):
    INF = 25 * 25 * 500
    n = len(board)
    cost_board = [[[INF] * 4 for _ in range(n)] for _ in range(n)]
    
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    
    q = deque([])
    q.append((0, 0, 1))
    q.append((0, 0, 2))
    cost_board[0][0][0], cost_board[0][0][1] = 0, 0
    cost_board[0][0][2], cost_board[0][0][3] = 0, 0
    
    while q:
        x, y, d = q.popleft()
        #print(q, cost_board[x][y])
        
        for k in range(4):
            #정반대 방향
            if (k + 2) % 4 == d:
                continue
                
            nx = x + dx[k]
            ny = y + dy[k]
            
            #범위를 벗어난 경우
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            
            #벽인 경우
            if board[nx][ny]:
                continue
                
            #추가 도로건설 비용
            add_cost = 100
            
            if k != d:
                add_cost = 600
            if cost_board[nx][ny][k] > (cost_board[x][y][d] + add_cost):
                q.append((nx, ny, k))
                cost_board[nx][ny][k] = cost_board[x][y][d] + add_cost
    #print(cost_board)
    return min(cost_board[n-1][n-1])