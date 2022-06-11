class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1] * (n+1)
        if n == 1:
            return 1
        else:
            for i in range(2, n+1):
                dp[i] = dp[i-1] + dp[i-2]          
            return dp[n]