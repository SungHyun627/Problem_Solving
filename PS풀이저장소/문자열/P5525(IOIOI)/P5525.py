from sys import stdin

stdin = open('./input.txt', 'r')

n = int(stdin.readline())
m = int(stdin.readline())
s = list(stdin.readline())

start_from_i = False
pattern_num = []
count = 0
temp_char = ''
num = 0

for i in range(m):
    if not start_from_i:
        if s[i] == 'I':
            count +=1
            start_from_i = True
            temp_char = s[i]
        continue
    if temp_char != s[i]:
        temp_char = s[i]
        count += 1
        if i == m-1:
            pattern_num.append(count)
    else:
        if count != 1:
            pattern_num.append(count)

        if temp_char == 'I':
            count = 1
        else:
            start_from_i = False
            count = 0

# print(pattern_num)
for k in pattern_num:
    if k < (2*n+1):
        continue
    num += int((k - (2*n + 1)) // 2) + 1
print(num)