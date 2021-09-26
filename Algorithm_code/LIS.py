from bisect import bisect_left
##Longest Increasing Subsequence(LIS)

n = 6
arr = [10, 20, 10, 30, 20, 50]

#dp 방법 : O(n^2)
dp = [1]*n
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i],  dp[j] + 1)
print(dp)

#이진 탐색 방법 : O(nlogn)
#1. bisect_left 이용
Lis1 = [arr[0]]

end1 = 0

for i in range(1, n):
    if Lis1[end1] < arr[i]:
        Lis1.append(arr[i])
        end1 += 1
    else:
        ## 이진탐색
        idx = bisect_left(Lis1, arr[i])
        Lis1[idx] = arr[i]
    # print(Lis1)
print(Lis1)

#2. binary_search 함수 사용
def binary_search(array, target, start, end):
    while(start <= end):
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

Lis2 = [arr[0]]
end2 = 0

for i in range(1, n):
    if arr[i] > Lis2[end2]:
        Lis2.append(arr[i])
        end2 += 1
    else:
        idx = binary_search(Lis2, arr[i], 0, end2)
        Lis2[idx] = arr[i]
print(Lis2)


###LIS 구하는 법###
#모든 원소에 대하여 LIS내의 index를 구한 후
#LIS길이의 역순에 해당하는 인덱스부터 가장 빨리 해당 index가 나오는 element를 구한다.
#차례로 구한 후 reverse하면, 구하고자 하는 LIS가 나온다.


    