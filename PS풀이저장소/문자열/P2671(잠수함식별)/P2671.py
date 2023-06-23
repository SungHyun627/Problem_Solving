#P2671 잠수함식별
from sys import stdin
import re

stdin = open('./input.txt', 'r')

x = stdin.readline().rstrip()
check = re.compile('(100+1+|01)+')

if check.fullmatch(x):
  print('SUBMARINE')
else:
  print('NOISE')