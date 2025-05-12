n, m = map(int, input().split())
arr = [int(input()) for _ in range(m)]


ans = 0
start, end = 1, 10**14

while start <= end:
    mid = (start + end) // 2
    total = 0
    for time in arr:
        total += (mid // time)
        if total >= n:
            ans = mid
            end = mid - 1
            break
    if total < n:
        start = mid + 1
print(ans)

