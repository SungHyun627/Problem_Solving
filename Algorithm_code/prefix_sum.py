n = 5
data = [i for i in range(10, 60, 10)]
prefix_sum = [0]
sum_value = 0
for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

#left, right
left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left-1])