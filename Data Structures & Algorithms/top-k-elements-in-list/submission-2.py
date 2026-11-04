class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        length = len(nums)
        freq_list = [[] for i in range(length + 1)]

        # fill up hashmap
        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)
        
        for n, freq in hashmap.items():
            freq_list[freq].append(n)
            
        
        res = []

        for i in range(len(freq_list) - 1, 0, -1):
            print(freq_list[i])
            for num in freq_list[i]:
                res.append(num)
                if len(res) == k:
                    return res

        
        

