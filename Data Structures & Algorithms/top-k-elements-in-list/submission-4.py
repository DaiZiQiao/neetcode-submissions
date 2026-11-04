class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        store_arr = [[] for _ in range(len(nums)+1)]

        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
        
        for num, freq in hashmap.items():
            store_arr[freq].append(num)
        print(store_arr)
        
        res = []

        for i in range(len(store_arr) -1, -1, -1):
            for num in store_arr[i]:
                res.append(num)
                if len(res) == k:
                    return res

