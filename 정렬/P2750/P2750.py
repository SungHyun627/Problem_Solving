from sys import stdin

stdin = open('./input.txt', 'r')

# 입력받을 수의 개수
n = int(stdin.readline().rstrip())

# 수를 담을 리스트
numbers = []

# 수 입력 받기
for _ in range(n):
    numbers.append(int(stdin.readline().rstrip()))

#오름차순 정렬 
numbers.sort()

# 출력
for i in numbers:
    print(i)