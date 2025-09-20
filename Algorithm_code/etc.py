#재귀한도 설정
from sys import setrecursionlimit
setrecursionlimit(10 ** 6)

#math 모듈 (sqrt, gcd, factorial, pi, e)
from math import sqrt, gcd, factorial
print(sqrt(9), gcd(10, 15), factorial(5))

# 문장 합칠 때 join
string = ["hello", "how are you"] 
print('?'.join(string))

# 2차원 리스트 컴프리헨션
n = 3 
m = 4
array = [[0] * n for _ in range(m)]

# 무한으로 설정
INF = int(1e9)
print(INF)

## 리스트 (list)
# lst = []              # 빈 리스트
# lst = [1, 2, 3]
# lst = list(range(5))  # [0, 1, 2, 3, 4]

# 메서드	설명	시간복잡도
# append(x)	맨 뒤에 추가	O(1)
# pop()	맨 뒤 제거 후 반환	O(1)
# pop(i)	인덱스 i 제거	O(n)
# insert(i, x)	인덱스 i에 삽입	O(n)
# remove(x)	값 x 제거 (첫 번째만)	O(n)
# index(x)	값 x의 인덱스 반환	O(n)
# count(x)	x의 개수	O(n)
# sort()	정렬 (제자리)	O(n log n)
# sorted(lst)	정렬된 새 리스트 반환	O(n log n)
# reverse()	순서 뒤집기	O(n)
# copy()	얕은 복사	O(n)

#####

## 딕셔너리 (dict)

# d = {}  
# d = {"a": 1, "b": 2}
# d = dict(x=10, y=20)

### 메서드

# d[key]	key로 value 접근	O(1)
# d[key] = val	삽입/수정	O(1)
# del d[key]	key 삭제	O(1)
# d.get(key, default)	key 값 없으면 default 반환	O(1)
# d.keys()	모든 key 반환	O(n)
# d.values()	모든 value 반환	O(n)
# d.items()	(key, value) 쌍 반환	O(n)
# d.pop(key, default)	key 제거 + 값 반환	O(1)
# d.popitem()	임의의 (key, value) 제거	O(1)
# d.update(other)	다른 dict 병합	O(len(other))
# d.clear()	비우기	O(n)
# d.copy()	얕은 복사	O(n)

#####3
#셋 (set)

# s = set()  
# s = {1, 2, 3}  

## 메서드
# add(x)	원소 추가	O(1)
# remove(x)	원소 삭제 (없으면 에러)	O(1)
# discard(x)	원소 삭제 (없어도 안전)	O(1)
# pop()	임의 원소 제거 후 반환	O(1)
# clear()	비우기	O(n)
# copy()	얕은 복사	O(n)
# union(t)	합집합	O(n+m)
# intersection(t)	교집합	O(min(n,m))
# difference(t)	차집합	O(n)
# symmetric_difference(t)	대칭차집합	O(n)
# issubset(t)	부분집합 여부	O(n)
# issuperset(t)	상위집합 여부	O(n)