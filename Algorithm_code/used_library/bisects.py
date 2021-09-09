#이분(이진) 탐색에 사용
from bisect import bisect_left, bisect_right

# 정렬된 순서를 유지하며 데이터를 삽입할 가장 오른쪽, 왼쪽 index 찾을 때 사용
# 시간복잡도 : O(logN)
a = [1,2,4,4,8]
x = 4
print(bisect_left(a, x), bisect_right(a, x))