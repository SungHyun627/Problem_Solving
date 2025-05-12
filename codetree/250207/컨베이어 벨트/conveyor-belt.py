n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

arr = u+d
t = t % (n*2)
n_arr = arr[2*n-t:2*n]+arr[:2*n-t]

print(*n_arr[:n])
print(*n_arr[n:])
