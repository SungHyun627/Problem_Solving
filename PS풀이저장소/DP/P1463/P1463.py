from sys import stdin

stdin = open('./input.txt', 'r')

num = int(stdin.readline())

# dp 테이블
d = [0] * 1000001

# 2부터 num까지 d[i]계산
for i in range(2, num + 1):
    d[i] = d[i-1] + 1

    # 2으로 나눠 떨어진다면
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    # 3으로 나눠 떨어진다면
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)

print(d[num])