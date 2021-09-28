from sys import stdin
from collections import deque

stdin = open('./input.txt', 'r')

#r, c
r, c = map(int, stdin.readline().split())
graph = [list(stdin.readline().rstrip()) for _ in range(r)]

#특정 시간에 불이 특정 위치에 도달하는 시간을 기록하기 위한 2차원 리스트
fire_move = [[-1] * c for _ in range(r)]
#특정 시간에 사람이 특정 위치에 도달하는 시간을 기록하기 위한 2차원 리스트
person_move = [[-1] * c for _ in range(r)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs():
    #불에 대한 queue
    queue1 = deque()
    #사람에 대한 queue
    queue2 = deque()

    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'F':
                queue1.append((i, j))
                fire_move[i][j] = 0

    while queue1:
        x, y = queue1.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #범위를 벗어난 경우
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue

            #벽인 경우
            if graph[nx][ny] == '#':
                continue

            #이미 불이 예전에 도달한 경로인 경우
            if fire_move[nx][ny] != -1:
                continue

            fire_move[nx][ny] = fire_move[x][y] + 1
            queue1.append((nx, ny))

    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'J':
                queue2.append((i, j))
                person_move[i][j] = 0

    while queue2:
        x, y = queue2.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #범위를 벗어난 경우  => 탈출 성공
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                print(person_move[x][y] + 1)
                return

            #벽인 경우
            if graph[nx][ny] == '#':
                continue

            #사람이 이미 도달한 경우
            if person_move[nx][ny] != -1:
                continue

            #불이 먼저 도달한 경우
            if (fire_move[nx][ny] != -1) and (fire_move[nx][ny] <= person_move[x][y] + 1):
                continue

            person_move[nx][ny] = person_move[x][y] + 1
            queue2.append((nx, ny))
    print("IMPOSSIBLE")

bfs()