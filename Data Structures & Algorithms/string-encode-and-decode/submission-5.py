class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str = ""
        for word in strs:
            encode_str += str(len(word)) + "#" + word
        return encode_str


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            print(length)
            i = j+1
            j = j + length + 1
            res.append(s[i:j])
            i = j
        return res
