class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        new_s = "".join(sorted(s))
        new_t = "".join(sorted(t))

        for i in range(0, len(s)):
            if new_s[i] != new_t[i]:
                return False
        return True