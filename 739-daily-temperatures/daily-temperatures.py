class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []  # stores indices of days

        for i, temp in enumerate(temperatures):
            # While current day is warmer than the day on top of stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_day = stack.pop()
                res[prev_day] = i - prev_day  # number of days waited
            # Push current day's index
            stack.append(i)

        return res
