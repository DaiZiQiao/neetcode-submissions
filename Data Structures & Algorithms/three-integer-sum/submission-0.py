class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # a + b + c = 0
        # b + c = -a
        sorted_nums = sorted(nums)
        res = []
        for i in range(len(sorted_nums)):
            if sorted_nums[i] > 0:
                break
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue
            pairs = self.twoSum(sorted_nums, i + 1, -sorted_nums[i])
            for pair in pairs:
                res.append([sorted_nums[i]] + pair)
        return res
    
    def twoSum(self, nums, start, target): 
        left, right = start, len(nums) - 1
        pairs = []
        while left < right:
            combine = nums[left] + nums[right]
            if combine == target:
                pairs.append([nums[left], nums[right]])
                left += 1
                while left < right and nums[left] ==nums[left-1]:
                    left +=1
            elif combine > target:
                right -= 1
            elif combine < target:
                left += 1
        return pairs