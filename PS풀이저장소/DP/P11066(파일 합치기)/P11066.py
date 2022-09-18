#P11066 파일 합치기
#PyPy로 통과
from sys import stdin

stdin = open('./input.txt', 'r')

t = int(stdin.readline())
INF = int(10000*500*500)

def calculate_min_cost(n, arr):
  dp = [[INF] * n for _ in range(n)]
  arr_sum = [0] + [i for i in arr]
  for i in range(n):
    arr_sum[i+1] += arr_sum[i]

  for i in range(n):
    dp[i][0] = 0
  
  # 페이지 사이 간격
  for k in range(1, n):
    # 시작 페이지
    for i in range(n-k):
      for j in range(k):
        # print(i, j, k)
        # print(dp[i][j], dp[i+j+1][k-j-i-1], arr_sum[i+k+1] , arr_sum[i])
        dp[i][k] = min(dp[i][k], dp[i][j]+ dp[i+j+1][k-j-1] + arr_sum[i+k+1] - arr_sum[i])
        # print(dp)
    
  return dp[0][n-1]

for _ in range(t):
  n = int(stdin.readline())
  arr = list(map(int, stdin.readline().split()))
  print(calculate_min_cost(n, arr))