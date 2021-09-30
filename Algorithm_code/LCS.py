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

#Longest Common Subsequence 구하는 방법
# 1. LCS 배열의 가장 마지막 값에서 시작 / 결과값을 저장할 result 배열을 준비
# 2. LCS[i - 1][j]와 LCS[i][j - 1] 중 현재 값과 같은 값을 탐색
# # 2-1. 만약 같은 값이 있다면 해당 값으로 이동
# 2-2. 만약 같은 값이 없다면 result배열에 해당 문자를 넣고 LCS[i -1][j - 1]로 이동
# 2번 과정을 반복하다가 0으로 이동하게 되면 종료. result 배열의 역순 출력.

