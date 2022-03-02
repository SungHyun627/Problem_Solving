#P2156 포도주 시식
stdin = open('./input.txt', 'r')

n = int(stdin.readline())
dp = [[0] * 3 for _ in range(n)]
arr = []

for _ in range(n):
  arr.append(int(stdin.readline()))
# print(arr, dp)

for i in range(n):
  if not i:
    dp[0][1] = arr[0]
  else:
    dp[i] = max(dp[i-1]), (dp[i-1][0] + arr[i]), (dp[i-1][1] + arr[i])

print(max(dp[n-1]))