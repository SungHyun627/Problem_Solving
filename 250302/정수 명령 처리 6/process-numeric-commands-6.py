import heapq
n = int(input())
q = []

for _ in range(n):
    commands = input().split()
    c = commands[0] 
    if c == 'push':
        heapq.heappush(q, -int(commands[1]))
    elif c == 'pop':
        print(-heapq.heappop(q))
    elif c == 'size':
        print(len(q))
    elif c == 'empty':
        print(1 if len(q) == 0 else 0)
    else:
        print(-q[0])