from functools import reduce
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numsLen = len(nums)
        answer = [1] * numsLen
        lprod, rprod = 1, 1
        
        for i in range(numsLen):
            answer[i] *= lprod
            lprod *= nums[i]
        for i in range(numsLen-1, -1, -1):
            answer[i] *= rprod
            rprod *= nums[i]
        
        return answer