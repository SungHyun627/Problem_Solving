from bisect import bisect_left
from sys import stdin

stdin = open('./input.txt', 'r')

#전깃줄의 개수
n = int(stdin.readline())

#전기줄의 정보를 담는 리스트
wires = [0] * 500001

#전깃줄 정보 입력
for _ in range(n):
    a, b = map(int, stdin.readline().split())
    wires[a] = b


#LIS 내에서의 각 원소의 index
dp_index = [0] * 500001

#겹치지 않는 전봇대(b)의 정보롤 담는 리스트
dp = []

end = 0
first_element = 0

for i in range(500001):
    if wires[i] != 0:
        dp.append(wires[i])
        dp_index[i] = 1
        break

for i in range(1, 500001):
    if wires[i] == 0:
        continue
    if wires[i] > dp[end]:
        dp.append(wires[i])
        end += 1
        dp_index[i] = (end+1)
    else:
        idx = bisect_left(dp, wires[i])
        dp[idx] = wires[i]
        dp_index[i] = idx+1

target_index = 500001
for i in range(end+1, 0, -1):
    for j in range(target_index-1, 0, -1):
        if dp_index[j] == i:
            dp_index[j] = 0
            target_index = j
            break

print(n-end-1)

for i in range(500001):
    if dp_index[i] != 0:
        print(i)