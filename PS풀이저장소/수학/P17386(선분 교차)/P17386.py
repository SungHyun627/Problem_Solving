#P17386 선분 교차
from sys import stdin
stdin = open('./input.txt', 'r')

#point1, point2, point3, point4
x1, y1, x2, y2 = map(int, stdin.readline().split())
x3, y3, x4, y4 = map(int, stdin.readline().split())

min_L1_x, max_L1_x = min(x1, x2), max(x1, x2)
min_L2_x, max_L2_x = min(x3, x4), max(x3, x4)
min_L1_y, max_L1_y = min(y1, y2), max(y1, y2)
min_L2_y, max_L2_y = min(y3, y4), max(y3, y4)

def ccw(p1_x, p1_y, p2_x, p2_y, p3_x, p3_y):
    #CCW 알고리즘, 외적
    return (p1_x*p2_y + p2_x*p3_y + p3_x*p1_y) - (p2_x*p1_y + p3_x*p2_y + p1_x*p3_y)

#point_1, point2가 이루는 선분에 대한 외적
ccw12 = ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4)
#point_3, point4가 이루는 선분에 대한 외적
ccw34 = ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2)

# 두 선분이 일직선상에 있는 경우
if ccw12 == 0 and ccw34 == 0:
    if (min_L1_x <= max_L2_x) and (min_L2_x <= max_L1_x) and (min_L1_y <= max_L2_y) and (min_L2_y <= max_L1_y):
        print(1)
    else:
        print(0)
else:
    if ccw12 <= 0 and ccw34 <= 0:
        print(1)
    else:
        print(0)