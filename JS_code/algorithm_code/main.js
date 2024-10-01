const arr2 = [
  [1, 2],
  [4, 7],
  [-1, 3],
  [8, 6],
];

const arr1 = [2, 3, 1, 32, 5];
arr1.sort((a, b) => a - b);
console.log(arr1);
arr2.sort((a, b) => a[0] - b[0]);
console.log(arr2);

const str1 = 'abcdefghijklmnopc';

console.log(str1);
console.log(str1.slice(2));

console.log(str1.indexOf('c'));

/**    

## 문자열

1. 문자열 자르기 : substring, slice
- subString(시작, 종료) => 시작 ~ 종료-1
- slice(시작, 종료) => 시작 ~ 종료-1

2. 문자열 대소문자 및 타입 변환
- toUpperCase(대문자), toLowerCase(소문자)
- charCodeAt(문자 => 아스키코드), fromCharCode(아스키코드 => 문자)
- toString(문자열)

3. 문자열 파싱 및 변환 : indexOf, includes, replace, replaceAll, split, repeat 
- indexOf(찾는 문자열) => 없으면 -1 반환
- includes(찾는 문자열)
- replace('찾는 문자열', '바꿀 문자열') => 모든 문자열을 바꾸고 싶을 경우 replaceAll 사용
- split(기준 문자열)
- repeat(반복 횟수)

*/

/**
 
## Map 객체(a)
Map은 삽입 순서를 기억
- map 생성 => let a = new Map();
- set: 값 추가 => a.set(key, value)
- get : 값 조회 => a.get(key)
- has : 값 존재 유무 확인 => a.has(key)
- delete : 값 지우기 => a.delete(key)
- size : 개수 => a.size
- 객체 순환 : for (let [key, value] of map 객체)
- map 정렬 => map 객체를 배열로 변환 => 정렬 => map 객채로 변환

 */

let a = new Map();
const key = [2, 3];
a.set(1, 2);
a.set(key, new Map());

console.log(a.delete(key));
console.log(a);

/** Set(b) : 중복 허락 x
 - 생성 : let b = new Set();
 - add : 값 추가 
 - has : 값 있는 지 체크
 - delete : 값 지우기
 - size : 요소 개수
 - 객체 순환 : for ( let value of set 객체)
 - set 정렬 => set 객체를 배열로 변환 => 정렬 => set 객채로 변환
  
 */

/**
  배열 Method : map, filter, reduce, forEach
  
  배열 생성
  - let arr = new Array(배열 크기).fill(content)
  - Array.from( { length: 5 }, (value, index) => index)
  - 다른 배열 활용 => Array.from( arr1, (el, index) => el * 2)
  */

/**
 *  V 순열, 조합
 *  V 서로소
 *  V 다익스트라
 *  V 이분탐색
 *  */
