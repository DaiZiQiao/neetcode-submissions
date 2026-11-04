class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1

        l_max = height[left]
        r_max = height[right]
        acc_water = 0

        while left < right:
            if l_max < r_max:
                left += 1
                l_max = max(height[left], l_max)
                acc_water += l_max - height[left]
            else:
                right -= 1
                r_max = max(height[right], r_max)
                acc_water += r_max - height[right]
        return acc_water
