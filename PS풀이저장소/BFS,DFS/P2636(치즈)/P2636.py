from sys import stdin
from collections import deque

stdin = open('./input.txt', 'r')

#세로, 가로
n, m = map(int, stdin.readline().rstrip().split())

#판
board = [list(map(int, stdin.readline().rstrip().split())) for _ in range(n)]

#이동 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#치즈 조각 개수
cheeze_num = 1

#마지막 치즈 조각 개수
final_cheeze_num = 0

for i in range(1, n-1):
    for j in range(1, m-1):
        if board[i][j] == 1:
            final_cheeze_num += 1

#치즈가 없어질때까지 걸린 시간
hour = 0

#치즈 내부의 구멍 또는 치즈이면 : True, 아니면 : False
hole_inside = [[True] * m for _ in range(n)]
hole_inside[0][0] = False

def bfs(x, y):
    visited = [[False] * m for _ in range(n)]
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if board[nx][ny] == 1:
                continue
            else:
                if not visited[nx][ny]:
                    hole_inside[nx][ny] = False
                    visited[nx][ny] = True
                    queue.append((nx, ny))


while True:
    #0으로 초기화
    cheeze_num = 0
    bfs(0,0)
    for i in range(1, n-1):
        for j in range(1, m-1):
            the_end = False
            if board[i][j] == 1:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if hole_inside[nx][ny] == False:
                        board[i][j] = 0
                        the_end = True
                        break
                if the_end:
                    continue
                cheeze_num += 1
    hour += 1
    if not cheeze_num:
        break
    final_cheeze_num = cheeze_num
    
print(hour, final_cheeze_num, sep ='\n')