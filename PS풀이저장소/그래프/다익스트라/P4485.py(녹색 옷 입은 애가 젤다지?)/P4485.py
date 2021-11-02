#P4485 녹색 옷 입은 애가 젤다지?
from sys import stdin
import heapq

stdin = open('./input.txt', 'r')

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

def dijkstra(graph, n):
    if n == 1:
        return graph[0][0]
    q = []
    visited = [[False] * n for _ in range(n)]
    visited[0][0] = True
    heapq.heappush(q, (graph[0][0], (0, 0)))

    while q:
        luffy, pos = heapq.heappop(q)
        x, y = pos
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or ny >= n or nx < 0 or ny < 0:
                continue
            if not visited[nx][ny]:
                if nx == n-1 and ny == n-1:
                    return luffy + graph[n-1][n-1]
                else:
                    visited[nx][ny] = True
                    heapq.heappush(q, (luffy + graph[nx][ny], (nx, ny)))

test_num = 1
while True:
    #그래프 세로, 가로 크기
    n = int(stdin.readline().rstrip())
    
    if n == 0:
        break

    graph = [list(map(int, stdin.readline().split())) for _ in range(n)]
    print("Problem {0}: {1}".format(test_num, dijkstra(graph, n)))
    test_num += 1