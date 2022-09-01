#P3079 입국심사
from sys import stdin

stdin = open('./input.txt', 'r')
n, m = map(int, stdin.readline().split())

process_times = [int(stdin.readline().rstrip()) for _ in range(n)]

start, end = 1, max(process_times) * m
answer = 0

while start <= end:
  people_num = 0
  mid = (start + end) // 2
  for process_time in process_times:
    people_num += (mid // process_time)
    if people_num >= m:
        answer = mid
        end = mid - 1
        break
  if people_num < m:
    start = mid + 1
print(answer)

