from sys import stdin
from collections import deque

stdin = open('./input.txt', 'r')
# 문장 개수
n = int(stdin.readline())

# deque 생성
deq = deque()

for i in range(n):
    sentence = stdin.readline().rstrip() + '@'
    for j in sentence:
        if j == "@":
            while(len(deq)):
                print(deq.pop(), end = "")
            if i != n-1:
                print("")
            break
        if j == " ":
            deq.appendleft(j)
        else:
            if len(deq) == 0:
                deq.append(j)
            else:
                if deq[0] == " ":
                    while(len(deq)):
                        print(deq.pop(), end = "")
                deq.append(j)