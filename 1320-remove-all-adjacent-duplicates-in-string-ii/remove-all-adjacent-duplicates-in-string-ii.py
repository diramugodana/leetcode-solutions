class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # for every removed substring, concatenate the left & right
        # pass over the new string doing the same thing
        # 

        if len(s) <= 1:
            return s

        stack = []

        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([char, 1])

        return "".join(char * count for char, count in stack)


        