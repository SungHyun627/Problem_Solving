from sys import stdin

stdin = open('./input.txt', 'r')

# 세로, 가로 길이
n, m = map(int, stdin.readline().rstrip().split())

# 로봇청소기가 청소한 영역을 표시하기 위한 리스트
clean_area = [[0]*m for _ in range(n)]

# 로봇이 움직이는 방향을 나타내는 리스트
# 북 : 0, 동 : 1, 남 : 2, 서 : 3
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 현재 로봇의 x, y 위치, 바라보는 방향
x, y, direction = map(int, stdin.readline().rstrip().split())
# 지도
map_list = [list(map(int, stdin.readline().rstrip().split())) for _ in range(n)]

# 현재 위치를 방문 처리
clean_area[x][y] = 1

# 로봇이 왼쪽방향으로 회전하는 함수
def turn_left():
    global direction
    direction -= 1
    if direction < 0:
        direction = 3

# 청소가능한 영역의 수
count = 1
# 왼쪽으로 회전한 횟수
turn_num = 0

# 시뮬레이션
while(1):
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]   
    ny = y + dy[direction]

    # 청소 가능한 영역일 경우
    if clean_area[nx][ny] == 0 and map_list[nx][ny] == 0:
        clean_area[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_num = 0
        continue
    # 청소 불가능한 영역일 경우
    else:
        turn_num += 1
    # 네 방향 모두 청소 불가능한 영역인 경우
    if turn_num == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤쪽방향이 벽이 아닌 경우
        if map_list[nx][ny] == 0:
            x = nx
            y = ny
            turn_num = 0
        # 뒤쪽방향이 벽인 경우
        else:
            break
print(count)