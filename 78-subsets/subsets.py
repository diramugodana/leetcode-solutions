class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [] # stores all valid subsets
        path = [] # partial solution

        def backtrack(start):
            # use path[:] to store a copy, not the current list
            res.append(path[:])
            # add each rem element one by one
            for i in range(start, len(nums)):
                # choose
                path.append(nums[i])
                # look forward, so we dont reuse elements
                backtrack(i + 1)
                # backtrack (remove last choice and explore next one)
                path.pop()

        backtrack(0)
        return res
        