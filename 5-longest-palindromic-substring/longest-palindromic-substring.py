class Solution(object):
    def longestPalindrome(self, s):
       # DP approach
       # example
       # abba
       # len 1 = a, b, b, a -> all palindromes, maxLen = 1
       # len 2 = ab,bb, ba -> maxLen = 2 (bb)
       # len 3 = abb, bba -> maxLen = 2
       # len 4 = abba -> maxLen = 4 (abba)
        n = len(s)
        if n == 0:
            return ""
        
        # construct dp table
        dp = [[False] * n for _ in range(n)]

        start = 0 # start of longest palindrome
        max_len = 1 # len longest palindrome (at least 1)

        # base case 1: len 1 substrings
        for i in range(n):
            dp[i][i] = True

        # len 2 substrings
        # palindrome if both characters match
        for i in range(n - 1): # to avoid index out of bound error
            if s[i] == s[i + 1]:
                dp[i][i+1]  = True # updating dp table
                start = i
                max_len = 2

        # general case: len >= 3 substrings
        for length in range(3, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                # a substring [i...j] a palindrome if:
                # s[i] == s[j] and 
                # substring s[i+1...j-1] is a palindrome
                if s[i] == s[j] and dp[i+1][j-1] is True:
                    dp[i][j] = True
                    if length > max_len:
                        start = i
                        max_len = length
        return s[start:start+max_len]

    
    

        # # two pointer approach
        # res = ""
        # resLen = 0 # stores length

        # for i in range(len(s)):
        #     # odd length palindrome , center i
        #     l , r = i, i 
        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         # if palindrome longest so far
        #         if (r - l + 1) > resLen:
        #             res = s[l:r+1]
        #             resLen = r - l + 1
        #         l -= 1
        #         r += 1

        #     # even length palindrome
        #     l , r = i , i + 1
        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         if (r - l + 1) > resLen:
        #             res = s[l: r+1]
        #             resLen = r - l + 1
        #         l -= 1
        #         r += 1
                

        # return res


        