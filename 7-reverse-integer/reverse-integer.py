class Solution:
    def reverse(self, x: int) -> int:
        
        s = str(x)
       
        if s[0] == '-':
             reversed_s = '-' + s[:0:-1].lstrip('0')
        else:
            reversed_s = s[::-1].lstrip('0')

        result = int(reversed_s) if reversed_s not in ('', '-') else 0

        if -2**31 <= result <= 2**31 - 1:
            return result
        return 0
        