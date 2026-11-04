class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_dict = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c)-ord('a')] += 1
            new_dict[tuple(count)].append(word)
        return list(new_dict.values())