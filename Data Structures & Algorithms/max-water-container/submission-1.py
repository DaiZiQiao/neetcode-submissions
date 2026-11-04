class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_water = 0

        while left < right:
            container = (right - left) * min(heights[left], heights[right])
            if heights[left] > heights[right]:
                right -= 1
            elif heights[right] > heights[left]:
                left += 1
            else:
                right -= 1
                left += 1
            
            max_water = max(container, max_water)

        return max_water


