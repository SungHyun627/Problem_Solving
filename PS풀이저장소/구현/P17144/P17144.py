from sys import stdin
from copy import deepcopy

stdin = open('./input.txt', 'r')

# 방의 행, 열, 시간
r, c, t = map(int, stdin.readline().rstrip().split())

# 각 칸의 미세먼지 및 공기 청정기 위치
room_dust = [list(map(int, stdin.readline().rstrip().split())) for _ in range(r)]

# 위, 아래 공기 청정기 위치
for i in range(r):
    if room_dust[i][0] == - 1:
        u_air_cleaner_x = i
        d_air_cleaner_x = i + 1
        break

# 확산 전 각 칸의 미세먼지 양과 청정기의 위치
before_second_room = [[0] * c for _ in range(r)]
# 확산 후 각 칸의 미세먼지 양과 청정기의 위치
after_second_room = [[0] * c for _ in range(r)]

# 확산 후 / 공기 청정기 사용 전에 칸의 미세먼지 양을 계산하는 함수
def dust_amount_calculate(x, y):
    global before_second_room, r, c, u_air_cleaner_x, d_air_cleaner_x
    # 동, 서, 남, 북의 주위 칸에 대해 공기 청정기가 아니거나 벽이 아닌 경우를 count
    count = 0 
    # 먼지의 양
    dust_amount = 0
    # 북
    if x != 0 and not(x - 1 == d_air_cleaner_x and y == 0):
        dust_amount += before_second_room[x-1][y] // 5
        count += 1
    # 남
    if x != r-1 and not (x + 1 == u_air_cleaner_x and y == 0):
        dust_amount += before_second_room[x+1][y] // 5
        count += 1
    # 서
    if y != 0 and not(x == d_air_cleaner_x and y == 1) and not(x == u_air_cleaner_x and y == 1):
        dust_amount += before_second_room[x][y-1] // 5
        count += 1
    # 동
    if y != c-1:
        dust_amount += before_second_room[x][y+1] // 5
        count += 1
    # 특정 칸의 먼지의 양 = 기존에 있던 먼지의 양 + 들어온 먼지의 양 - 나간 먼지의 양
    dust_amount = dust_amount + before_second_room[x][y] - (before_second_room[x][y] // 5) * count
    return dust_amount

before_second_room = deepcopy(room_dust)

# 공기 청정기 위치 설정
after_second_room[d_air_cleaner_x][0] = -1
after_second_room[u_air_cleaner_x][0] = -1

for _ in range(t):
    # 확산
    for i in range(r):
        for j in range(c):
            if j == 0 and (i == u_air_cleaner_x or i == d_air_cleaner_x):
                continue
            after_second_room[i][j] = dust_amount_calculate(i, j)
    
    # 공기청정기 작동

    # 위쪽 공기 청정기

    # 공기 청정기 row
    upper_point_1 = after_second_room[u_air_cleaner_x].pop()
    after_second_room[u_air_cleaner_x].insert(1, 0)
    # 맨 오른쪽 column
    upper_point_2 = after_second_room[0].pop()
    for i in range(0, u_air_cleaner_x -1):
        after_second_room[i].append(after_second_room[i+1].pop())
    after_second_room[u_air_cleaner_x-1].append(upper_point_1)
    # 맨 상단 row
    upper_point_3 = after_second_room[0].pop(0)
    after_second_room[0].insert(-1, upper_point_2)
    # 맨 왼족 column
    after_second_room[u_air_cleaner_x-1].pop(0)
    for i in range(u_air_cleaner_x - 2, 0, -1):
        after_second_room[i+1].insert(0, after_second_room[i].pop(0))
    after_second_room[1].insert(0, upper_point_3)
    
    # # 아래쪽 공기 청정기

    # 공기 청정기 row
    lower_point_1 = after_second_room[d_air_cleaner_x].pop()
    after_second_room[d_air_cleaner_x].insert(1, 0)
    # 맨 오른쪽 column
    lower_point_2 = after_second_room[r-1].pop()
    for i in range(r-1, d_air_cleaner_x + 1, -1):
        after_second_room[i].append(after_second_room[i-1].pop())
    after_second_room[d_air_cleaner_x + 1].append(lower_point_1)
    # 맨 하단 row
    lower_point_3 = after_second_room[r-1].pop(0)
    after_second_room[r-1].insert(-1, lower_point_2)
    # 맨 왼쪽 column
    after_second_room[d_air_cleaner_x+1].pop(0)
    for i in range(d_air_cleaner_x + 1, r-2):
        after_second_room[i].insert(0, after_second_room[i+1].pop(0))
    after_second_room[r-2].insert(0, lower_point_3)

    before_second_room = deepcopy(after_second_room)

dust_sum = 0
for i in after_second_room:
    dust_sum += sum(i)
print(dust_sum + 2)