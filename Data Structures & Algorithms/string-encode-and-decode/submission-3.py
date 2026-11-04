class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str = ""
        for word in strs:
            encode_str += str(len(word)) + '#' + word
        print(encode_str)
        return encode_str

    def decode(self, s: str) -> List[str]:
        i = 0
        decode_word = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i : j])
            decode_word.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return decode_word
