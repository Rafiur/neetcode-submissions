class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = {}
        if len(s) != len(t):
            return False
        for c in s:
            if c in freq_s:
                freq_s[c] = freq_s[c] + 1
            else:
                freq_s[c] = 1
        for c in t:
            if c in freq_s:
                if freq_s[c] == 0:
                    return False
                else:
                    freq_s[c] = freq_s[c] - 1
            else:
                return False
        return True