from sys import stdin

stdin = open('./input.txt', 'r')

n = int(stdin.readline())
x_coord = []
y_coord = []

for _ in range(n):
    a, b = map(int, stdin.readline().split())
    x_coord.append(a)
    y_coord.append(b)
x_coord.append(x_coord[0])
y_coord.append(y_coord[0])

a = 0
b = 0

for i in range(n):
    a += x_coord[i] * y_coord[i+1]
    b += y_coord[i] * x_coord[i+1]

print('{0:.1f}'.format(0.5 * abs(a-b)))