from sys import stdin

stdin = open('./input.txt', 'r')

h, w = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
max_height = max(arr)
water_in_height = [0] * (max_height+1)

for i in range(1, max_height+1):
    for j in range(w):
        is_exist_right = False
        is_exist_left = False
        if arr[j] >= i:
            continue
        for k in range(j):
            if arr[k] >= i:
                is_exist_left = True
                break
        for p in range(j+1, w):
            if arr[p] >= i:
                # print("p", p, j)
                is_exist_right = True
                break
        if is_exist_left and is_exist_right:
            # print(i, j)
            water_in_height[i] += 1
print(sum(water_in_height))