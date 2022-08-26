from collections import deque

def solution(maps):
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    q = deque([])
    
    n, m = len(maps), len(maps[0])
    
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    q.append((0, 0, 1))
    
    while q:
        x, y, cnt = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if not maps[nx][ny]:
                continue
            if visited[nx][ny]:
                continue
            if nx == n-1 and ny == m-1:
                return cnt + 1
            visited[nx][ny] = True
            q.append((nx, ny, cnt+1))
            
    return -1