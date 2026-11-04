class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_profit = 0

        for i,n in enumerate(prices):
            if i != l:
                max_profit = max(max_profit, n - prices[l])

            if n <= prices[l]:
                l = i

        return max_profit