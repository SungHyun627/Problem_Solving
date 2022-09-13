def solution(sizes):
    answer = 0
    sizes = [sorted(size, reverse = True) for size in sizes]
    x, y = max(list(size[0] for size in sizes)), max(list(size[1] for size in sizes))
    print(sizes, x, y)
    return x * y