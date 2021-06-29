# 캥거루 세마리 2
from sys import stdin

# stdin = open('./input.txt', 'r')

jump_num = 0

while(1):
    kangaroo_position = stdin.readline().rstrip()
    # 문자열이 없을 때 break
    if not(kangaroo_position):
        break;
    a, b, c =  map(int, kangaroo_position.split())
    
    # 캥거리 사이의 간격 중 가장 큰 간격의 거리 - 1 만큼이 캥거루가 최대 움직일 수 있는 횟수이다.

    # b - a > c - b
    if (b - a) > (c - b):
        jump_num = b - a - 1
    else:
        jump_num = c - b - 1

    print(jump_num)
    