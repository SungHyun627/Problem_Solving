from collections import deque
import heapq
def solution(jobs):
    total_time = 0
    time = 0
    jobs_length = len(jobs)
    jobs.sort(key = lambda x: x[0])
    jobs = deque(list(map(lambda x: (x[1], x[0]),jobs)))
    
    print(jobs)
    a = []
    while True:
        # print(time, total_time)
        while True:
            if jobs and jobs[0][1] <= time:
                heapq.heappush(a, jobs.popleft())
            else:
                break
        
        if not a:
            if not jobs:
                break
            else:
                time = jobs[0][1]
        else:        
            x, y = heapq.heappop(a)
            # print(x, y, time)
            time += x
            total_time += (time - y)
                
    return int(total_time // jobs_length)