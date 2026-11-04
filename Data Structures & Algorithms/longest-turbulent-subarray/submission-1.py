class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        ans = 1
        left = 0
        prev_sign = 0

        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                sign = 1
            elif arr[i] < arr[i-1]:
                sign = -1
            else:
                sign = 0

            if sign == 0:
                left = i
                prev_sign = 0
            elif sign == prev_sign:
                left = i - 1
                prev_sign = sign
            else:
                prev_sign = sign
            
            ans = max(ans, i - left + 1)
        return ans