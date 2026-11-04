class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            pairs = self.twoSum(nums, i + 1, -nums[i])
            for pair in pairs:
                triplets.append(pair + [nums[i]])
        return triplets
    
    def twoSum(self, nums, start, target):
        left = start
        right = len(nums) - 1
        pairs = []
        while left < right:
            total = nums[left] + nums[right]
            if total == target:
                pairs.append([nums[left], nums[right]])
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
            elif total < target:
                left += 1
            elif total > target:
                right -= 1
        return pairs

            