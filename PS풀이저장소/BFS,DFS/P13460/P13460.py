from sys import stdin
from collections import deque

stdin = open('./input.txt', 'r')
n, m = map(int, stdin.readline().rstrip().split())
graph = [list(stdin.readline().rstrip()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'R':
            init_rx, init_ry = i, j
        elif graph[i][j] == 'B':
            init_bx, init_by = i, j
        else:
            pass

#기울이는 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def move(x, y, dx, dy):
    #이동한 횟수
    count = 0
    #다음 이동할 곳이 벽이거나, 현재 위치가 구멍일 경우 반복문 종료
    while graph[x + dx][y + dy] != '#' and graph[x][y] != 'O':
        x += dx
        y += dy
        count += 1
    return x, y, count


def bfs():
    visited = {}
    queue = deque()
    visited[init_rx, init_ry, init_bx, init_by] = True
    queue.append([init_rx, init_ry, init_bx, init_by, 1])

    while queue:
        rx, ry, bx, by, move_number = queue.popleft()
        if move_number > 10:
            break

        for i in range(4):
            nrx, nry, r_count = move(rx, ry, dx[i], dy[i])
            nbx, nby, b_count = move(bx, by, dx[i], dy[i])

            #파란색 구슬이 구멍에 들어간 경우
            if graph[nbx][nby] == "O":
                continue

            #빨간색 구슬이 구멍에 들어간 경우
            if graph[nrx][nry] == "O":
                return move_number
            
            #빨간색 구슬과 파란색 구슬의 위치가 동일한 경우
            if nrx == nbx and nry == nby:
                #더 많이 이동한 구슬을 한 칸 뒤로 뺀다
                if r_count > b_count:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]
            
            #방문 여부 확인
            if not (nrx, nry, nbx, nby) in visited:
                visited[nrx, nry, nbx, nby] = True
                queue.append([nrx, nry, nbx, nby, move_number + 1])
        
    #움직힌 횟수가 10회가 넘었거나, 'O'까지 경로가 없을 때
    return -1

print(bfs())