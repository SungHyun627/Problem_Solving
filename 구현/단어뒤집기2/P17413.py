from sys import stdin
from collections import deque

stdin = open('./input.txt', 'r')

sentence = stdin.readline().rstrip()
# deque 생성
deq = deque()
for i in sentence:
    if i == "<":
        while(len(deq)):
            print(deq.pop(), end ="")
        deq.append(i)
    elif i == ">":
        deq.append(i)
        while(len(deq)):
            print(deq.popleft(), end ="")
    elif i == " ":
        if len(deq) == 0:
            deq.append(i)
        else:
            if deq[0] == "<":
                deq.append(i)
            else:
                deq.appendleft(i)
    else:
        if len(deq) == 0:
            deq.append(i)
        else:
            if deq[0] == "<":
                deq.append(i)
            elif deq[0] == " ":
                while(len(deq)):
                    print(deq.pop(), end ="")
                deq.append(i)
            else:
                deq.append(i)
while(len(deq)):
    print(deq.pop(), end ="")