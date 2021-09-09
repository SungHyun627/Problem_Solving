#재귀한도 설정
from sys import setrecursionlimit
setrecursionlimit(10 ** 6)

#math 모듈 (sqrt, gcd, factorial, pi, e)
from math import sqrt, gcd, factorial
print(sqrt(9), gcd(10, 15), factorial(5))

# 문장 합칠 때 join
string = ["hello", "how are you"] 
print('?'.join(string))

# 2차원 리스트 컴프리헨션
n = 3 
m = 4
array = [[0] * n for _ in range(m)]

# 무한으로 설정
INF = int(1e9)
print(INF)