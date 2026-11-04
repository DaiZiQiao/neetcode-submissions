class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = right = 0
        diff = float('-inf')

        while right < len(prices):
            diff = max(diff, prices[right] - prices[left])
            if prices[right] < prices[left]:
                left = right
            right += 1
        return diff

        