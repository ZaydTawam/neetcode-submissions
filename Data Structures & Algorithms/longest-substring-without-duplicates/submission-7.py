class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        substr_set = set()
        l = 0
        for r in range(len(s)):
            while s[r] in substr_set:
                substr_set.remove(s[l])
                l += 1
            substr_set.add(s[r])
            max_len = max(r - l + 1, max_len)

        return max_len


