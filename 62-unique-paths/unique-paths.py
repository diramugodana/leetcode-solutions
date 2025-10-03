class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[i][j] = number of unique rightward or downward paths to cell (i, j)

        # base cases
        # dp[0][0] = 1. only one way to get to starting point
        # dp[0][j] and dp[i][0] = 1 too
        
        # recurrence relation = dp[i][j] = dp[i-1][j] + dp[i][j-1]

        

        # empty dp table
        dp = [[0] * n for _ in range(m)]
        # populate dp table
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]





        