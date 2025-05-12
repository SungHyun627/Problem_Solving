s = int(input())

start, end = 1, s
ans = -1

while start <= end:
    mid = (start + end) // 2
    total_sum = (mid)*(mid+1) // 2
    if total_sum > s:
        end = mid - 1
    else:
        start = mid+1
        ans = max(mid, ans)
print(ans)