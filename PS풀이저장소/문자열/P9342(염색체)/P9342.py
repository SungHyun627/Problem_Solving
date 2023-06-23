#P9342 염색체
from sys import stdin
import re
stdin = open('./input.txt', 'r')

x = re.compile('[A-F]?A*F*C*[A-F]?$')
n = int(stdin.readline())

for _ in range(n):
  y = stdin.readline().rstrip()
  if x.match(y) == None:
    print('Good')
  else:
    print('Infected!')