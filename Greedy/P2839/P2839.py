from sys import stdin

# stdin = open('./input.txt', 'r')

n = int(stdin.readline().rstrip())
# x : 5kg 봉지 개수, y : 3kg 봉지 개수
# 5x + 3y = n
# modular 연산

if n % 3 == 0:
    x = 3 * (n // 15)
elif n % 3 == 1:
    if n < 10:
        x = None
    else:
        x = 3 * ((n - 10) // 15) + 2
else:
    if n < 5:
        x = None
    else:
        x = 3 * ((n - 5) // 15) + 1

if x == None:
    print("-1")
else:
    y = int((n - 5 * x) / 3)
    print(x + y)
