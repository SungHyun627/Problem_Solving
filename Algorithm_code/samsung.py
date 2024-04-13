n, m = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]

for i in range(n):
  print(board[i])
print('------------')

# 1. zip 활용
## 시계방향 90도
arr1 = list(map(list,zip(*board[::-1])))
for i in range(4):
  print(arr1[i])

print('------------')
## 시계방향 180도
arr2 = list(x[::-1] for x in board[::-1])
for i in range(4):
  print(arr2[i])

print('------------')
## 시계방향 270도
arr3 = [*map(list, zip(*board))][::-1]
for i in range(4):
  print(arr3[i])

print('-------------------------------------')


## 2. 정사각형 index
## 시계방향 90도
n_arr1 = [[0] * n for _ in range(n)]
for i in range(n):
  for j in range(n):
    n_arr1[j][n-i-1] = board[i][j]
for i in range(n):
  print(n_arr1[i])  
print('------------')

## 시계방향 180도
n_arr2 = [[0] * n for _ in range(n)]
for i in range(n):
  for j in range(n):
    n_arr2[n-i-1][n-j-1] = board[i][j]
for i in range(n):
  print(n_arr2[i])  
print('------------')

## 시계방향 270도
n_arr3 = [[0] * n for _ in range(n)]
for i in range(n):
  for j in range(n):
    n_arr3[n-j-1][i] = board[i][j]
for i in range(n):
  print(n_arr3[i])  
print('------------')


## 3. 직사각형 index
## 시계방향 90도
m_arr1 = [[0] * n for _ in range(m)]
### 범위주의
for i in range(n):
  for j in range(m):
    m_arr1[j][n-i-1] = board[i][j]
for i in range(m):
  print(m_arr1[i])  
print('------------')

## 시계방향 180도
m_arr2 = [[0] * m for _ in range(n)]
### 범위주의
for i in range(n):
  for j in range(m):
    m_arr2[n-i-1][m-j-1] = board[i][j]
for i in range(n):
  print(m_arr2[i])  
print('------------')

## 시계방향 270도
m_arr3 = [[0] * n for _ in range(m)]
### 범위주의
for i in range(n):
  for j in range(m):
    m_arr3[m-j-1][i] = board[i][j]
for i in range(m):
  print(m_arr3[i])  
print('------------')

def rotate_90(sx, sy, length):
  
    # 정사각형을 시계방향으로 90도 회전
    for x in range(sx, sx + length):
        for y in range(sy, sy + length):
            # 1단계 : (0,0)으로 옮겨주는 변환을 진행함
            ox, oy = x - sx, y - sy
            # 2단계 : 90도 회전했을때의 좌표를 구함
            rx, ry = oy, length - ox - 1
            # 3단계 : 다시 (sx,sy)를 더해줌
            new_arr[sx + rx][sy + ry] = board[x][y]

    print(new_arr)
    # new_arr 값을 현재 board에 옮겨줌
    for x in range(sx, sx + length):
        for y in range(sy, sy + length):
            board[x][y] = new_arr[x][y]


from sys import stdin
from collections import deque

arr = [1, 2, 3, 4]

## 1. 순열
visited = [False] * len(arr)
ans1 = []


def permutations(n, new_arr):
    global arr
    # 순서 상관 0, 중복 X
    if len(new_arr) == n:
        ans1.append(new_arr)
        return
    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = True
            permutations(n, new_arr + [arr[i]])
            visited[i] = False


permutations(2, [])
print(ans1)

## 2. 중복순열
ans2 = []

def product(n, new_arr):
    global arr
    # 순서 상관 0, 중복 0
    if len(new_arr) == n:
        ans2.append(new_arr)
        return
    for i in range(len(arr)):
        product(n, new_arr + [arr[i]])

product(2, [])
print(ans2)

## 3. 조합
ans3 = []

def combinations(n, new_arr, c):
    # 순서 상관 X, 중복 X
    if len(new_arr) == n:
        ans3.append(new_arr)
        return
    for i in range(c, len(arr)):
        combinations(n, new_arr + [arr[i]], i + 1)


combinations(2, [], 0)
print(ans3)


## 4. 중복조합
ans4 = []
def combinations_with_replacement(n, new_arr, c):
    # 순서 상관 X, 중복
    if len(new_arr) == n:
        ans4.append(new_arr)
        return
    for i in range(c, len(arr)):
        combinations_with_replacement(n, new_arr + [arr[i]], i)


combinations_with_replacement(2, [], 0)
print(ans4)



## 토네이도
arr = [[0] * 5 for _ in range(5)]


def tornado():
    global arr
    d = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    y = len(arr) // 2
    x = len(arr) // 2
    num = 0  # 칸에 채워넣을 값
    dist = 1
    d_idx = 0  # 서 남 동 북 순서
    move_count = 0  # 2가 되면 dist 길이가 1 늘어나고 move_count는 다시 0으로 초기화
    while True:
        for _ in range(dist):
            dy, dx = d[d_idx]
            Y = dy + y
            X = dx + x
            if (Y, X) == (0, -1):  # 0행 -1열이 토네이도가 모두 끝나고 나서의 위치임
                return
            num += 1
            arr[Y][X] = num
            y = Y
            x = X
        move_count += 1
        d_idx = (d_idx + 1) % 4
        if move_count == 2:
            dist += 1
            move_count = 0


tornado()
for i in range(5):
    print(arr[i])


### 밖 => 안
def solution(n):
    if n == 1:
        return [[1]]

    answer = [[0 for j in range(n)] for i in range(n)]  # 배열 초기화

    x = 0
    y = 0
    d_idx=0

    for i in range(n * n):
        answer[x][y] = i + 1
        if d_idx == 0:
            y += 1
            if y == n - 1 or answer[x][y + 1] != 0:  # 맨 끝에 도달했거나 가려는 곳에 이미 값이 있으면 방향 전환
                d_idx = 1
        elif d_idx == 1:
            x += 1
            if x == n - 1 or answer[x + 1][y] != 0:
                d_idx = 2
        elif d_idx == 2:
            y -= 1
            if y == 0 or answer[x][y - 1] != 0:
                d_idx = 3
        elif d_idx == 3:
            x -= 1
            if x == n - 1 or answer[x - 1][y] != 0:
                d_idx = 0

    return answer


arr=solution(5)
for i in range(len(arr)):
    print(arr[i])


### 중력
def gravity():
    n = len(arr)
    m = len(arr[0])
    for i in range(n - 1):
        for j in range(m):
            p = i
            # 현재칸이 아래로 내려갈 수 있다면 그 윗줄도 한 칸 씩 연쇄적으로 내려와야함
            while 0 <= p and arr[p][j] == 1 and arr[p + 1][j] == 0:
                arr[p][j], arr[p + 1][j] = arr[p + 1][j], arr[p][j]
                p -= 1

### 한칸씩 이동
from sys import stdin
from collections import deque

stdin = open('./input.txt', 'r')

N, M, R = map(int, stdin.readline().split())
print(N, M, R)

arr = []
new_arr = [[0] * M for _ in range(N)]
q = deque()

for i in range(N):
    arr.append(list(map(int, stdin.readline().split())))

loops = min(N, M) // 2
for i in range(loops):
    q.clear()
    q.extend(arr[i][i:M-i])
    q.extend([row[M-i-1] for row in arr[i+1:N-i-1]])
    q.extend(arr[N-i-1][i:M-i][::-1])
    q.extend([row[i] for row in arr[i+1:N-i-1]][::-1])
    
    q.rotate(-R)
    
    for j in range(i, M-i):                 # 상
        new_arr[i][j] = q.popleft()
    for j in range(i+1, N-i-1):             # 우
        new_arr[j][M-i-1] = q.popleft()
    for j in range(M-i-1, i-1, -1):           # 하
        new_arr[N-i-1][j] = q.popleft()  
    for j in range(N-i-2, i, -1):           # 좌
        new_arr[j][i] = q.popleft()    

print(new_arr)