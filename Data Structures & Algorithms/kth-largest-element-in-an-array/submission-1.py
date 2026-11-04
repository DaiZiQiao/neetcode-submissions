class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        if k > len(nums):
            return None

        nums = [-num for num in nums]
        heapq.heapify(nums)

        res = None
        for _ in range(k):
            res = -heapq.heappop(nums)
            
        return res