from sys import stdin
from math import ceil, log2

stdin = open('./input.txt', 'r')


#n : 수의 개수, m: 수의 변경이 일어나는 횟수, k : 구간의 합을 구하는 횟수
n, m, k = map(int, stdin.readline().split())

#수를 담는 리스트
a = []

#트리의 높이
h = ceil(log2(n))

#트리를 담는 리스트
tree = [0] * (2 ** (h+1) - 1)

#수 받기
for i in range(n):
    a.append(int(stdin.readline()))

#트리 초기화
def init(node, start, end):
    if start == end:
        tree[node] = a[start]
        return
    else:
        mid = (start + end) // 2
        init(node*2, start, mid)
        init(node*2 + 1, mid+1, end)
        tree[node] = tree[node*2] + tree[node*2 + 1]

#트리 업데이트
def update(node, start, end, index, diff):
    if (index < start) or (index > end):
        return
    tree[node] += diff
    if (start != end):
        mid = (start + end) // 2
        update(node * 2, start, mid, index, diff)
        update(node * 2 + 1, mid + 1, end, index, diff)


#구간 합 구하기
def find_interval_sum(node, start, end, left, right):
    #겹치는 범위가 없을 때
    if left > end or right < start:
        return 0
    
    #구간 합이 노드의 범위를 포함하고 있는 있을 때 ex) 구간합(1~9), node(2~4)
    if left <= start and right >= end:
        return tree[node]
    
    mid = (start + end) // 2
    return find_interval_sum(node*2, start, mid, left, right) + find_interval_sum(node*2 + 1, mid+1, end, left, right)

#트리 초기화
init(1, 0, n-1)

for _ in range(m+k):
    b, c, d = map(int, stdin.readline().split())
    if b == 1:
        #수를 담는 리스트 값 수정
        pre_value = a[c-1]
        a[c-1] = d
        update(1, 0, n-1, c-1, d - pre_value)
    else:
        print(find_interval_sum(1, 0, n-1, c-1, d-1))
    # print(tree)