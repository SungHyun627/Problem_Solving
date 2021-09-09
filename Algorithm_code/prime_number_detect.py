#에라토스테네스의 체
#n보다 작거나 같은 모든 소수를 찾을 때 사용
# 시간복잡도 : O(NlogNlogN)
# N이 백만 이내일 때 사용
"""
1. 2부터 n까지 모든 자연수 나열
2. 남은 수 중(~ sqrt(n))아직 처리하지 않은 가장 작은 수 i를 찾는다.
3. i의 배수를 제거(i는 남긴다)
4. 2~3을 반복
"""

from math import sqrt

n = 30
array = [True] * (n+1)

for i in range(2, int(sqrt(n)) + 1):
    if array[i]:
        j = 2
        while i*j <= n:
            array[i*j] = False
            j += 1
for i in range(2, n+1):
    if array[i]:
        print(i, end= ' ')