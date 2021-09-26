from bisect import bisect_left
from sys import stdin

stdin = open('./input.txt', 'r')

# O(nlogn) 방법

#수열의 크기
n = int(stdin.readline())

#수열
arr = list(map(int, stdin.readline().split()))

#LIS의 길이를 구하기 위한 리스트
dp = [arr[0]]

#LIS에서 각 원소가 위치하는 index를 기록하는 리스트
dp_index = [0] * (n)
dp_index[0] = 1


#최장 LIS
answer = []

#dp의 마지막 원소의 index
end = 0

for i in range(1, n):
    if arr[i] > dp[end]:
        dp.append(arr[i])
        end += 1
        dp_index[i] = (end+1)
    else:
        idx = bisect_left(dp, arr[i])
        dp[idx] = arr[i]
        dp_index[i] = (idx + 1)

target_index = n
for i in range(end+1, 0, -1):
    for j in range(target_index-1,  -1, -1):
        if dp_index[j] == i:
            answer.append(arr[j])
            target_index = j
            break

#역순
answer.reverse()

print(end+1)
print(*answer)