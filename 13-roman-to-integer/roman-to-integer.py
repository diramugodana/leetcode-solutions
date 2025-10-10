class Solution:
    def romanToInt(self, s: str) -> int:
        # first map the main romans to numbers
        mapping = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        total_sum = 0
        n = len(s)

        for i in range(n):
            current_value = mapping[s[i]]

        # avoid out of bounds error, and check if we need to subtract=1
            if i + 1 < n and current_value < mapping[s[i+1]]:
                total_sum -= current_value
            else:
                total_sum += current_value
        
        return total_sum

        