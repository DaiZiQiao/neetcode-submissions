class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_set = set(nums)
        chain = 0
        for num in num_set:
            if num - 1 not in num_set:
                curr_num = num
                curr_chain = 1
                while curr_num + 1 in num_set:
                    curr_num = curr_num + 1
                    curr_chain += 1
                chain = max(curr_chain, chain)
        return chain
