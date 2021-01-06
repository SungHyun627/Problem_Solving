from sys import stdin

stdin = open('./input.txt', 'r')

# 지도 세로 크기, 가로 크기, 주사위를 놓는 좌표, 명령의 개수
n, m, x, y, k = map(int, stdin.readline().rstrip().split())

# D : 바닥을 가리키는 주사위의 면, E : 동쪽을 가리키는 주사위의 면, S : 남쪽을 가리키는 주사위의 면
# 초기 주사위 상태 => D : 6, E : 3, S : 5
dice_state = {'D': 6, 'E': 3, 'S': 5}

# 각 주사위 면에 적힌 값
dice_value = [0] * 7

# 주사위의 동, 서, 북, 남 방향 정의
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 지도의 각 칸에 쓰여져 있는 수 입력
map_number = [list(map(int, stdin.readline().rstrip().split())) for _ in range(n)]

# 명령 리스트
order_list = list(map(int, stdin.readline().rstrip().split()))

# 주사위의 상태를 refresh 해주는 함수
def refresh_dice(order):
    global dice_state
    value1 = dice_state['D']
    value2 = dice_state['E']
    value3 = dice_state['S']
    # 동
    if order == 1:
        dice_state['E'] = 7 - value1
        dice_state['D'] = value2
    # 서
    elif order == 2:
        dice_state['E'] = value1
        dice_state['D'] = 7 - value2
    # 북
    elif order == 3:
        dice_state['S'] = value1
        dice_state['D'] = 7 - value3
    # 남
    else:
        dice_state['S'] = 7 - value1
        dice_state['D'] = value3


for i in order_list:
    # 주사위 이동
    nx = x + dx[i-1]
    ny = y + dy[i-1]
    # 지도의 범위를 벗어난 경우, 명령 무시
    if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
    # 이동
    x = nx
    y = ny
    # 주사위 상태 refresh
    refresh_dice(i)
    # 해당 위치의 지도에 기입되어 있는 숫자 확인
    if map_number[x][y] == 0:
        map_number[x][y] = dice_value[dice_state['D']]
    else:
        dice_value[dice_state['D']] = map_number[x][y]
        map_number[x][y] = 0
    # print(dice_value)
    print(dice_value[7 - dice_state['D']])