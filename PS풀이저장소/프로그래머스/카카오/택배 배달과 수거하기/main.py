inputs = [[1, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]], [2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]]]

def solution(cap, n, deliveries, pickups):
    answer = 0
    d = p = 0  # 배달 남은 박스, 수거 남은 박스
    for i in range(n-1, -1, -1):  # 가장 먼 집부터
        d += deliveries[i]
        p += pickups[i]
        print(d, p)
        # 이번 집까지 가야 할 일이 남아 있으면
        while d > 0 or p > 0:
            d -= cap
            p -= cap
            answer += (i + 1) * 2  # 왕복 거리            
    return answer

for input in inputs:
  print(solution(*input))