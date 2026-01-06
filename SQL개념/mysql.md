```sql
SELECT A.PRODUCT_CODE, (SUM(B.SALES_AMOUNT) * A.PRICE) AS SALES
	FROM PRODUCT A
	JOIN OFFLINE_SALE B
	ON A.PRODUCT_ID = B.PRODUCT_ID
	GROUP BY A.PRODUCT_CODE
ORDER BY SALES DESC, PRODUCT_CODE
```

동작 순서 : from and join ⇒ where ⇒ group by ⇒ having ⇒ select ⇒ order by

- **Order by** : 정렬, default는 오름차순
  - ORDER BY 컬럼명
  - 내림차순 : DESC
- **Between 날짜 and 날짜** - 날짜 사이
- **date_format :** DATE 타입 포매팅
  - 연-월-일(2021-12-03) : DATE_FORMAT(컬럼명, ‘%Y-%m-%d)
  - %c : 월
- **Ifnull:** 특정컬럼 값이 없는 경우 처리
  - IFNULL(TLNO, ‘NONE’)
- **Limit** : 조회할 레코드 수 제한
- **CASE - WHEN 조건 - THEN 반환값 - ELSE ‘WHEN 조건에 해당 안되는 경우 반환 값’ - END**
  ```sql
  CASE WHEN LENGTH IS NULL THEN 10 ELSE LENGTH END
  ```
- **Distinct** : 중복된 데이터를 하나만 count
- **Concat** : 문자열 합치기
- **Like** : 특정 문자열이 포함되었는지 확인
- **Count(\*)를 통해** 그룹별 행의 개수를 셀 수 있다.

- 날짜 관련

  1. **날짜 및 시간 데이터형**

  - **DATE -** 날짜 (YYYY-MM-DD 형식)
  - **DATETIME**: 날짜와 시간 (YYYY-MM-DD HH:MM형식)
  - **TIMESTAMP**: UTC 시간 기준으로 날짜와 시간
  - **TIME**: 시간 (HH:MM형식)

  1. **날짜와 시간 함수**

  - **CurDate()**: 현재 날짜를 반환합니다.
  - **Now()**: 현재 날짜와 시간을 반환합니다.
  - **Date()**: DATETIME에서 날짜 부분만 추출합니다.
  - **Time()**: DATETIME에서 시간 부분만 추출합니다.
  - **Year(), Month(), Day()**: 날짜에서 각각 연도, 월, 일을 추출합니다.
  - **Datediff(date1, date2)**: 두 날짜 간의 차이를 일수로 계산합니다.
    - date1-date2
  - **Date_add(date, Interval expr unit)**: 날짜에 특정 기간을 더합니다.
    ```sql
    SELECT DATE_ADD(NOW(), INTERVAL 10 DAY);  -- 10일 더하기
    ```
  - **Date_Sub(date, Interval expr unit)**: 날짜에서 특정 기간을 뺍니다.
    ```sql
    SELECT DATE_SUB(NOW(), INTERVAL 10 DAY);  -- 10일 빼기
    ```
  - **Str_to_date(str, format)**: 문자열을 날짜 형식으로 변환합니다.
    ```sql
    SELECT STR_TO_DATE('2024-01-01', '%Y-%m-%d');
    ```
  - **Date_format(date, format)**: 날짜를 지정된 형식으로 포맷합니다.
    ```sql
    SELECT DATE_FORMAT(NOW(), '%Y-%m-%d %H:%i:%s');
    ```

  1. **날짜 필터링 예시**

     - 특정 날짜 범위, 월, 연도의 데이터 조회

       ```sql
       SELECT *
       FROM your_table
       WHERE date_column BETWEEN '2024-01-01' AND '2024-12-31';

       SELECT *
       FROM your_table
       WHERE MONTH(date_column) = 1;  -- 1월 데이터

       SELECT *
       FROM your_table
       WHERE YEAR(date_column) = 2024;
       ```

     - 최근 30일간의 데이터 조회
       ```sql
       SELECT *
       FROM your_table
       WHERE date_column >= DATE_SUB(CURDATE(), INTERVAL 30 DAY);
       ```

  2. **날짜 관련 집계 예시**

     - 월별, 연도별 데이터 집계

       ```sql
       SELECT MONTH(date_column) AS month, COUNT(*) AS count
       FROM your_table
       GROUP BY MONTH(date_column);

       SELECT YEAR(date_column) AS year, COUNT(*) AS count
       FROM your_table
       GROUP BY YEAR(date_column);

       ```

- 문자열 관련

  1. **문자열 함수**

  - **Length(str)**: 문자열의 길이를 반환합니다.
  - **Char_length(str)**: 문자열의 문자 수를 반환합니다.
  - **Concat(str1, str2, ...)**: 여러 문자열을 결합합니다.
  - **SubString(str, start, length)**: 문자열의 일부를 추출합니다.
  - **Substring_index(str, sep, count)** : 특정 구분자를 기준으로 문자열을 잘라내고, 그 결과를 반환
    - **양수 count**: 문자열을 왼쪽부터 잘라서 첫 번째 구분자까지의 부분을 반환합니다.
      ```sql
      SELECT SUBSTRING_INDEX('apple,banana,cherry', ',', 2) AS First_Two_Fruits;
      -- 결과 : apple,banana
      ```
    - **음수 count**: 문자열을 오른쪽부터 잘라서 첫 번째 구분자까지의 부분을 반환
      ```sql
      SELECT SUBSTRING_INDEX('apple,banana,cherry', ',', -2) AS Last_Two_Fruits;
      -- 결과 : banana,cherry
      ```
  - **upper(str)**: 문자열을 대문자로 변환합니다.
  - **lower(str)**: 문자열을 소문자로 변환합니다.
  - **Trim(str)**: 문자열의 앞과 뒤의 공백을 제거합니다.
  - **Replace(str, from_str, to_str)**: 문자열에서 특정 문자열을 다른 문자열로 교체합니다.
  - **Instr(str, substr)**: 문자열 내에서 특정 문자열의 위치를 반환합니다. (첫 번째 문자의 위치는 1)
  - **find_in_set(str, list)**: 문자열이 주어진 리스트의 요소 중 하나로 존재하는지 확인합니다.
  - **left(str, length)**: 문자열의 왼쪽에서 지정된 길이만큼의 부분을 반환합니다.
  - **right(str, length)**: 문자열의 오른쪽에서 지정된 길이만큼의 부분을 반환합니다.

  ```sql
  SELECT LENGTH('Hello, World!');  -- 13
  SELECT CHAR_LENGTH('Hello');  -- 5
  SELECT CONCAT('Hello', ' ', 'World!');  -- 'Hello World!'
  SELECT SUBSTRING('Hello, World!', 1, 5);  -- 'Hello'
  SELECT SUBSTRING_INDEX('apple,banana,cherry', ',', 1) AS First_Friuts; -- 'apple'
  SELECT UPPER('hello');  -- 'HELLO'
  SELECT LOWER('HELLO');  -- 'hello'
  SELECT TRIM('   Hello   ');  -- 'Hello'
  SELECT REPLACE('Hello, World!', 'World', 'MySQL');  -- 'Hello, MySQL!'
  SELECT INSTR('Hello, World!', 'World');  -- 8
  SELECT FIND_IN_SET('b', 'a,b,c');  -- 2
  SELECT LEFT('Hello', 2);  -- 'He'
  SELECT RIGHT('Hello', 2);  -- 'lo'
  ```

  1. **문자열 관련 쿼리 예시**

     - 특정 문자열 포함된 데이터 조회
       - **Like** 문자열 패턴 매칭을 위해 사용되며, %와 \_ 통해 다양한 패턴을 지정할 수 있습니다.
       - 주로 where 절에서 조건을 설정하는 데 유용하며, 대소문자 구분 여부는 데이터베이스 설정에 따라 달라질 수 있습니다.
       - Not Like를 통해 포함되지 않을 때도 고려할 수 있다.
       ```sql
       SELECT *
       FROM your_table
       WHERE your_column LIKE '%search_string%';
       ```
     - 문자열 결합하여 새로운 컬럼 생성
       ```sql
       SELECT CONCAT(first_name, ' ', last_name) AS full_name
       FROM employees;
       ```
     - 문자열에서 특정 부분만 추출
       ```sql
       SELECT SUBSTRING(your_column, 1, 5)
       FROM your_table;
       ```
     - 대소문자 무시하고 데이터 조회
       ```sql
       SELECT *
       FROM your_table
       WHERE LOWER(your_column) = LOWER('SomeValue');
       ```
     - 문자열 길이로 데이터 필터링
       ```sql
       SELECT *
       FROM your_table
       WHERE LENGTH(your_column) > 10;
       ```
     - 문자열 교체
       ```sql
       SELECT REPLACE(your_column, 'old_value', 'new_value')
       FROM your_table;
       ```

  2. 문자열 조작을 위한 쿼리 예시

  - 특정 패턴으로 데이터 필터링
    ```sql
    SELECT *
    FROM your_table
    WHERE your_column REGEXP '^[A-Z]';  -- 대문자로 시작하는 문자열
    ```
  - 문자열을 공백으로 나누고 각 부분 조회

```sql
select a.member_name, b.review_text, date_format(b.review_date, '%Y-%m-%d')
	as review_date from member_profile a
	join rest_review b
	on a.member_id = b.member_id
	where a.member_id = (
		select member_id from rest_review
		group by member_id
		order by count(member_id) desc
		limit 1
	)
	order by b.review_date, b.review_text
```

### 참고링크

- [SELECT 쿼리 문법 순서 및 실행 순서](https://nohriter.tistory.com/129)
- [MYSQL JOIN](https://hongong.hanbit.co.kr/sql-%EA%B8%B0%EB%B3%B8-%EB%AC%B8%EB%B2%95-joininner-outer-cross-self-join/)
