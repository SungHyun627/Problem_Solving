from sys import stdin
import re

stdin = open('./input.txt', 'r')
n = int(stdin.readline())
p =  re.compile('(100+1+|01)+')
for _ in range(n):
    radio_wave = stdin.readline().rstrip()
    if p.fullmatch(radio_wave):
        print('YES')
    else:
        print('NO')