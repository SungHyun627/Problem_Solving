from sys import stdin
import heapq
stdin = open('./input.txt', 'r')

m, n = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().rstrip())) for _ in range(n)]

dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

def bfs():
    #칸이 1개 뿐일 때
    if n == 1 and m == 1:
        return 0
    
    #방문 배열 
    visited = [[False] * m for _ in range(n)]
    q = []
    visited[0][0] = True
    heapq.heappush(q, (0, (0, 0)))
    
    while q:
        count, pos = heapq.heappop(q)
        x, y = pos
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >=n or ny >= m:
                continue
            if not visited[nx][ny]:
                if graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    heapq.heappush(q, (count + 1, (nx, ny)))
                else:
                    if nx == n-1 and ny == m-1:
                        return count
                    else:
                        visited[nx][ny] = True
                        heapq.heappush(q, (count, (nx, ny)))               

print(bfs())