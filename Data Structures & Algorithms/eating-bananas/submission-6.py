class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        res = r

        while l <= r:
            k = (l + r) // 2

            hours = 0
            for n in piles:
                hours += math.ceil(n/k)

            if hours <= h:
                res = k
                r = k - 1
            elif hours > h:
                l = k + 1

        return res