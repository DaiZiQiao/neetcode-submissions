class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        min_k = max(piles) + 1

        while l <= r:
            mid = (l + r) // 2

            hours = 0
            for n in piles:
                hours += (n + mid - 1) // mid

            if hours <= h:
                min_k = min(min_k, mid)
                r = mid - 1
            elif hours > h:
                l = mid + 1

        return min_k