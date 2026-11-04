class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        res = {}
        if k == 0:
            return False

        for i in range(len(nums)):

            if nums[i] in res and i - res[nums[i]] <= k:
                return True

            res[nums[i]] = i
        return False

