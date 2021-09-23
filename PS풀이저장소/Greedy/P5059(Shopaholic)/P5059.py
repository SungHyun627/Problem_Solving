from sys import stdin

stdin = open('./input.txt', 'r')

#테스트 케이스
t = int(stdin.readline())

for _ in range(t):
    #최대로 할인할 수 있는 가격
    max_discount = 0
    # item 수
    n = int(stdin.readline())
    # item의 가격을 담을 리스트
    arr = list(map(int, stdin.readline().rstrip().split()))
    arr.sort(reverse=True)
    if n >= 3:
        for i in range(2, n, 3):
            max_discount += arr[i]
    print(max_discount)