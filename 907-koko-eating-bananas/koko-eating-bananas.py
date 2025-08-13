class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # lowest eating speed is 1, highest = max(piles) (fastest possible)
        left = 1
        right = max(piles)

        # binary search to find smallest possible eating speed
        while left < right:
            middle = (left + right) // 2

            # calculate tot. hours to eat at speed mid
            total_hours = sum(math.ceil(pile / middle) for pile in piles)

            if total_hours > h:
                # took too long, try faster speed
                left = middle + 1

            else: #valid
                right = middle
        return left # or return right


        