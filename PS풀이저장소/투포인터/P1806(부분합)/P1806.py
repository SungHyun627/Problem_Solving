from sys import stdin

stdin = open('./input.txt', 'r')

#n : 원소의 개수, s: 합
n, s = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

end = 0
interval_sum = 0
min_length = n+1

for start in range(n):
    while interval_sum < s and end < n:
        # print(start, end, interval_sum)
        interval_sum += arr[end]
        end += 1
    if interval_sum >= s:
        interval_sum -= arr[start]    
        if min_length > (end-start):
            min_length = (end - start)

if min_length == n+1:
    min_length = 0
print(min_length)