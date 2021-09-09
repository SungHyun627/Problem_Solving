import heapq

# heap을 사용하는경우
# 데이터를 우선순위에 따라 처리하고 싶을 때 / (개선된 다익스트라 알고리즘에서 사용)
# 파이썬과 자바에서는 최소힙이 default, C++에서는 최대힙이 default
# 최대힙을 사용하는경우 음수를 붙여 사용한다.
# heap는 완전이진트리로 삽입, 삭제에 시간복잡도 : O(lgn)
# heappush, heappop, heappushpop(합친것), heapify

a = [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]
heap = []
result = []
for value in a:
    heapq.heappush(heap, -value)
print(heap)
while heap:
    result.append(-heapq.heappop(heap))
print(result)


