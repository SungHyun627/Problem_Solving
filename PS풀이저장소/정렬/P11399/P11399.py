from sys import stdin

stdin = open('./input.txt', 'r')

# 입력받을 수의 개수
n = int(stdin.readline().rstrip())

# 돈을 인출하는데 걸리는 시간 입력받기
withdrawal_time = list(map(int, stdin.readline().split()))

#오름차순 정렬 
withdrawal_time.sort()

# 돈을 인출하는 데 걸리는 시간
sum = 0
for i in range(n):
    sum += withdrawal_time[i] * (n-i)
print(sum)