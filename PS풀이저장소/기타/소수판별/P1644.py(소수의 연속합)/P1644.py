from sys import stdin
from bisect import bisect_left

stdin = open('./input.txt', 'r')
    
n = int(stdin.readline())

result = 0
arr = [True] * (n+1)
prime_num = []

for i in range(2, int(n ** 0.5) + 1):
    if arr[i]:
        j = 2
        while j*i <=n:
            arr[i*j] = False
            j += 1

for i in range(2, n+1):
    if arr[i]:
        prime_num.append(i)

prime_num.insert(0, 0)
# print(prime_num)

idx = bisect_left(prime_num, int(n // 2))

#n이 소수인지 확인
if prime_num[-1] == n:
    result += 1

#소수 리스트의 길이
arr_length = len(prime_num)

#누적 합
for i in range(1, arr_length):
    prime_num[i] += prime_num[i-1]

# print(prime_num)
for i in range(arr_length):
    #2는 예외처리
    if n == 2 or n == 3 or i > idx:
        break
    for j in range(i+1, arr_length):
        if prime_num[j] - prime_num[i] >= n:
            if prime_num[j] - prime_num[i] == n:
                # print(i, j)
                result += 1
            break
print(result)