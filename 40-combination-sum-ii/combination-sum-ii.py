class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # we are not gonna be reusing any int 
        res = [] 
        path = [] # partial answer
        candidates.sort()

        def backtrack(start, total):
            if total == target:
                res.append(path[:])
                return 

            if total > target:
                return 

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue 
                path.append(candidates[i])
                backtrack(i+1, total + candidates[i])
                path.pop()

        backtrack(0, 0)
        return res
            
        