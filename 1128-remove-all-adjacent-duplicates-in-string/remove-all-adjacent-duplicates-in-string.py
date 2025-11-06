class Solution:
    def removeDuplicates(self, s: str) -> str:

        # stack = []
        # for char in s:
        #     if stack and stack[-1][0] == char:
        #         stack[-1][1] += 1

        #         if stack[-1][1] == 2:
        #             stack.pop()
            
        #     else:
        #         stack.append([char, 1])
            
        # return "".join(char * count for char, count in stack)

        stack = []

        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)


        