class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # each permutation same size as nums
        res = []
        path = []
        used = [False] * len(nums)

        def backtrack():
            # base case
            if len(path) == len(nums):
                res.append(path[:])
                return 

            for i in range(len(nums)):
                if used[i]:
                    continue

                path.append(nums[i])
                used[i] = True
                backtrack()
                path.pop()
                used[i] = False

        backtrack()
        return res


        