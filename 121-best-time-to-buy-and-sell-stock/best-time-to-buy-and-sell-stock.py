class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prices[i] is price of a given stock on the ith day
        # find min and the greatest max after it, and minus
        # brute force approach would be 
        # for every day you buy, check all follwing, and find diff, then return max diff? 
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit

        # time complexity = O(n)
        # space complexity = O(1)
