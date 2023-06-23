#P9996 한국이 그리울 땐 서버에 접속하지
from sys import stdin
import re

stdin = open('./input.txt', 'r')

n = int(stdin.readline())
s = stdin.readline().rstrip().replace('*', '[a-z]*')
x = re.compile(s)

for _ in range(n):
  y = stdin.readline().rstrip()
  if x.fullmatch(y) == None:
    print('NE')
  else:
    print('DA')