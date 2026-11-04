class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        right = arr[-1]

        for i in range(len(arr)-1, -1, -1):
            if arr[i] <= right:
                arr[i] = right
            
            else:
                curr = arr[i]
                arr[i] = right
                right = curr
        
        arr[-1] = -1

        return arr