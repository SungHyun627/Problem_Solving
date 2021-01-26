from sys import stdin

stdin = open('./input.txt', 'r')
# m : 가치의 총합
m = int(stdin.readline())
# 화폐리스트
moneyList = [2, 5]
# 각 화폐가치에 대한 최소한의 화폐개수를 저장하는 리스트
d = [100000] * (m + 1)
d[0] = 0

for i in range(2):
    for j in range(moneyList[i], m + 1):
        if d[j - moneyList[i]] != 100000:
            d[j] = min(d[j], d[j - moneyList[i]] + 1)

print(d[m]) if d[m] != 100000 else print(-1)
