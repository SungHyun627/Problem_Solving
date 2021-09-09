from sys import stdin

stdin = open('./input.txt', 'r')
str1 = stdin.readline().rstrip()
str2 = stdin.readline().rstrip()

lcs = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
# print(lcs)

for i in range(len(str1) + 1):
    for j in range(len(str2) + 1):
        # print(i, j)
        if i == 0 or j == 0:
            continue
        if str1[i-1] == str2[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

max_length = 0
# print(lcs)

for i in range(1, len(str1) + 1):
    if max_length < max(lcs[i]):
        max_length = max(lcs[i])
print(max_length)
