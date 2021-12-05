#P17298 오큰수
from sys import stdin
from collections import deque
stdin = open('./input.txt', 'r')

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
answer = deque()
stack = []

for i in range(n-1, -1, -1):
    while True:
        if not stack:
            answer.appendleft(-1)
            stack.append(arr[i])
            break

        if stack[-1] > arr[i]:
            answer.appendleft(stack[-1])
            stack.append(arr[i])
            break
        else:
            stack.pop()
print(*answer)