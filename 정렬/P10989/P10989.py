# Counting sort 사용
from sys import stdin

stdin = open('./input.txt', 'r')
n = int(stdin.readline())
number_array = [0] * 10001
for i in range(n):
    number_array[int(stdin.readline())] += 1

for i in range(1, 10001):
    if number_array[i] != 0:
        for _ in range(number_array[i]):
            print(i)