class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        new_dict = defaultdict(int)

        for num in nums:
            new_dict[num] += 1
        
        sorted_item = sorted(new_dict.items(), key=lambda x: x[1], reverse = True)
        res = [key for key, _ in sorted_item[:k]]

        return res