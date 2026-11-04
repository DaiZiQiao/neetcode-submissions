class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = {}

        for i, n in enumerate(nums):
            if n in window:
                if i - window[n] <= k:
                    return True
            window[n] = i

        return False