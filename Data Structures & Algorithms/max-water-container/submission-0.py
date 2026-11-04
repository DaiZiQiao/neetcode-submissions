class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_water = 0
        while left < right:
            width = right - left
            amount = min(heights[left], heights[right]) * width
            if amount > max_water:
                max_water = amount
            print(width, amount, max_water)
            if heights[left] > heights[right]:
                right -= 1
            elif heights[right] > heights[left]:
                left += 1
            else:
                left += 1
                right -=1
        return max_water