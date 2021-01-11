from sys import stdin

stdin = open("./input.txt", 'r')

# 입력받을 수의 개수
n = int(stdin.readline())
# 숫자 입력 리스트
numbers = []
for _ in range(n):
    numbers.append(int(stdin.readline().rstrip()))
# 오름차순 정렬
numbers.sort()
# 출력
for i in numbers:
    print(i)