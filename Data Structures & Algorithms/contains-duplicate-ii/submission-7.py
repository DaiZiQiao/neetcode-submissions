class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        l = 0

        for i in range(len(nums)):
            if i - l <= k and nums[i] in window:
                return True
            if i - l == k and nums[l] in window:
                window.remove(nums[l])
                l += 1
            window.add(nums[i])
        
        return False