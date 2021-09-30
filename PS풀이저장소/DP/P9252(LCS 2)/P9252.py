from sys import stdin

stdin = open('./input.txt', 'r')

str1 = stdin.readline().rstrip()
str2 = stdin.readline().rstrip()

arr = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

for i in range(len(str1) + 1):
    for j in range(len(str2) + 1):
        if i == 0 or j == 0:
            continue
        else:
            if str1[i-1] == str2[j-1]:
                arr[i][j] = arr[i-1][j-1] + 1
            else:
                arr[i][j] = max(arr[i-1][j], arr[i][j-1])

#LCS의 최대 길이
max_len = 0
for i in range(len(str1) + 1):
    max_i = max(arr[i])
    if max_len < max_i:
        max_len = max_i
print(max_len)

#LCS를 역순으로 담을 리스트
result = []

x, y = len(str1), len(str2)

while arr[x][y] != 0:
    if arr[x][y] == arr[x-1][y]:
        x -= 1
        continue
    elif arr[x][y] == arr[x][y-1]:
        y -= 1
        continue
    else:
        result.append(str1[x-1])
        x -= 1
        y -= 1

result.reverse()
print(''.join(result))