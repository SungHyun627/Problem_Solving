from sys import stdin

stdin = open('./input.txt', 'r')

str1 = stdin.readline().rstrip()
str2 = stdin.readline().rstrip()
str3 = stdin.readline().rstrip()

arr = [[[0] * (len(str3) + 1) for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]

for i in range(len(str1) + 1):
    for j in range(len(str2) + 1):
        for k in range(len(str3) + 1):
            if i == 0 or j == 0 or k == 0:
                continue
            if str1[i-1] == str2[j-1] == str3[k-1]:
                arr[i][j][k] = arr[i-1][j-1][k-1] + 1
            else:
                # print(i, j, k)
                arr[i][j][k] = max(arr[i-1][j][k], arr[i][j-1][k], arr[i][j][k-1])

max_len = 0
max_i = 0
for i in range(len(str1) + 1):
    for j in range(len(str2) + 1):
        max_j = max(arr[i][j])
        max_i = max(max_i, max_j)
    max_len = max(max_i, max_len)
print(max_len)
