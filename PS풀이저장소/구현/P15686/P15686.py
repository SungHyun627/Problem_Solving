from sys import stdin
from collections import deque
from itertools import combinations

stdin = open('./input.txt', 'r')

n, m = map(int, stdin.readline().rstrip().split())
graph = [list(map(int, stdin.readline().rstrip().split())) for _ in range(n)]

#집
homes = []
# 치킨집
chicken_list = []

for i in range(n):
    for j in range(n):
        if not graph[i][j]:
            continue
        if graph[i][j] == 1:
            homes.append((i, j))
        else:
            chicken_list.append((i, j))

#기울이는 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def calculate_distance(x, y, removed_chickens):
    # print(removed_chickens)
    min_distance = int(1e9)
    existing_chickens_list = list(set(chicken_list) - set(removed_chickens))
    # print(existing_chickens_list)
    for existing_chicken in existing_chickens_list:
        pos_x, pos_y = existing_chicken
        calculate_distance = abs(x-pos_x) + abs(y-pos_y)
        if min_distance > calculate_distance:
            min_distance = calculate_distance
    # print(min_distance)
    return min_distance

def calculate_min_chicken_distance():
    #없앨 치킨집 M개를 선택
    removed_chickens_list = list(combinations(chicken_list, len(chicken_list)-m))

    #최소 도시의 치킨 거리
    min_chicken_distance = int(1e9)

    for removed_chickens in removed_chickens_list:
        # print(removed_chickens)
        chicken_distance = 0
        #m개의 치킨집 제거
        for removed_chicken_pos in removed_chickens:
            chicken_posx, chicken_posy = removed_chicken_pos
            graph[chicken_posx][chicken_posy] = 0

        # print(graph)
        #각 home에서의 치킨 거리 계산
        for home in homes:
            home_posx, home_posy = home
            chicken_distance += calculate_distance(home_posx, home_posy, removed_chickens)
        
        #치킨집 복구
        for removed_chicken_pos in removed_chickens:
            chicken_posx, chicken_posy = removed_chicken_pos
            graph[chicken_posx][chicken_posy] = 2

        # print(chicken_distance)
        if min_chicken_distance > chicken_distance:
            min_chicken_distance = chicken_distance
        
        # print(home_chicken_distances)
    return min_chicken_distance
        
print(calculate_min_chicken_distance())