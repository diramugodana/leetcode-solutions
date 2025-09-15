class Solution:
    def rob(self, nums: List[int]) -> int:
        # s - subproblem -> dp[i] = max amount of money you can rob without alerting police from house [0 ... i]
        # b - base cases: dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])
        # r - 
        # base cases
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        # create dp table
        dp = [0] * n
        # populate dp table
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        return dp[-1]


        
