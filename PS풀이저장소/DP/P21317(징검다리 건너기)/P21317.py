#P21317 징검다리 건너기
from sys import stdin

stdin = open('./input.txt', 'r')
n = int(stdin.readline())
# i번째 돌에서 작은 점프(1칸), 큰 점프(2칸)를 하는 데 소비되는 에너지를 저장하는 리스트
arr = [[0] * 2 for _ in range(n)]

for i in range(1, n):
    arr[i][0], arr[i][1] = map(int, stdin.readline().split())

# 매우 큰 점프를 하는데 소비하는 에너지(3칸)
k = int(stdin.readline())
    
# di[i][0] : i번째 돌까지 매우 큰 점프를 사용하지 않고, 소모한 최소한의 총 에너지
# di[i][0] : i번째 돌까지 매우 큰 점프를 사용하고, 소모한 최소한의 총 에너지
dp = [[5000*20] * 2 for _ in range(n+1)]
dp[0][0], dp[0][1], dp[1][0], dp[1][1] = 0, 0, 0, 0
if n == 1:
    print(0)
elif n == 2:
    print(arr[1][0])
elif n == 3:
    print(min(arr[1][1], dp[2][0] + arr[2][0]))
else:
    dp[2][0] = arr[1][0]
    dp[3][0] = min(arr[1][1], dp[2][0] + arr[2][0])

    for i in range(4, n+1):
        dp[i][0] = min(dp[i-1][0] + arr[i-1][0], dp[i-2][0] + arr[i-2][1])
        dp[i][1] = min(dp[i-1][1] + arr[i-1][0], dp[i-2][1] + arr[i-2][1], dp[i-3][0] + k)

    print(min(dp[n]))