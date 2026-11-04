class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right 


        while left <= right:
            hours = 0
            k = (left + right) // 2
            for pile in piles:
                hours += math.ceil(pile / k)
            
            if hours <= h:
                res = min(res, k)
                right = k - 1
            else:
                left = k + 1
        return res
        