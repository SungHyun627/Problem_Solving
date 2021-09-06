from sys import stdin

stdin = open('./input.txt', 'r')

#용액의 수
n = int(stdin.readline())

#용액의 특성값
solution_acidity = list(map(int, stdin.readline().rstrip().split()))
solution_acidity.sort()

#투 포인터
start = 0
end = n-1

#두 용액의 산성도
solution1_acidity = 0
solution2_acidity = 0
#두 용액의 산성도의 합
acidity_sum = 0
close_to_zero_sum = 2000000000

#산성도의 합
while start != end:
    # print(start, end)
    acidity_sum = solution_acidity[start] + solution_acidity[end]
    if acidity_sum == 0:
        solution1_acidity = solution_acidity[start]
        solution2_acidity = solution_acidity[end]
        break
    
    if abs(close_to_zero_sum) > abs(acidity_sum):
        solution1_acidity = solution_acidity[start]
        solution2_acidity = solution_acidity[end]
        close_to_zero_sum = acidity_sum

    if acidity_sum < 0:
        start += 1
    else:
        end -= 1
    # print(solution1_acidity, solution2_acidity)

# print(n, solution_acidity)
print(solution1_acidity, solution2_acidity)