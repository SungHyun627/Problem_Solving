from sys import stdin

stdin = open('./input.txt', 'r')

#스위치 수
n = int(stdin.readline().rstrip())

#스위치 리스트
switch_list = list(map(int, stdin.readline().rstrip().split()))

# 학생 수
m = int(stdin.readline().rstrip())

# 0을 1로, 1을 0으로 변환하는 함수
def one_zero (k):
    if k == 0:
        k = 1
    else:
        k = 0
    return k

for _ in range(m):
    # 성별, 받은 수
    a, b = map(int, stdin.readline().rstrip().split())
    # 남자일 경우
    if a == 1:
        for i in range(b-1, n, b):
            switch_list[i] = one_zero(switch_list[i])
    # 여자일 경우
    else:
        switch_list[b-1] = one_zero(switch_list[b-1])
        num = 1
        while(1):
            if b - 1 - num < 0 or b - 1 + num >= n:
                break
            if switch_list[b-1-num] == switch_list[b-1+num]:
                switch_list[b-1-num] = one_zero(switch_list[b-1-num])
                switch_list[b-1+num] = one_zero(switch_list[b-1+num])
            else:
                break
            num += 1
for i in range(0, n//20):
    print(*switch_list[20*i:20*(i+1)], sep =" ")
print(*switch_list[20*(n//20):], sep = " ")