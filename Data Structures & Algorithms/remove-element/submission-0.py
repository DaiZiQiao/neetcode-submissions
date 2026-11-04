class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # any nums[i] == val must be removed
        i = 0
        n = len(nums)

        while i < n:
            if nums[i] == val:
                n -= 1
                nums[i] = nums[n]
            else:
                i +=1
        
        return n