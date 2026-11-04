class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = []

        nums.sort()

        for i,n in enumerate(nums):

            if n > 0:
                break

            if i > 0 and nums[i-1] == nums[i]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum = nums[left] + nums[right]

                if sum + n == 0 and i != left and i != right:
                    result.append([n, nums[left], nums[right]])
                    right -= 1
                    left += 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                
                elif sum + n > 0:
                    right -= 1
                else:
                    left += 1
        
        return result