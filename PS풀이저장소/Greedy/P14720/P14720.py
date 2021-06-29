from sys import stdin

stdin = open('./input.txt', 'r')
# 딸기 -> 초코 -> 바나나 순으로 마신다.

drunken_milk_num = 0
drunken_milk = 0

# 우유 가게의 수
n = map(int, stdin.readline().rstrip().split())

# 우유 가게 정보
# 딸기 우유 : 0, 초코 우유 : 1, 바나나 우유 : 2
milk_list = list(map(int, stdin.readline().rstrip().split()))

for milk in milk_list:
    if milk == drunken_milk:
        drunken_milk_num +=1
        drunken_milk +=1
        if drunken_milk > 2:
            drunken_milk = 0

print(drunken_milk_num)