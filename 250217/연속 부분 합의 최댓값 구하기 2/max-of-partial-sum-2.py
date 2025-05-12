n = int(input())
numbers = list(map(int, input().split()))

arr = [i for i in numbers]
result = -1000
curSum = 0

for i in range(n):
    if curSum < 0:
        curSum = arr[i]
    else:
        curSum += arr[i]
    result = max(curSum, result)

print(result)