from collections import Counter, deque

number = [1, 1, 3, 4, 5, 3, 4]

# 1. Counter : iterable 객체가 주어졌을 때, 해당 객체 내부의 원소가 몇번 등장했는지를 알려준다.
counter = Counter(number)
print(counter)
print(counter[1])
# 사전 자료형으로 변환
print(dict(counter))

# 2. deque
# 삽입 : append, appendleft / 삭제 : pop, popleft
queue = deque(number)
print(queue.popleft(), queue.pop())