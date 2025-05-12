n, k = map(int, input().split())
x = [int(input()) for _ in range(n)]

x.sort()

ans = 0

start, end = 0, (x[0] + x[-1]) // 2

while start <= end:
    mid = (start + end) // 2
    cnt = 1
    cur = x[0]+mid
    idx = 0

    while idx != n:
        if abs(x[idx] - cur) <= mid:
            idx +=1
            continue
        cnt += 1
        cur = x[idx]+mid
        idx +=1
    
    if cnt > k:
        start = mid + 1
    else:
        ans = mid
        end = mid - 1

print(ans)


    

