class Solution:
    def fib(self, n: int) -> int:
        # subproblem -> dp[i] = obtained by adding up the two previous numnbers
        # base cases -> F(0) = 0, F(1) = 1
        # recurrence relation = F(n) = F(n - 1) + F(n - 2), for n > 1.

        if n == 0:
            return 0
        if n == 1:
            return 1

        # build dp table
        dp = [0] * (n + 1)
        # populate dp table
        dp[0], dp[1] = 0, 1
        for i in range(2, n+1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

        