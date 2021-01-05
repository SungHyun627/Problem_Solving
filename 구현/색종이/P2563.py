from sys import stdin

stdin = open('./input.txt', 'r')

# 색종이 수
n = int(stdin.readline().rstrip())
# 1X1 사각형의 왼쪽 아래 꼭지점을 key로 하는 dictionary 생성
square_point = {}

# dictionary에 해당 점이 포함되지 않았으면 dictionary에 추가
for _ in range(n):
    a, b = map(int, stdin.readline().rstrip().split())
    for i in range(a, a + 10):
        for j in range(b, b + 10):
            if (i, j) not in square_point:
                square_point[(i, j)] = 1
# dictionary의 key의 수 출력
print(len(square_point))