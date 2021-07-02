from sys import stdin
from collections import deque

stdin = open('./input.txt', 'r')

n = int(stdin.readline().rstrip())


for _ in range(n):
    # '('의 개수
    cnt = 0
    is_vps = True
    parenthesis_String = stdin.readline().rstrip()

    for i in range(len(parenthesis_String)):
        if parenthesis_String[i] == '(':
            cnt += 1 
        else:
            cnt -= 1
        
        if cnt < 0:
            is_vps = False
            print("NO")
            break

    if not is_vps:
        continue
    else:
        print("YES") if cnt == 0 else print("NO")