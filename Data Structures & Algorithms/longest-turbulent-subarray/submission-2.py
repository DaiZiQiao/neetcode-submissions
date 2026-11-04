class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        left = 0
        ans = 1
        prev_sign = 0

        for right in range(1, len(arr)):
            if arr[right - 1] > arr[right]:
                sign = -1
            elif arr[right -1] < arr[right]:
                sign = 1
            else:
                sign = 0
            
            # not turbulent as sign is same as prev
            if prev_sign == sign and prev_sign != 0:
                left = right - 1
                prev_sign = sign
            # if sign is 0, reassign left pointer to right
            elif sign == 0:
                left = right
            # if turbulent, just update the new prev_sign
            else:
                prev_sign = sign
            ans = max(ans, right - left + 1)
        return ans