import math

class Solution:
    def numSquares(self, n):
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = i
            
            for j in range(1, int(math.sqrt(i)) + 1):
                if i - j*j >= 0:
                    dp[i] = min(dp[i], dp[i - j*j] + 1)

        return dp[n]
