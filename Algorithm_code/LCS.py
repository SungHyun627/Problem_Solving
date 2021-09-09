from sys import maxsize


str1 = "ABCDEF"
str2 = "GBCDFE"

## 1. 최장공통 부분 문자열(Longest common SubString)

# 2차원 배열 생성, 1부터 비교하기 위해 마진 생성 
# 문자가 일치 할 때 LIS[i][j] = LIS[i-1][j-1] + 1
# 문자가 일치하지 않을 때 LIS[i][j] = 0
length_1 = len(str1)
length_2 = len(str2)

arr1 = [[0] * (length_2 + 1) for _ in range(length_1 + 1)]

for i in range(length_1 + 1):
    for j in range(length_2 + 1):
        if i == 0 or j == 0:
            continue
        if str1[i-1] == str2[j-1]:
            arr1[i][j] = arr1[i-1][j-1] + 1
        else:
            arr1[i][j] = 0
print(arr1)

max_longest_common_substring_length = 0

for i in range(1, length_1 + 1):
    if max_longest_common_substring_length < max(arr1[i]):
        max_longest_common_substring_length = max(arr1[i])
print(max_longest_common_substring_length)
    
## 2. 최장 공통 부분 수열(Longest common subsequence)
# 2차원 배열 생성, 1부터 비교하기 위해 마진 생성 
# 문자가 일치 할 때 LIS[i][j] = LIS[i-1][j-1] + 1
# 문자가 일치하지 않을 때 LIS[i][j] = LIS[i][j-1] + LIS[i-1][j]

arr2 = [[0] * (length_1 + 1) for _ in range(length_2 + 1)]

for i in range(length_1 + 1):
    for j in range(length_2 + 1):
        if i == 0 or j == 0:
            continue
        if str1[i-1] == str2[j-1]:
            arr2[i][j] = arr2[i-1][j-1] + 1
        else:
            arr2[i][j] = max(arr2[i-1][j], arr2[i][j-1])
print(arr2)

max_longest_common_subsequence_length = 0

for i in range(1, length_2 + 1):
    if max_longest_common_subsequence_length < max(arr2[i]):
        max_longest_common_subsequence_length = max(arr2[i])
print(max_longest_common_subsequence_length)



