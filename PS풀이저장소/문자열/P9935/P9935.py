from sys import stdin

stdin = open('./input.txt', 'r')
s = stdin.readline().rstrip()
bomb = stdin.readline().rstrip()

stack = []

for i in range(len(s)):
    stack.append(s[i])
    
    # Stack의 element 수가 bomb의 길이보다 같거나 클 때
    if len(stack) >= len(bomb):
        if ''.join(stack[-len(bomb):]) == bomb:
            for _ in range(len(bomb)):
                stack.pop()

if not stack:
    print("FRULA")
else:
    print(''.join(stack))