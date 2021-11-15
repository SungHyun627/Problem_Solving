#P2096 내려가기
from sys import stdin

stdin = open('./input.txt', 'r')

n = int(stdin.readline())

start = list(map(int, stdin.readline().split()))
max_arr = [*start]
min_arr = [*start]

for i in range(1, n):
    a, b, c = map(int, stdin.readline().split())
    max_arr = [a + max(max_arr[0], max_arr[1]), b + max(max_arr), c + max(max_arr[1], max_arr[2])]
    min_arr = [a + min(min_arr[0], min_arr[1]), b + min(min_arr), c + min(min_arr[1], min_arr[2])]
print(max(max_arr), min(min_arr))