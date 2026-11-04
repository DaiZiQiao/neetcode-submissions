class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # counter that counts every 1's in the list. Once counter meets 0, it resets
        # then i will have a max_counter to store the highest number of counter

        counter = 0
        max_counter = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                counter = 0
            else:
                counter += 1
                max_counter = max(max_counter, counter)
        return max_counter