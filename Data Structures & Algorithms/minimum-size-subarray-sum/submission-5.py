class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        res = [] # list that contains the length of all subarrays
        total = 0

        while right < len(nums):
            total += nums[right]
            while total >= target:
                res.append(right - left + 1)
                total -= nums[left]
                left += 1
            
            right += 1
                
        return min(res) if res else 0
