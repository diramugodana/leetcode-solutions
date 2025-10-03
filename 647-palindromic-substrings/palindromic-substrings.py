class Solution(object):
    def countSubstrings(self, s):
        # return number of substrings that are palindromes
        # every char is on palindrome

        # so we can count by number of characters
        # base cases 
        # if len(s) = 1 : return True
        # if len(s) = 2 : return True if s[0] == s[i]
        # if len(s) = 3 : return True if s[0] == s[-1], middle doesnt matter
         # subproblem
        # dp[i][j] True if s[i...j] is a palindrome
        resLen = 0
        n = len(s) 

        dp = [[False] * n for _ in range(n)]

        for i in range(n-1, -1, -1): # i goes backward
            for j in range (i, n): # j goes forward, from i
        # if len(s)
        # odd length palindromes
            # condition
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1] == True):
                    dp[i][j] = True
                    resLen += 1
        return resLen
            
    #     # expand around center
    #     count = 0
    #     for i in range(len(s)):
    #         # odd length
    #         count += self.expandAroundCenter(s,i, i)
    #         # even length
    #         count += self.expandAroundCenter(s, i, i+1)
    #     return count

    # def expandAroundCenter(self, s, l, r):
    #     localCount = 0
    #     while l >=0 and r < len(s) and s[l] == s[r]:
    #         localCount += 1
    #         l -= 1
    #         r += 1
    #     return localCount
