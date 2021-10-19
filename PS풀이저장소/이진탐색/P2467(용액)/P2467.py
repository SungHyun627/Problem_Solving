from sys import stdin
from bisect import bisect_left
stdin = open('./input.txt', 'r')

n = int(stdin.readline())

arr = list(map(int, stdin.readline().split()))

def make_close_netural():
    if arr[-1] < 0:
        return arr[-2], arr[-1]
    
    if arr[0] > 0:
        return arr[0], arr[1]
    
    a, b = int(1e9), - int(1e9)
    acidity = 2 * int(1e9)
    
    for i in range(len(arr)):
        # print(i, acidity)
        sum1 = 2 * int(1e9)
        sum2 = 2 * int(1e9)
        
        if arr[i] > 0:
            if i != n-1:
                if arr[i] + arr[i+1] < abs(acidity):
                    return arr[i], arr[i+1]
            return a, b

        x = arr[i]
        idx = bisect_left(arr, -x)
        
        if idx-1 != i:
            sum1 = arr[i] + arr[idx-1]
        if idx <= n-1:
            sum2 = arr[i] + arr[idx]

        if sum1 == 0:
            return arr[i], arr[idx-1]
        elif sum2 == 0:
            return arr[i], arr[idx]
        else:
            if abs(sum1) > abs(sum2):
                if abs(sum2) < abs(acidity):
                    acidity = sum2
                    a, b = arr[i], arr[idx]
            else:
                if abs(sum1) < abs(acidity):
                    acidity = sum1
                    a, b = arr[i], arr[idx-1]
    return a, b

print(*make_close_netural())