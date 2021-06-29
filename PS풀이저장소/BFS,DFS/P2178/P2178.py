from sys import stdin
from collections import deque

stdin = open('./input.txt', 'r')

# 세로, 가로
n, m = map(int, stdin.readline().split())

# 미로
maze = [list(map(int, list(stdin.readline().rstrip()))) for _ in range(n)]

# 이동할 네 방향(동, 서, 남, 북)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 방문 리스트
visited = [[0] * m for _ in range(n)]

# 동, 서, 남, 북 방향
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def BFS(x, y):
    # 큐 생성
    queue = deque()
    # 시작점을 큐에 삽입
    queue.append((x, y))
    # 방문 체크
    visited[x][y] = 1

    # 큐가 완전히 비어있을 때까지 진행
    while queue:
        # 하나의 노드(좌표)를 pop
        x, y = queue.popleft()

        #네 방향에 대해 방문할 수 있는 노드(좌표)가 있는지 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로의 범위를 벗어난 경우 또는 이동할 수 없는 칸인 경우 제외
            if nx >= n or ny >=m or nx < 0 or ny < 0 or maze[nx][ny] == 0:
                continue

            # 방문한 기록이 있는지 확인
            if visited[nx][ny] == 1:
                continue
            else:
                maze[nx][ny] = maze[x][y] + 1
                # 방문
                queue.append((nx, ny))
                # 방문 체크
                visited[nx][ny] = 1
    return maze[n-1][m-1]

print(BFS(0, 0))