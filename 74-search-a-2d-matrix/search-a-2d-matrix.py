class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # perform binary search to first find the right row
            ROWS = len(matrix) # no. of rows
            COLS = len(matrix[0]) # no. of cols

            top = 0
            bot = ROWS - 1 # len(matrix) - 1

            while top <= bot:
                row = (top + bot) // 2
                if target > matrix[row][-1]:
                    top = row + 1
                elif target < matrix[row][0]:
                    bot = row - 1
                else:
                    break # target is now within the row range

            # Finds the first row such that:
            # matrix[row][0] <= target <= matrix[row][-1]
            # If no such row is found, it exits the loop.

            if not (top <= bot):
                return False

            # now d normal binary search within that row
            row = (top + bot) // 2
            l = 0
            r = COLS - 1 # last index in the row

            while l <= r:
                m = (l + r) // 2
                if target > matrix[row][m]:
                    l = m + 1
                elif target < matrix[row][m]:
                    r = m - 1
                else:
                    return True
            return False
