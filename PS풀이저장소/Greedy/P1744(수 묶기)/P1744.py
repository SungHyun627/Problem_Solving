from sys import stdin
from bisect import bisect_left, bisect_right

stdin = open('./input.txt', 'r')

n = int(stdin.readline())
arr = list(int(stdin.readline()) for _ in range(n))

#오름차순 정렬
arr.sort()
#총합
arr_sum = 0

zero_num = bisect_right(arr, 0) - bisect_left(arr, 0)
one_num = bisect_right(arr, 1) - bisect_left(arr, 1)
positive_num = n - bisect_left(arr, 1)
negative_num = bisect_right(arr, -1)

# print(zero_num, one_num, positive_num, negative_num)

#음수가 있다면
if negative_num:
   #홀수개 있다면 
   if negative_num % 2 == 1:
       for i in range(0, negative_num - 1, 2):
           arr_sum += arr[i] * arr[i+1]
        
       #0이 없다면
       if not zero_num:
            arr_sum += arr[negative_num - 1]
    #짝수개 있다면
   else:
        for i in range(0, negative_num, 2):
            arr_sum += arr[i] * arr[i+1]
        

#0과 1, 음수가 아닌 양의 정수의 개수
num = positive_num - one_num

for k in range(n-1, n-num, -2):
    arr_sum += arr[k]*arr[k-1]

#num이 홀수라면
if num % 2 == 1:
    arr_sum += arr[n-num]

#1의 개수 만큼 덧셈
arr_sum += (one_num)

print(arr_sum)