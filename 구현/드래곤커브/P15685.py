from sys import stdin
from copy import deepcopy

stdin = open('./input.txt', 'r')

# 드래곤 커브 개수
n = int(stdin.readline().rstrip())

# 정사각형이 만들어지기 위해 필요한 꼭지점의 개수를 저장하는 리스트
# y = 0일 때 길이가 1인 변을 밑변으로 가지는 정사각형들을, 왼쪽에서부터 0으로 시작하여 매긴다.
# 총 0~9999번의 10000개의 번호가 생긴다.
sqaure_point_num_list = [0]*10000

# 모든 curve의 point(꼭지점)을 저장하는 리스트 (중복 X)
point_list = []

# 주어진 문제의 좌표와는 다르게, 기존에 통용되는 좌표축을 사용한다.
# 오른쪽으로 갈수록 x 값이 커지고 위쪽으로 갈수록 y값이 커진다.
# 따라서 이 좌표계에서는 매 세대마다 기준점을 기준으로 반시계 방향으로 90회전한다.
for _ in range(n):
    # origin_x : 시작점의 x좌표, origin_y : 시작점의 y좌표, d : 시작방향, g : 세대
    origin_x, origin_y, d, g =  map(int, stdin.readline().rstrip().split())
    
    # 각 curve의 point(꼭지점)을 저장하는 리스트
    curve_point_list = [[origin_x, origin_y]]
    # 0세대인 경우 새로이 생기는 꼭지점의 방향을 나타내는 리스트 => dx, dy
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    zero_x = origin_x + dx[d]
    zero_y = origin_y + dy[d]
    curve_point_list.append([zero_x, zero_y])
    # 다음 세대의 시작점 갱신
    start_x = zero_x
    start_y = zero_y
    for _ in range(g):
        nth_curve_point_list = deepcopy(curve_point_list)
        for x, y in nth_curve_point_list:
            """
            세대의 증가에 따라 새롭게 생기는 x, y좌표 => nx, ny
            특정 좌표(a, b)를 중심으로 하는 반시계방향의 90도 회전변환
            nx = - y + a + b, ny = x - a + b
            """
            nx = -y + start_x + start_y
            ny = x - start_x + start_y
            if [nx, ny] not in curve_point_list:
                # 새롭게 생성된 좌표가 리스트에 없다면 추가
                curve_point_list.append([nx, ny])
            # 다음 curve의 시작점 갱신
            if x == origin_x and y == origin_y:
                next_start_x = nx
                next_start_y = ny
        start_x = next_start_x
        start_y = next_start_y
    
    # 각 드래곤 커브에서 얻어진 point를 point_list에 기록
    for x, y in curve_point_list:
        if [x, y] not in point_list:
            point_list.append([x, y])

# point 리스트의 좌표에 따라 각 좌표를 지니는 정사각형에 해당하는 인덱스의 값을 1씩 증가
for x, y in point_list:
    if x < 100 and y < 100:
        sqaure_point_num_list[x + y*100] += 1
    if x >= 1 and y < 100:
        sqaure_point_num_list[x-1 + y*100] += 1
    if x < 100 and y >= 1:
        sqaure_point_num_list[x+(y-1)*100] += 1   
    if x >= 1 and y >= 1:
        sqaure_point_num_list[x-1 + (y-1)*100] += 1

print(sqaure_point_num_list.count(4))