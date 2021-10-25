#P11049. 행렬 곱셈 순서
from sys import stdin

stdin = open('./input.txt', 'r')

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
#오름차순 정렬
arr.sort()

def find_three_solutions():
    if arr[-1] <= 0:
        return arr[-3], arr[-2], arr[-1]
    
    if arr[0] >= 0:
        return arr[0], arr[1], arr[2]
    solution_sum = int(1e9) * 3
    
    for i in range(n-2):
        #투 포인터
        start, end = i+1, n-1
        target_sum = -arr[i]
        while start < end:
            temp_sum = arr[start] + arr[end]
            if temp_sum == target_sum:
                return arr[i], arr[start], arr[end]
            if solution_sum > abs(temp_sum + arr[i]):
                solution_sum = abs(temp_sum + arr[i])
                solution1, solution2, solution3 = arr[i], arr[start], arr[end]
            
            if temp_sum >= target_sum:
                end -=1
            else:
                start += 1
    return solution1, solution2, solution3

print(*find_three_solutions())