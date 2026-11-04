class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        if not numbers:
            return []

        while left < right:
            combine = numbers[left] + numbers[right]
            if combine == target:
                return [left + 1, right + 1]
            elif combine < target:
                left += 1
            elif combine > target:
                right -= 1


