class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        set_n = len(set(nums))

        if set_n < n:
            return True
        return False