class Solution:

    def encode(self, strs: List[str]) -> str:
        for index, word in enumerate(strs):
            strs[index] = str(len(word)) + "#" + word
        
        encode = "".join(strs)
        print(encode)
        return encode

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            word = s[j+1 : j + length + 1]
            result.append(word)
            i = j + 1 + length
        return result