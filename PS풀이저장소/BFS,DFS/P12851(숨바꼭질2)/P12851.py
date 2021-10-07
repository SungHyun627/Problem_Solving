from sys import stdin
from collections import deque

stdin = open('./input.txt', 'r')

n, k = map(int, stdin.readline().split())

queue = deque()
time = 0
answer_time = 0
count_answer = 0
queue.append((n, time))

def bfs():
    global answer_time
    global count_answer

    visited = [0] * 200001
    visited[n] = 0
    is_terminated = False

    if n == k:
        count_answer += 1
        return

    while queue:
        if is_terminated:
            break
        x, t = queue.popleft()        
        nx_list = [2 * x, x + 1, x -1]

        for nx in nx_list:
            if nx < 0 or nx >= 200000:
                continue
            if not visited[nx] or visited[nx] >= t + 1:
                if nx != k:
                    queue.append((nx, t+1))
                    visited[nx] = t+1
                else:
                    is_terminated = True
                    answer_time = (t+1) 
                    visited[nx] = t+1
                    count_answer += 1
           
    while queue:
        x, t = queue.popleft()

        if t+1 > answer_time:
            break

        nx_list = [2 * x, x + 1, x -1]

        for nx in nx_list:
            if nx < 0 or nx >= 200000:
                continue
            if nx == k:
                count_answer += 1
bfs()

print(answer_time, count_answer, sep = '\n')