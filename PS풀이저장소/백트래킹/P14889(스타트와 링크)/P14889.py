#P14889 스타트와 링크
from sys import stdin
stdin = open('./input.txt', 'r')

n = int(stdin.readline())
matrix = [list(map(int, stdin.readline().split())) for _ in range(n)]
start_sum = 0
link_sum = 0

# 최소 차
min_diff = 20*20*100
# 팀 구성 유무
in_team = [False] * n
# start team
start_team = []


def backtrack(num, k):
    global min_diff
    global start_sum
    global link_sum
    if num ==  n // 2:
        for i in range(n):
            if not in_team[i]:
                for j in range(n):
                    if i == j:
                        continue
                    if not in_team[j]:
                        link_sum += matrix[i][j]
        diff = abs(start_sum - link_sum)
        if min_diff > diff:
            min_diff = diff
        link_sum = 0
        return
    for i in range(k+1, n):
        if not in_team[i]:
            for j in start_team:
                start_sum += matrix[i][j]
                start_sum += matrix[j][i]
            in_team[i] = True
            start_team.append(i)
            backtrack(num+1, i)
            in_team[i] = False
            start_team.pop()
            for j in start_team:
                start_sum -= matrix[i][j]
                start_sum -= matrix[j][i]
backtrack(0, -1)
print(min_diff)
                

