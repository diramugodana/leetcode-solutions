class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # for each int, we count the frequency
        # for each int where its count == k, we pop all k consecutive duplicates
        # use a stack = [char, count]
        
        # for each char:
        # if stack is not empty and the current char == the top char:
        # we increment count of the char on top of stack
        # if count of top char == k:
        # we pop top char from stack
        # elif stack is empty or top char != curr char, we push c[char, count] onto stack
        # rebuild final strirng by repeating char by its count

        # each [char, count] stores consecutive entries of chars in a string state
        # therefore, stack = [["a", 2], ["b", 1], ["a"], 1] is acceptable

        stack = []

        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1

                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([char, 1])

        return "".join(char * count for char, count in stack)










            

    
            