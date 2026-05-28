class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freqMapS = {}
        for c in s:
            if c not in freqMapS:
                freqMapS[c] = 1
            else:
                freqMapS[c] += 1
        freqMapT = {}
        for c in t:
            if c not in freqMapT:
                freqMapT[c] = 1
            else:
                freqMapT[c] += 1
        if freqMapS == freqMapT:
            return True
        return False