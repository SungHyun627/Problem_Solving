from sys import stdin

stdin = open('./input.txt', 'r')

# 컵의 위치를 바꾼 횟수
n = int(stdin.readline().rstrip())

# 볼의 위치
ball_position = 1

# n번의 cup의 위치 change
for _ in range(n):
    a, b = map(int, stdin.readline().rstrip().split())
    if ball_position == a:
        ball_position = b
        continue
    elif ball_position == b:
        ball_position = a
        continue
    else:
        continue
print(ball_position)