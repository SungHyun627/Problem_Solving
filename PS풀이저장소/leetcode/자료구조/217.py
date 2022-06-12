#P217. Contains Duplicate
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return True if len(nums) != len(set(nums)) else False