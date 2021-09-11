from sys import stdin
from bisect import bisect_left

stdin = open('./input.txt', 'r')
n = int(stdin.readline())
arr = list(map(int, stdin.readline().rstrip().split()))

Lis1 = [arr[0]]

end1 = 0

for i in range(1, n):
    if Lis1[end1] < arr[i]:
        Lis1.append(arr[i])
        end1 += 1
    else:
        ## 이진탐색
        idx = bisect_left(Lis1, arr[i])
        Lis1[idx] = arr[i]
    # print(Lis1)
print(end1 + 1)