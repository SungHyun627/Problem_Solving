from sys import stdin

stdin = open('./input.txt', 'r')

# 테스트 케이스 수
n = int(stdin.readline())
# 정수 리스트
numList = list(int(stdin.readline()) for _ in range(n))
# 각 정수의 합의 경우의 수를 저장하기 위한 리스트
d = [0] * 10
d[0] = 1
d[1] = 2
d[2] = 4
#  d[i] = d[i-1] + d[i-2] + d[i-3]
for i in range(3, 10):
    d[i] = d[i-1] + d[i-2] + d[i-3]

for i in numList:
    print(d[i-1])