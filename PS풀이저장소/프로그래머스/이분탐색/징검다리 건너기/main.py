def can_cross(stones, x, k, w):
    continuous_cannot_move_stone_count = 0
    for i in range(w):
        if stones[i] < x:
            continuous_cannot_move_stone_count += 1
        else:
            continuous_cannot_move_stone_count = 0
        if continuous_cannot_move_stone_count == k:
            return False
    return True

def solution(stones, k):
    answer = 0
    start, end = 1, max(stones)
    stones_len = len(stones)
    
    while start <= end:
        print(start, end)
        mid = int((start + end) // 2)
        if can_cross(stones, mid, k, stones_len):
            answer = mid
            start = mid+1
        else:
            end = mid-1
    return answer