class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = 0
        min_length = float('inf')
        curr_sum = 0

        while right < len(nums):
            curr_sum += nums[right]  
            while curr_sum >= target:
                min_length = min(min_length, right - left + 1)
                curr_sum -= nums[left]
                left += 1
            
            right += 1


        if min_length == float('inf'):
            min_length = 0
        return min_length
