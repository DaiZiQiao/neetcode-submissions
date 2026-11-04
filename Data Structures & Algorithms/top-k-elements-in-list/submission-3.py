class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        array = [[] for i in range(len(nums)+1)]
        
        for i in range(len(nums)):
            hashmap[nums[i]] = 1 + hashmap.get(nums[i],0)

        for ele, freq in hashmap.items():
            array[freq].append(ele)
        
        res = []

        for i in range((len(array))-1, 0, -1):
            for num in array[i]:
                res.append(num)
                if len(res) == k:
                    return res
            