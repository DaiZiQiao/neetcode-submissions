class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
    # h = time taken to eat all bananas
    # k = banana eaten / hr
    # need to find a suitable k such that time taken for all bananas eaten is LESS than h

        lo , hi = 1, max(piles) # lo, hi represents the lowest/highest rate of eating banana per hour


        while lo < hi:
            k = lo + (hi - lo) // 2
            acc_time = sum(math.ceil(pile / k) for pile in piles)

            if acc_time > h:
                lo = k + 1
            else:
                hi = k
        return lo
    


        