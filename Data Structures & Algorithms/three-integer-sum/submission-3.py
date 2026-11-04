class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            pairs = self.twoSum(nums, i+1,-nums[i])
            for pair in pairs:
                triplets.append(pair + [nums[i]])
        return triplets
    
    def twoSum(self, lst, start, target):
        left, right = start, len(lst) - 1
        pairs = []
        while left < right:
            total = lst[left] + lst[right]
            if total == target:
                pairs.append([lst[left], lst[right]])
                left += 1
                while left < right and lst[left] == lst[left - 1]:
                    left += 1
            elif total > target:
                right -=1
            elif total < target:
                left += 1
        return pairs
        