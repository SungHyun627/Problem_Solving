class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_len = len(nums)
        index_value = {}
        for x, y in enumerate(nums):
            index_value[y] = x
        for i in range(nums_len):
            a = target - nums[i]
            if a in index_value and index_value[a] != i:                
                return [i, index_value[a]]
                