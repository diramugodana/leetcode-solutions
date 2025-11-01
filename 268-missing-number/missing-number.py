class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # for num in range len(nums), if nums not in nums, return num??
        xor_result = 0

        for i, num in enumerate(nums):
            xor_result ^= i ^ num
        xor_result ^= len(nums)
        return xor_result


        # # other approach
        # n = len(nums)
        # total = n * (n+1) // 2
        # return total - sum(nums)
