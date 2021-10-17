from sys import stdin

stdin = open('./input.txt', 'r')

n = int(stdin.readline())
#구하고자 하는 값
result = 0

#나온 알파벳들의 값을 저장하는 dict
alpabet = {}

for _ in range(n):
    str1 = stdin.readline().rstrip()
    #자릿 수
    num = 1
    for i in range(len(str1) - 1, -1, -1):
        if str1[i] not in alpabet:
            alpabet[str1[i]] = num
        else:
            alpabet[str1[i]] += num
        num *= 10

values = list(alpabet.values())
#내림차순으로 정렬
values.sort(reverse = True)

allocate_num = 9

for value in values:
    result += value * allocate_num
    allocate_num -= 1
print(result)