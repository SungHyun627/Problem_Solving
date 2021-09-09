array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 1. 선택 정렬(Selection Sort) , O(N^2)
array1 = array[:]

for i in range(len(array1)):
    min_idx = i
    for j in range(i+1, len(array1)):
        if array1[j] < array1[min_idx]:
            min_idx = j
    array1[i], array1[min_idx] = array1[min_idx], array1[i]

print(array1)


# 2. 삽입 정렬(Insertion Sort), O(N^2)

array2 = array[:]

for i in range(1, len(array2)):
    for j in range(i, 0, -1):
        if array2[j] < array2[j-1]:
            array2[j], array2[j-1] = array2[j-1], array2[j]
        else:
            break
print(array2)

# 3. 퀵 정렬(Quick Sort), O(NlogN)

array3 = array[:]

def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)
print(quick_sort(array3))

#4. 계수 정렬 : 데이터의 개수가 백만개 이하일 때, 데이터간의 편차가 크지 않을때 사용하기 용이
# 데이터 개수 : N, 데이터 중 최대 크기 : K =? O(N+K)

array4 = array[:] + [0]
print(array4)
count = [0] * (max(array4) + 1)
for num in array4:
    count[num] += 1
print(count)
for i in range(len(count)):
    for _ in range(count[i]):
        print(i, end = ' ')

# 5. 병합 정렬(merge sort) => O(NlogN)