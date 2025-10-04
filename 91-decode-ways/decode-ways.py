class Solution:
    def numDecodings(self, s: str) -> int:
        # return no. of ways to decode a message
        # if s begins with 0, return 0
        # if n is 0, return 0
        # valid one digit btwn 1 and 9 inclusive
        # valid two digit message btwn 10 ans 26 inclusive

        # base cases
        n = len(s)
        # 213 -> n = 3, s = '213'

        dp = [0] * (n+1) 
        # populate dp table
        dp[0] = 1
        dp[1] = 1 if s[0] != "0" else 0

        for i in range(2, n+1):
            one = int(s[i-1])
            two = int(s[i-2:i])

            if 1 <= one <= 9:
                dp[i] += dp[i-1]
            if 10 <= two <= 26:
                dp[i] += dp[i-2]
        return dp[n]


        
        