class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        left = 0
        answer = 1
        prev_sign = 0

        for right in range(1, len(arr)):
            if arr[right-1] > arr[right]:
                sign = -1
            elif arr[right-1] < arr[right]:
                sign = 1
            else:
                sign = 0
            # if pre
            if sign == 0:
                left = right
            elif prev_sign == sign:
                left = right -1
                prev_sign = sign
            else:
                prev_sign = sign
            answer = max(answer, right - left + 1)
        return answer