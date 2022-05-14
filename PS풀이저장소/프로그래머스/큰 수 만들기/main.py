import sys

# sys.setrecursionlimit(10**5)

def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while k > 0 and stack and int(stack[-1]) < int(num):
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)