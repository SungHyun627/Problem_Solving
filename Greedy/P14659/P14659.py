from sys import stdin

# stdin = open('./input.txt', 'r')
# 활잡이 / 봉우리 수
n= int(stdin.readline().rstrip())

# 봉우리 리스트
mount_list = list(map(int, stdin.readline().rstrip().split()))


# 가장 높은 봉우리의 높이
max_mount = 0
# 최대로 처치할 수 있는 적의 수 
max_enemy_kill = 0
# 처치한 적의 수
enemy_kill = 0
for mount in mount_list :
    if mount > max_mount:
        max_mount = mount
        enemy_kill = 0
    else:
        enemy_kill += 1
    max_enemy_kill = max(max_enemy_kill, enemy_kill)
    
print(max_enemy_kill)


