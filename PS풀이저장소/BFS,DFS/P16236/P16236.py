from sys import stdin
from collections import deque

stdin = open('./input.txt', 'r')
n = int(stdin.readline())

#저장해야 할 값
#상어의 크기, 먹은 물고기의 수, 위치
# 1. 해당위치에 먹을 수 있는 물고기가 있나
# 2. 이동할 수 있는 곳이 있나
# 3. 최단거리인가 (위쪽, 왼쪽)

##Graph 입력
graph = [list(map(int, stdin.readline().rstrip().split())) for _ in range(n)]

#상어의 default 위치
shark_position_x, shark_position_y = 0, 0

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            shark_position_x, shark_position_y = i, j
            break
    if graph[shark_position_x][shark_position_y] == 9:
        graph[shark_position_x][shark_position_y] = 0
        break

#상어의 크기
shark_size = 2
#먹은 고기의 수
eating_amount = 0
#총 걸린 시간
time = 0

#4가지 방향(북, 서, 남, 동)
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def find_feed (startx, starty):
    distance_from_start = 0
    visited = [[False]*n for _ in range(n)]
    visited[startx][starty] = True
    feed_list = []
    #큐 생성
    queue = deque()
    #시작점을 큐에 삽입
    queue.append((startx, starty, distance_from_start))
    while queue:
        x, y, distance = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or ny >= n or nx < 0 or ny < 0:
                continue

            if (graph[nx][ny] == shark_size or graph[nx][ny] == 0) and not visited[nx][ny]:
                queue.append((nx, ny, distance + 1))
                visited[nx][ny] = True
            elif (graph[nx][ny] > shark_size):
                continue
            else:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    feed_list.append((nx, ny, distance + 1))
        # print(queue)
    # print(feed_list)

    if not feed_list:
        return False
    else:
        feed_list.sort(key=lambda x:(x[2], x[0], x[1]))
        return feed_list[0]
    
while True:
    # if iterate == 14:
    #     break
    a = find_feed(shark_position_x, shark_position_y) 
    # print(a)
    if not a:
        print(time)
        break
    eating_amount += 1
    if eating_amount == shark_size:
        shark_size += 1
        eating_amount = 0
    shark_position_x = a[0]
    shark_position_y = a[1]
    time += a[2]
    graph[shark_position_x][shark_position_y] = 0
    # iterate += 1
    # print(shark_position_x, shark_position_y, time, shark_size, eating_amount)    