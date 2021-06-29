from sys import stdin

stdin = open('./input.txt', 'r')

# 세로 : n, 가로 : m
n, m = map(int, stdin.readline().rstrip().split())

# 최대 방문할 수 있는 칸의 수

if n == 1:
    max_visited = 1
elif n == 2:
    # 나이트가 4회 이상 이동 불가
    if m < 3:
        max_visited = 1
    elif m >= 3 and m < 5:
        max_visited = 2
    elif m >= 5 and m < 7:
        max_visited = 3
    else:
        max_visited = 4
else:
    # 나이트가 4회 이상 이동불가
    if m < 5:
        max_visited = m
    # 나이트가 4회 이상 이동불가
    elif m >= 5 and m <= 6:
        max_visited = 4
    # 나이트가 4회 이상 이동
    else:
        max_visited = 5 + (m - 7)

print(max_visited)    
