class Solution:
    def countBits(self, n: int) -> List[int]:
        # count the number of 1s in binary rep of each number in given range
        # i & (i-1) removes exactly one bit from i (last bit)

        # empty dp table
        res = [0] * (n+1)

        for i in range(1, n+1):
            res[i] = res[i & (i-1)] + 1
        return res
        