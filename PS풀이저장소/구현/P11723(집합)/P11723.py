#P11723 집합
from sys import stdin
stdin = open('./input.txt', 'r')

m = int(stdin.readline())
s = set()

for _ in range(m):
    a = list(stdin.readline().split())
    command = a[0]
    if command == 'add':
        if int(a[1]) in s:
            continue
        s.add(int(a[1]))
    elif command == 'remove':
        if int(a[1]) not in s:
            continue
        else:
            s.remove(int(a[1]))
    elif command == 'check':
        if int(a[1]) in s:
            print(1)
        else:
            print(0)
    elif command == 'toggle':
        if int(a[1]) in s:
            s.remove(int(a[1]))
        else:
            s.add(int(a[1]))
    elif command == 'all':
        s = set([i for i in range(1, 21)])
    else:
        s = set()