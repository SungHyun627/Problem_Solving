from functools import reduce

a = [1, 2, 3]
b = ['apple', 'watermelon', 'water']
c = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
d = [(0, 1), (3, 6), (2, 5), (8, 1), (1, 3)]
# 1. map : interable한 객체의 각 요소 처리
"""
람다 표현식 안에서는 if/else를 사용할 때 :를 붙이지 않는다.
람다 표현식 안에서는 if를 썼으면 else를 반드시 써준다. elif 사용을 못한다.

"""
print(list(map(lambda x : str(x) if x % 3 == 0 else x, a)))
print(list(map(lambda x, y : str(x) + y, a, b)))

# 2. filter : iterable한 객체에서 특정 조건에 맞는 요소만 가져올 때 사용, filter내부의 함수의 반환값이 True일때 해당 요소를 가져온다.
def func(x):
    return x > 5 and x < 10
print(list(filter(lambda x : x > 5 and x < 10, c)))

# 3. reduce : iterable한 객체의 각 요소를 지정된 함수로 처리한 뒤 이전 결과와 누적해서 반환하는 함수
def f(x, y):
    return x + y
print(reduce(f, c))
print(reduce(lambda x, y : x + y, c))

d.sort(key=lambda x: x[1])
print(d)