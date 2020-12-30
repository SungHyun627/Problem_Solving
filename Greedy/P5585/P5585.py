from sys import stdin

stdin = open("./input.txt", 'r')

# 거스름 받을 돈
returned_money = 1000 - int(stdin.readline().rstrip())
# 잔돈 리스트
changes = [500, 100, 50, 10, 5, 1]
# 잔돈 개수
chagne_num = 0
for i in changes:
    chagne_num += returned_money // i
    returned_money %= i
    if returned_money == 0:
        break

print(chagne_num)
