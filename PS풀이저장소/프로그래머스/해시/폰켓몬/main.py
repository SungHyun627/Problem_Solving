def solution(nums):
    answer = 0
    n = len(nums)
    nums = set(nums)
    return n // 2 if (n // 2) <= len(nums) else len(nums)