class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        for i  in range(32):
            if (n & (1 << i)): result += 1
        return result
        