inputs = [[4, [1, 1, 0, 1]],[2, [0, 1]], [10, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]]

def solution(n, tops):
  MOD = 10007
  ### 가운데 정삼각형을 채우는 방법에 대한 경우의 수로 생각
  ## 1. 삼각형 2. ﹆ 3. ⏥ 4. ♢

  ### 3번방식으로 채울 때
  a = [0] * (n+1)
  ### 3번방식으로 채우지 않을 때
  b = [0] * (n+1)

  a[1] = 1
  b[1] = 3 if tops[0] == 1 else 2

  for i in range(2, n+1):
    if tops[i-1] == 1:
      a[i] = (a[i-1] + b[i-1]) % MOD
      b[i] = (2 * (a[i-1] + b[i-1]) + b[i-1]) % MOD
    else:
      a[i] = (a[i-1] + b[i-1]) % MOD
      b[i] = ((a[i-1] + b[i-1]) + b[i-1]) % MOD
    
  return (a[n] + b[n]) % MOD

for input in inputs:
  print(solution(input[0], input[1]))