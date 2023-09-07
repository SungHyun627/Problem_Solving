#P12904 A와 B
from sys import stdin
stdin = open('./input.txt', 'r')

s = stdin.readline().rstrip()
t = stdin.readline().rstrip()

while len(s) != len(t):
  x = t[-1]
  t = t[:-1]
  if x == 'B':
    t = t[::-1]
if s == t:
  print(1)
else:
  print(0)