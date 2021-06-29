from sys import stdin
from collections import Counter

stdin = open('./input.txt', 'r')
# 나무의 개수, 가져가고자 하는 나무의 길이
n, m = map(int, stdin.readline().split())

# 나무
woods = Counter(list(map(int, stdin.readline().split())))

# 이진 탐색
start = 0
end = max(woods.keys())

while start <= end:
    # 총 필요한 나무의 양
    total = 0
    # cutting할 지점
    mid = (start + end) // 2
    for wood in woods.keys():
        if wood > mid:
            total += (wood - mid) * woods[wood]
    
    if total < m:
        end = mid -1
    elif total == m:
        result = mid
        break
    else:
        result = mid
        start = mid + 1
print(result)