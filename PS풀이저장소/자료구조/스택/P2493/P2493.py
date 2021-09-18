from sys import stdin
from bisect import bisect_left

stdin = open('./input.txt', 'r')

n = int(stdin.readline())
answer = []
towers = list(map(int, stdin.readline().rstrip().split()))
stack = []

for i in list(enumerate(towers)):
    while True:
        # print(stack)
        if not stack:
            stack.append(i)
            answer.append(0)
            break        
        index = stack[-1][0]
        height = stack[-1][1]

        if height > i[1]:
            answer.append(index+1)
            stack.append(i)
            break
        else:
            stack.pop()
print(*answer)