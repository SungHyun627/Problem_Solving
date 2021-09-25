from sys import stdin
from math import log2, ceil

stdin = open('./input.txt', 'r')

#사탕상자에 손을 댄 횟수
n = int(stdin.readline())

#사탕의 종류 수
candy_category_num = int(1e6)

#트리
tree = [0] * (2 ** (ceil(log2(candy_category_num)) + 1) -1)

def update(node, start, end, target_candy, add_candy_num):
    if target_candy < start or target_candy > end:
        return

    #diff만큼    
    tree[node] += add_candy_num

    #해당 타겟을 찾으면 종료
    if start == end:
        return

    mid = (start + end) // 2
    update(node*2, start, mid, target_candy, add_candy_num)
    update(node*2 +1, mid+1, end, target_candy, add_candy_num)

def take_out(node, start, end, target_order):
    if start >= end:
        update(1, 0, candy_category_num-1, start, -1)
        # print(start)
        return start
    
    mid = (start + end) // 2

    if tree[node*2] >= target_order:
        return take_out(node*2, start, mid, target_order)
    else:
        return take_out(node*2 + 1, mid+1, end, target_order - tree[node*2])

for _ in range(n):
    candy_task = list(map(int, stdin.readline().split()))
    if candy_task[0] == 1:
        print(take_out(1, 0, candy_category_num-1, candy_task[1]) + 1)
    else:
        update(1, 0, candy_category_num-1, candy_task[1] - 1, candy_task[2])

