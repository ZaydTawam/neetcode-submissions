class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        substring_dict = {}
        l = 0
        for r in range(len(s)):
            if s[r] in substring_dict and substring_dict[s[r]] >= l:
                l = substring_dict[s[r]] + 1
            
            substring_dict[s[r]] = r
            max_len = max(max_len, r - l + 1)

        return max_len