a = [1, 2, 3, 0]
b = [4, 5, 6, 7]
c = ['apple', 'banana', 'watermelon']
# 1. any : Iterable한 자료형 중 하나라도 참이면 True
print(any(a))

# 2. all : Iterable한 자료형 중 모두 참이면 True
print(all(a))

# 3. zip : 동일한 개수로 이루어진 자료형을 묶어주는 역할
print(type(zip(a,b)))
print(list(zip(a, b)))

# 4. enumerate : 순서가 있는 자료형의 인덱스, 값을 포함하는 enumerate 객체 반환
print(type(enumerate(c)))
print(list(enumerate(c)))

# 5. eval : 실행 가능한 문자열을 입력받아 실행한 결과값을 반환
print(eval('1+2'))