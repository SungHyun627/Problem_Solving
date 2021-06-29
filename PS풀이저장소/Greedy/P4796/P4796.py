from sys import stdin

stdin = open('./input.txt', 'r')

num = 1

while(1):
    l, p, v = map(int, stdin.readline().rstrip().split())
    if l == 0:
        break
    can_used = (v // p ) * l + min(l, v % p)
    print("Case {0}: {1}".format(num, can_used))
    num += 1