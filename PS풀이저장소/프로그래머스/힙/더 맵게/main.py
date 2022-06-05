import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for food_scoville in scoville:
        heapq.heappush(heap, food_scoville)
    
    new_food_scoville = 0

    while True:
        food1 = heapq.heappop(heap)    
        if food1 >= K:
            break
        if not heap:
            answer = -1
            break
        food2 = heapq.heappop(heap)
        new_food_scoville = food1 + food2 * 2
        answer += 1

        heapq.heappush(heap, new_food_scoville)
    return answer