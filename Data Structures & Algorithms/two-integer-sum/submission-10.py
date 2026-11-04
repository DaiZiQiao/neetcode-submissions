class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for i in range(len(nums)):
            my_dict[nums[i]] = i
        #print(my_dict)

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in my_dict and i != my_dict[diff]:
                return [i, my_dict[diff]]
            else:
                continue
        return []