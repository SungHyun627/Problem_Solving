from sys import stdin

#데이터 개수, 변경횟수, 구간 합 계산 횟수
n, m, k = map(int, stdin.readline().split())

#전체 데이터의 개수 최대 1,000,000개
arr = [0] * (n+1)
tree = [0] * (n+1)

#i번째까지의 누적합
def prefix_sum(i):
    result = 0
    while i > 0:
        result += tree[i]
        #0이 아닌 마지막 비트만큼 빼면서 이동
        i -= (i&-i)
    return result

#i번째 수를 diff만큼 더하는 함수
def update(i, diff):
    while i <= n:
        tree[i] += diff
        #0이 아닌 마지막 비트만큼 더하면서 이동
        i += (i&-i)

# Start부터 end까지의 구간 합을 계산하는 함수
def interval_sum(start, end):
    return prefix_sum(end) - prefix_sum(start-1)

for i in range(1, n+1):
    x = int(stdin.readline())
    arr[i] = x
    update(i, x)

for i in range(m+k):
    a, b, c = map(int, stdin.readline().split())
    # update 연산인 경우
    if a == 1:
        update(b, c - arr[b])
        arr[b] = c
    # 구간 합인 경우
    else:
        print(interval_sum(b, c))