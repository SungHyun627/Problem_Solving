#투 포인터

#특정합을 가지는 부분 연속 수열 개수 찾기
n = 5
m = 5
data = [1, 2, 3, 2, 5]

count = 0
interval_sum = 0
end = 0

for start in range(n):
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]

print(count)

# 정렬되어 있는 두 리스트의 합집합
p, q = 3, 4
a = [1, 3, 5]
b = [2, 4, 6, 8]
results = [0]*(p+q)
i = 0 
j = 0
k = 0

while i < p or j < q:
    # b가 다 처리되었거나 a의 원소가 더 작을 때
    if j >= q or (i < p and a[i] <= b[j]):
        results[k] = a[i]
        i += 1
    else:
        results[k] = b[j]
        j += 1
    k += 1
print(results)
