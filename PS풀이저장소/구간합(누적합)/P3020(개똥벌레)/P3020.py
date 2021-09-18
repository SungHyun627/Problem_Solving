from sys import stdin


stdin = open('./input.txt', 'r')
#n : 너비, h : 높이
n, h = map(int, stdin.readline().rstrip().split())

obstacle_heights_from_bottom = [0]*h
obstacle_heights_from_top = [0]*h
obstacle_number = [0]*h
min_obstacles = n+1
count = 0


for i in range(0, (n//2)):
    a = int(stdin.readline())
    b = int(stdin.readline())
    obstacle_heights_from_bottom[a] += 1
    obstacle_heights_from_top[b] += 1

# print(obstacle_heights_from_bottom, obstacle_heights_from_top)

#obstacle_heights_from_bottom[i] 는 bottom에서 1~i까지의 높이를 가지는 장애물 수
#obstacle_heights_from_top[i] 는 top에서 1~i까지의 높이를 가지는 장애물 수
for i in range(1, h):
    obstacle_heights_from_bottom[i] += obstacle_heights_from_bottom[i-1]
    obstacle_heights_from_top[i] += obstacle_heights_from_top[i-1]

# print(obstacle_heights_from_bottom, obstacle_heights_from_top)

#각 높이에서 수평에 위치한 장애물의 개수 계산
for j in range(1, h+1):
    obstacles = obstacle_heights_from_bottom[h-1] - obstacle_heights_from_bottom[j-1] + obstacle_heights_from_top[h-1] - obstacle_heights_from_top[h-j]
    # print(obstacles)
    if obstacles < min_obstacles:
        min_obstacles = obstacles
        count = 1
    elif obstacles > min_obstacles:
        continue
    else:
        count += 1
        
print(min_obstacles, count)