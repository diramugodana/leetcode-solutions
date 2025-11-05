class Solution:
    def minOperations(self, n: int) -> int:
        # given positive int n
        # add / subtract a power of 2 from n
        # return min no of operations to make n equal to 0

        # strategy
        # if odd, add/ minus 1
        # if n % 4 != 0, add/ subtract 1 accordingly
        # if n% 4 == 1, subtract 1
        # if n% 4 == 3, add 1
        # otherwise, add/ subtract smallest possible power of 2 to get 0
        operations = 0 
        while n != 0:
            # check if n even or odd
            if n % 2 == 0:
                n //= 2
            else:
                if n % 4 == 1 or n == 1:
                    n -= 1
                else:
                    n += 1
                operations += 1
        return operations



        