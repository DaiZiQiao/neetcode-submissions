class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window = k
        total = 0
        counter = 0
        left = 0

        for right in range(len(arr)):
            total += arr[right]
        
            if right - left + 1> window:
                total -= arr[left]
                left += 1
            if right - left + 1 == window and total >= k * threshold:
                counter += 1
            
        return counter
