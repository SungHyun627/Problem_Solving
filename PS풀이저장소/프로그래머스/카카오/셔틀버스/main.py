def solution(n, t, m, timetable):
    answer = ''
    bus_times = [540 + t * i for i in range(n)]
    times = []
    for time in timetable:
        x, y = time.split(':')
        times.append(int(x) * 60 + int(y))
    times.sort()
    idx = 0
    
    for bus_time in bus_times:
        cnt = 0
        while cnt < m and idx < len(times) and times[idx] <= bus_time:
            cnt += 1
            idx += 1	
        if cnt < m:
        	answer = bus_time
        else:
            answer = times[idx-1] - 1
    answer = str(answer//60).zfill(2) + ':'+ str(answer%60).zfill(2)
    return answer