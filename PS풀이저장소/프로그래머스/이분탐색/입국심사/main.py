def solution(n, times):
    answer = 0
    start, end = 1, max(times) * n

    while start <= end:
      people_num = 0
      mid = (start + end) // 2
      for time in times:
        people_num += (mid // time)
        if people_num >= n:
            answer = mid
            end = mid - 1
            break
      if people_num < n:
        start = mid + 1

    return answer