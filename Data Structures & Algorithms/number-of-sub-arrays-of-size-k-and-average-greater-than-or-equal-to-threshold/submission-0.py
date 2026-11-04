class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = 0
        right = left + k - 1
        total = 0
        res = 0

        if k == 0:
            return None

        for num in arr[left:right+1]:
            total += num

        while right < len(arr) - 1:
            if total/k >= threshold:
                res += 1
            
            total -= arr[left]
            left += 1
            right += 1
            total += arr[right]

        if total/k >= threshold:
            res += 1
        return res
        
        
