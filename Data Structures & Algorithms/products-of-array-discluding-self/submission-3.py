class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        result = [1] * n

        prefix = 1
        for i in range(1,n):
            prefix *= nums[i-1]
            result[i] = prefix
        
        postfix = 1
        for i in range(n-2,-1,-1):
            postfix *= nums[i+1]
            result[i] *= postfix
        
        return result
        