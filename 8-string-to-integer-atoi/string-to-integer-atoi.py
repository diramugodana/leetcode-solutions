class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()  # Step 1: Ignore leading whitespace
        if not s:
            return 0

        # Step 2: Determine sign
        sign = 1
        if s[0] in ['-', '+']:
            if s[0] == '-':
                sign = -1
            s = s[1:]

        # Step 3: Read digits
        result = 0
        for char in s:
            if not char.isdigit():
                break
            result = result * 10 + int(char)

        # Step 4: Apply sign
        result *= sign

        # Step 5: Clamp to 32-bit integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        return result
