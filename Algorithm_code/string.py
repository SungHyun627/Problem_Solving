# 문자열 조작
# 문자열 조작 메서드 체이닝 가능
s = "Hello, World!"
fruits = ['apple', 'pear', 'grape', 'pineapple', 'orange']
ex = '??Python???'
t = 'stars'
# 1. 문자열(replace) / 문자(translate, maketrans) 바꾸기

print(s.replace('World!', 'good'))
table = str.maketrans('aeiou', '12345')
print(s.translate(table))

# 2. 문자열 분리(split)
print(s.split())

# 3. 문자열 연결(join)
print('-'.join(fruits))

# 4. 문자열 대소문자 (upper, lower)
print(s.upper(), s.lower())

# 5. 문자열 삭제 lstrip('삭제할 문자')/rstrip('삭제할 문자')/strip('삭제할 문자'), default는 공백
print(ex.lstrip('?'), ex.rstrip('?'), sep = '\n')

# 6. 문자열 정렬 ljust(길이), rjust(길이), center(길이), 남는 공간이 홀수이면 왼쪽에 한칸더 들어간다
print(t.ljust(10))
print(t.rjust(10))

# 7. 문자열 0 채우기 zfill(길이) => 왼쪽에 0 채우기
print(t.zfill(10))

# 8. 문자열 찾기 find, rfind => 없으면 -1 반환 / index, rindex => 없으면 error
print(t.find('s'))
print(t.rfind('s'))
print(t.index('rs'))

# 9. 문자열 개수 세기 count
print(t.count('s'))

# 10. 문자열 포매팅으로 정렬하기 / 숫자 채우기

#{인덱스:<길이}.format{값} 왼쪽(<), 오른쪽(>)
print('{0:>10}'.format('python'))
#'{인덱스:0개수d}.format'
print('{0:03d}'.format(35))
print('{0:08.2f}'.format(190.2))

#{인덱스:[[채우기]정렬][길이][.자릿수][자료형]}
print('{0:0>10.2f}'.format(15))

# 11. 문자열 판단
# 특정 문자열이 포함되어 있는 지 판단 , match(처음부터 매칭되는지 판단), search(문자 일부분 매칭 되는지 판단)
import re
# 앞 : ^, 뒤: $
print(re.search('^hello', 'hello, world'))
print(re.search('world$', 'hello, world'))

# 범위 판단 * : 0개 이상, + : 1개 이상, ? : 0개이거나 1개, .: 아무거나, ^: 포함되지 않을 때 ex) [0-9a-zA-Z]*, [0-9]+, [^0-9]
# 문자개수 {3}, {시작개수, 끝 개수}
# 공백 처리할 때 [0-9 ]
if not re.search('(44)+', '12das344'):
    print('None')
# 많이 사용할 때 예시
p = re.compile('[0-9]+')
print(p.search('hello12h1'))
# 패턴에 매칭되는 모든 문자열을 가져올 때
print(p.findall('hello12h1'))
#  re.match('[a-z]+(.[a-z]+)*$', 'hello')